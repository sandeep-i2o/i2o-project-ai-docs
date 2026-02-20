"""
md_to_pdf.py
============
Convert Markdown files (including Mermaid diagrams) to PDF.

Usage:
    # One or more files — one PDF per file
    python md_to_pdf.py report.md design.md

    # Entire directory
    python md_to_pdf.py ./docs

Requirements:
    pip install markdown weasyprint pymupdf pygments

External tool (must be on PATH):
    npm install -g @mermaid-js/mermaid-cli
    # verfy with: mmdc --version
"""

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import fitz                          # PyMuPDF  — PDF merging
import markdown
from pygments.formatters import HtmlFormatter
from weasyprint import CSS, HTML

# ── CSS ───────────────────────────────────────────────────────────────────────

PYGMENTS_CSS = HtmlFormatter(style="friendly").get_style_defs(".highlight")

BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Fira+Code&display=swap');

@page {
    size: A4;
    margin: 2.2cm 2.5cm 2.8cm 2.5cm;
    @bottom-left {
        content: "© 2026 i2o Retail";
        font-family: 'Inter', sans-serif;
        font-size: 9pt;
        color: #888;
    }
    @bottom-right {
        content: counter(page) " / " counter(pages);
        font-family: 'Inter', sans-serif;
        font-size: 9pt;
        color: #888;
    }
}

body {
    font-family: 'Inter', sans-serif;
    font-size: 11pt;
    line-height: 1.7;
    color: #1a1a2e;
    max-width: 100%;
}

h1, h2, h3, h4, h5, h6 {
    font-weight: 700;
    color: #1F3864;
    margin-top: 1.4em;
    margin-bottom: 0.4em;
    line-height: 1.3;
}

h1 { font-size: 22pt; border-bottom: 3px solid #2E75B6; padding-bottom: 6px; }
h2 { font-size: 16pt; border-bottom: 1px solid #d0dce8; padding-bottom: 4px; }
h3 { font-size: 13pt; color: #2E75B6; }
h4 { font-size: 11pt; }

p  { margin: 0.5em 0 0.9em 0; }

a  { color: #2E75B6; text-decoration: none; }

/* Inline code */
code {
    font-family: 'Fira Code', monospace;
    font-size: 9.5pt;
    background: #eef3f9;
    border: 1px solid #d0dce8;
    border-radius: 3px;
    padding: 1px 5px;
}

/* Code blocks */
pre {
    background: #f4f7fb;
    border: 1px solid #d0dce8;
    border-left: 4px solid #2E75B6;
    border-radius: 5px;
    padding: 12px 16px;
    overflow-x: auto;
    font-size: 9pt;
    line-height: 1.5;
}
pre code { background: none; border: none; padding: 0; }

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
    font-size: 10pt;
}
th {
    background: #2E75B6;
    color: #fff;
    font-weight: 600;
    padding: 8px 12px;
    text-align: left;
}
td { padding: 7px 12px; border-bottom: 1px solid #d0dce8; }
tr:nth-child(even) td { background: #eef3f9; }

/* Blockquote */
blockquote {
    border-left: 4px solid #2E75B6;
    margin: 0.8em 0;
    padding: 6px 16px;
    background: #eef3f9;
    color: #444;
    border-radius: 0 4px 4px 0;
}

/* Mermaid diagrams rendered as images */
.mermaid-diagram {
    text-align: center;
    margin: 1.4em 0;
    page-break-inside: avoid;
}
.mermaid-diagram img {
    max-width: 100%;
    height: auto;
    border: 1px solid #d0dce8;
    border-radius: 6px;
    padding: 8px;
    background: #fff;
}

/* Horizontal rule */
hr { border: none; border-top: 2px solid #d0dce8; margin: 1.5em 0; }

/* Lists */
ul, ol { padding-left: 1.5em; margin: 0.5em 0 0.9em 0; }
li { margin-bottom: 0.3em; }
"""

# ── Mermaid rendering ─────────────────────────────────────────────────────────

def check_mmdc():
    if not shutil.which("mmdc"):
        print(
            "ERROR: 'mmdc' not found on PATH.\n"
            "Install it with:  npm install -g @mermaid-js/mermaid-cli",
            file=sys.stderr,
        )
        sys.exit(1)

def render_mermaid(code: str, tmp_dir: Path, index: int) -> Path:
    """Write Mermaid source to a temp file, render to PNG via mmdc."""
    src  = tmp_dir / f"diagram_{index}.mmd"
    out  = tmp_dir / f"diagram_{index}.png"
    src.write_text(code, encoding="utf-8")
    result = subprocess.run(
        ["mmdc", "-i", str(src), "-o", str(out),
         "-b", "white", "-w", "1200", "--scale", "2"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"  ⚠  mmdc warning for diagram {index}: {result.stderr.strip()}")
    return out

# ── Markdown processing ───────────────────────────────────────────────────────

MERMAID_RE = re.compile(
    r"```mermaid\s*\n(.*?)```",
    re.DOTALL | re.IGNORECASE,
)

def preprocess_mermaid(md_text: str, tmp_dir: Path) -> str:
    """Replace ```mermaid blocks with <img> tags pointing to rendered PNGs."""
    diagrams = {}
    for i, m in enumerate(MERMAID_RE.finditer(md_text)):
        code = m.group(1).strip()
        png  = render_mermaid(code, tmp_dir, i)
        diagrams[m.group(0)] = png

    for raw, png in diagrams.items():
        img_tag = (
            f'<div class="mermaid-diagram">'
            f'<img src="{png.as_posix()}" alt="Diagram"/>'
            f'</div>'
        )
        md_text = md_text.replace(raw, img_tag)

    return md_text

def md_to_html(md_text: str, tmp_dir: Path) -> str:
    """Full pipeline: preprocess Mermaid → convert Markdown → wrap HTML."""
    processed = preprocess_mermaid(md_text, tmp_dir)

    extensions = [
        "extra",          # tables, fenced code, footnotes, attr_list
        "codehilite",     # syntax highlighting via Pygments
        "toc",            # table of contents anchors
        "nl2br",          # newlines → <br>
        "sane_lists",
    ]
    ext_configs = {
        "codehilite": {"css_class": "highlight", "guess_lang": True},
        "toc":        {"permalink": False},
    }
    body = markdown.markdown(processed, extensions=extensions,
                              extension_configs=ext_configs)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<style>
{PYGMENTS_CSS}
{BASE_CSS}
</style>
</head>
<body>
{body}
</body>
</html>"""

# ── PDF conversion ────────────────────────────────────────────────────────────

def html_to_pdf(html: str, out_path: Path):
    HTML(string=html).write_pdf(str(out_path))

def convert_file(md_path: Path, out_dir: Path, tmp_dir: Path) -> Path:
    """Convert a single Markdown file → PDF. Returns the PDF path."""
    print(f"  📄  {md_path.name}")
    text     = md_path.read_text(encoding="utf-8")
    html     = md_to_html(text, tmp_dir)
    pdf_path = out_dir / (md_path.stem + ".pdf")
    html_to_pdf(html, pdf_path)
    print(f"       → {pdf_path}")
    return pdf_path

def merge_pdfs(pdf_paths: list[Path], out_path: Path):
    """Merge multiple PDFs into one using PyMuPDF."""
    merged = fitz.open()
    for p in pdf_paths:
        merged.insert_pdf(fitz.open(str(p)))
    merged.save(str(out_path))
    merged.close()
    print(f"\n📦  Merged PDF → {out_path}")

# ── CLI ───────────────────────────────────────────────────────────────────────

def resolve_inputs(inputs: list[str]) -> list[Path]:
    """Accept files and/or directories; return sorted list of .md paths."""
    paths = []
    for raw in inputs:
        p = Path(raw)
        if p.is_dir():
            paths.extend(sorted(p.rglob("*.md")))
        elif p.is_file() and p.suffix.lower() == ".md":
            paths.append(p)
        else:
            print(f"  ⚠  Skipping '{raw}' (not a .md file or directory)")
    if not paths:
        print("No Markdown files found.", file=sys.stderr)
        sys.exit(1)
    return paths

def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert Markdown + Mermaid files to PDF."
    )
    parser.add_argument(
        "inputs", nargs="+",
        help="Markdown files or directories to convert"
    )
    parser.add_argument(
        "--out-dir", default=".",
        help="Directory for individual PDFs (default: current directory)"
    )
    return parser.parse_args()

# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    check_mmdc()
    args    = parse_args()
    md_files = resolve_inputs(args.inputs)
    out_dir  = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n🔄  Converting {len(md_files)} file(s)…\n")

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir  = Path(tmp)
        pdf_list = [convert_file(f, out_dir, tmp_dir) for f in md_files]

    print("\n✅  Done.")

if __name__ == "__main__":
    main()