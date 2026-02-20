GitHub URL: git@github.com:i2o-retail/i2o-admin-UI.git

# i2o Admin UI - Development Guide

## Project Overview

The **i2o Admin UI** is a modern React-based single-page application (SPA) serving as the operational dashboard for i2o Retail's internal teams. It provides interfaces for managing resellers, enforcement operations, invoicing, user management, and product tracking.

The application is built with **Vite** for fast development and bundling, uses **React** for the UI, and leverages a component-first architecture with **Shadcn UI** and **Tailwind CSS**. State management and data fetching are handled by **TanStack Query**, with authentication via **Keycloak**.

## Technology Stack

| Category | Technology | Version | Purpose |
|----------|------------|---------|---------|
| **Core Framework** | React | 18.3.1 | UI Library |
| **Build Tool** | Vite | 5.4.1 | Development server & bundler |
| **Language** | TypeScript | 5.5.3 | Type safety |
| **Styling** | Tailwind CSS | 3.4.11 | Utility-first CSS |
| **UI Components** | Shadcn UI | (latest) | Reusable component primitives |
| **Routing** | React Router DOM | 6.26.2 | Client-side routing |
| **State Management** | TanStack Query | 5.56.2 | Server state & caching |
| **Forms** | React Hook Form | 7.60.0 | Form handling |
| **Schema Validation**| Zod | 3.23.8 | Data validation |
| **Authentication** | Keycloak-js | 26.2.0 | Identity management |
| **Testing** | Vitest / Playwright | 3.2.4 / 1.55.0 | Unit & E2E testing |
| **Icons** | Lucide React | 0.462.0 | Iconography |

## Project Structure

```
i2o-admin-UI/
├── src/
│   ├── api/                # API client configuration (Axios)
│   ├── components/         # Reusable UI components
│   │   ├── ui/             # Shadcn UI primitives (Button, Input, Table, etc.)
│   │   ├── shared/         # app-specific reusable components (DataTable, Filters)
│   │   └── Layout.tsx      # Main application layout
│   ├── contexts/           # React Context providers (Notification, Auth)
│   ├── features/           # Feature-based modules (Domain Driven Design)
│   │   ├── EnforcementModule/
│   │   ├── InvoiceModule/
│   │   ├── ProductTrackingModule/
│   │   ├── ReportModule/
│   │   └── ResellersModule/
│   ├── hooks/              # Custom React hooks
│   ├── lib/                # Utilities and configurations (utils.ts, firebase.ts)
│   ├── pages/              # Route components (Page level)
│   ├── services/           # Service layer for complex business logic
│   ├── types/              # TypeScript type definitions
│   ├── App.tsx             # Main app component & Routing setup
│   └── main.tsx            # Entry point
├── public/                 # Static assets
└── package.json            # Dependencies and scripts
```

## Key Development Concepts

### 1. Feature-Based Architecture
The project is organized by "features" in `src/features`. Each feature folder (e.g., `ResellersModule`) contains components, hooks, and logic specific to that business domain.
- **Goal**: Keep related code together.
- **Rule**: If a component is only used within "Resellers", place it in `src/features/ResellersModule/components`. If it's used across multiple features, move it to `src/components/shared`.

### 2. UI Components (Shadcn UI)
We use [Shadcn UI](https://ui.shadcn.com/) which copies component code directly into `src/components/ui`.
- **Customization**: You can modify these files directly to fit design requirements.
- **Styling**: All styling is done via Tailwind CSS classes.

### 3. Data Fetching (TanStack Query)
All server state is managed via `useQuery` and `useMutation`.
- **API Client**: `src/api/index.ts` exports an Axios instance with interceptors for auth tokens.
- **Services**: Complex API interactions should be encapsulated in `src/services` (e.g., `generateCssService.ts`) or `src/api` helper functions.
- **Caching**: Queries are cached by default. Configuration is in `src/lib/ReactQueryConfig.ts`.

### 4. Authentication (Keycloak)
Authentication is handled via `KeycloakProvider` in `src/hooks/useKeycloak`.
- **Protection**: Routes are protected using `src/components/ProtectedRoute.tsx`.

## Key Workflows & Features

| Feature | Description | Key Components |
|---------|-------------|----------------|
| **Resellers** | Manage reseller accounts, enforcement status, and details. | `ResellersPageRefactored`, `ResellersModule` |
| **Enforcement** | Handle violation notifications, emails, and reporting. | `EnforcementOpsPageRefactored`, `EnforcementModule` |
| **Invoicing** | Manage client invoices and billing operations. | `InvoiceOpsPage`, `InvoiceModule` |
| **Product Tracking** | Dashboard for monitoring product metrics. | `ProductTrackingDashboard`, `ProductTrackingModule` |
| **CSS Generator** | Tool to generate custom stylesheets for reports. | `CssGenerator`, `generateCssService` |
| **User Mgmt** | Administer application users and roles. | `UsersPage` |

## How to Develop

### Adding a New Component
1. **Primitive**: If it's a basic UI element, check `src/components/ui`. If missing, install via shadcn CLI or create in `src/components/shared` if bespoke.
2. **Feature Component**: Create in `src/features/<ModuleName>/components`.

### Adding a New Page
1. Create the page component in `src/pages/NewPage.tsx`.
2. Add the route in `src/App.tsx` inside the `<ProtectedRoute>` wrapper.
3. Update `src/components/AppSidebar.tsx` to add a navigation link if needed.

### Styling Guidelines
- Use **Tailwind CSS** for all styling.
- Use `hsl(var(--variable))` for colors to support theming (defined in `index.css`).
- Follow the spacing and typography scales defined in `tailwind.config.ts`.
- **Fonts**: The application uses "DM Sans".

## Deployment

Build the application for production:
```bash
npm run build
```
This produces optimized static assets in the `dist/` directory, ready to be served by Nginx, AWS S3/CloudFront, or Docker.

### Environment Variables
Create a `.env` file in the root:
```env
VITE_API_BASE_URL=https://api.example.com
VITE_KEYCLOAK_URL=https://auth.example.com
VITE_KEYCLOAK_REALM=i2o-realm
VITE_KEYCLOAK_CLIENT_ID=i2o-admin-ui
```
