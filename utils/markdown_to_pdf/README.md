# Markdown to PDF MCP Tool

This tool allows you to convert Markdown files (including Mermaid diagrams) into beautifully styled PDF documents via the Model Context Protocol (MCP).

## Prerequisites

1.  **Python 3.10+**
2.  **System Dependencies** (for WeasyPrint on macOS):
    ```bash
    brew install python pango libffi
    ```
3.  **Mermaid CLI** (for diagram rendering):
    ```bash
    npm install -g @mermaid-js/mermaid-cli
    ```
4.  **Python Dependencies**:
    Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## How to Add to Antigravity MCP Server List

To add this tool to your Antigravity (or Claude) configuration, follow these steps:

1.  Open your MCP configuration file (e.g., `~/.gemini/antigravity/mcp_config.json` or equivalent).
2.  Add the following entry under the `mcpServers` object:

```json
{
  "mcpServers": {
    "markdown-to-pdf": {
      "command": "python3",
      "args": [
        "/Users/sandeepofficial/Documents/workspace/ai-accelerate/i2o-feature-ai-docs/utils/markdown_to_pdf/mcp_server.py"
      ],
      "env": {}
    }
  }
}
```

> **Note**: Ensure that the Python environment used in the `command` field has the dependencies from `requirements.txt` installed. If you are using `uv`, you can use `"command": "uv", "args": ["run", ".../mcp_server.py"]` instead.

## Available Tools

-   `convert_markdown_to_pdf`: Converts a string of Markdown text into a PDF file at a specified path.
-   `convert_markdown_file_to_pdf`: Reads an existing `.md` file and saves it as a `.pdf`.

## Features

-   **Premium Aesthetics**: Uses a curated color palette and modern typography (Inter).
-   **Syntax Highlighting**: Beautifully formatted code blocks via Pygments.
-   **Mermaid Support**: Automatically renders Mermaid code blocks into high-resolution diagrams.
-   **Professional Layout**: Includes page numbers, footers, and a clean table of contents (if requested in MD).
