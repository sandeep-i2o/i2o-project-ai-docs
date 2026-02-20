GitHub URL: git@github.com:i2o-retail/frontendapplication-i2oretail.git

# I2O Retail - Frontend Application

A comprehensive Angular-based retail analytics and monitoring platform for e-commerce business intelligence.

---

## 📋 Table of Contents

- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Key Modules](#key-modules)
- [Core Services](#core-services)
- [Authentication System](#authentication-system)
- [Environment Configuration](#environment-configuration)
- [Development Setup](#development-setup)
- [Build & Deployment](#build--deployment)
- [Key Files Reference](#key-files-reference)
- [Coding Guidelines](#coding-guidelines)

---

## 🛠 Technology Stack

| Category | Technology | Version |
|----------|------------|---------|
| **Framework** | Angular | 15.2.10 |
| **Language** | TypeScript | 4.9.5 |
| **UI Libraries** | Angular Material | 15.2.9 |
|                  | PrimeNG | 15.0.0 |
|                  | Bootstrap | 5.2.0 |
| **Data Grid** | AG Grid Enterprise | 21.1.1 |
| **Charts** | ECharts | 6.0.0 |
|            | FusionCharts | 3.23.0 |
| **Authentication** | Keycloak Angular | 13.1.0 |
| **State Management** | RxJS | 7.5.7 |
| **Real-time** | Socket.io Client | 2.3.1 |
| **Date Handling** | Moment.js / Luxon | 2.27.0 / 3.7.1 |
| **Testing** | Jasmine/Karma | ~3.6.0 / ~6.4.4 |
| **E2E Testing** | Protractor | ~7.0.0 |

---

## 📁 Project Structure

```
frontendapplication-i2oretail/
├── src/
│   ├── app/
│   │   ├── auth/                    # Authentication guards & interceptors
│   │   ├── directives/              # Custom Angular directives
│   │   ├── main/                    # Main layout components
│   │   │   ├── new-reseller-management/
│   │   │   ├── reseller-library/
│   │   │   └── shared/
│   │   ├── modules/                 # Feature modules (39 modules)
│   │   │   ├── alerts/
│   │   │   ├── brand-content-monitoring/
│   │   │   ├── common/              # Shared components & utilities
│   │   │   ├── core/                # Core functionality
│   │   │   ├── dashboard/
│   │   │   ├── detailTables/
│   │   │   ├── home/
│   │   │   ├── marketplace/
│   │   │   ├── portfolioSummary/
│   │   │   ├── price-monitor/
│   │   │   ├── price-monitor-alerts/
│   │   │   ├── promotions/
│   │   │   ├── sales-analysis/
│   │   │   ├── summary/
│   │   │   └── ... (more modules)
│   │   ├── pipes/                   # Custom pipes
│   │   ├── services/                # Application services (45 services)
│   │   ├── shared/                  # Shared interfaces & utilities
│   │   ├── styles/                  # SCSS/CSS styles
│   │   ├── app.component.ts         # Root component
│   │   ├── app.module.ts            # Root module
│   │   └── app-routing.module.ts    # Application routing
│   ├── assets/                      # Static assets
│   │   ├── fonts/
│   │   ├── icons/
│   │   ├── img/
│   │   ├── json/
│   │   ├── themes/
│   │   └── videos/
│   ├── environments/                # Environment configurations
│   ├── index.html                   # Main HTML entry
│   ├── main.ts                      # Application bootstrap
│   ├── styles.scss                  # Global styles
│   └── styles.css                   # Compiled CSS
├── e2e/                             # End-to-end tests
├── angular.json                     # Angular CLI configuration
├── package.json                     # Dependencies & scripts
├── tsconfig.json                    # TypeScript configuration
└── tslint.json                      # Linting rules
```

---

## 🧩 Key Modules

### Business Feature Modules

| Module | Path | Description |
|--------|------|-------------|
| **Dashboard** | `modules/dashboard/` | Main analytics dashboard |
| **Home** | `modules/home/` | Home/landing views |
| **Portfolio Summary** | `modules/portfolioSummary/` | Portfolio analytics & summaries |
| **Marketplace** | `modules/marketplace/` | Marketplace management |
| **Price Monitor** | `modules/price-monitor/` | Price tracking & monitoring |
| **Price Monitor Alerts** | `modules/price-monitor-alerts/` | Price change alert system |
| **Promotions** | `modules/promotions/` | Promotional campaign management |
| **Sales Analysis** | `modules/sales-analysis/` | Sales analytics & reports |
| **Summary** | `modules/summary/` | Summary reports & views |
| **Brand Content Monitoring** | `modules/brand-content-monitoring/` | Brand content tracking |
| **Alerts** | `modules/alerts/` | Alert management system |
| **Exception Management** | `modules/exceptionmanagement/` | Exception handling & workflows |

### Infrastructure Modules

| Module | Path | Description |
|--------|------|-------------|
| **Common** | `modules/common/` | Shared components (~787 files) |
| **Core** | `modules/core/` | Core application services |
| **Generic Module** | `modules/generic-module/` | Generic reusable components |
| **Generic Layout** | `modules/generic-layout-component/` | Layout templates |

---

## ⚙️ Core Services

Services are located in `src/app/services/`. Key services include:

### API & Communication
| Service | File | Purpose |
|---------|------|---------|
| **REST API Service** | `rest-api.service.ts` | Main HTTP client for backend APIs |
| **Socket Service** | `socket.service.ts` | Real-time WebSocket communication |
| **Share Link Service** | `share-link.service.ts` | Link sharing functionality |

### Data & State Management
| Service | File | Purpose |
|---------|------|---------|
| **Util Service** | `util.service.ts` | General utility functions |
| **Master Data Service** | `master-data.service.ts` | Master data handling |
| **Filter Data Service** | `filter-data.service.ts` | Data filtering logic |
| **User Persistence Service** | `user.persistence.service.ts` | User state persistence |
| **Current State Cache Service** | `current-state-cache.service.ts` | Application state caching |

### Business Logic
| Service | File | Purpose |
|---------|------|---------|
| **Generic Module Service** | `generic-module.service.ts` | Generic module operations |
| **Product Master Service** | `product-master.service.ts` | Product catalog management |
| **Portfolio Summary Service** | `portfolio-summary.service.ts` | Portfolio analytics |
| **Scheduler Service** | `scheduler-service.ts` | Task scheduling |

### UI & Experience
| Service | File | Purpose |
|---------|------|---------|
| **Event Emit Service** | `event-emit.service.ts` | Event-based communication |
| **Open Dialog Service** | `open-dialog.service.ts` | Dialog management |
| **App Theme Service** | `app-theme.service.ts` | Theme management |
| **Toggle Sidenav Service** | `toggle-sidenav.service.ts` | Navigation state |
| **Google Analytics Service** | `google-analytics.service.ts` | Analytics tracking |

### Grid & Export
| Service | File | Purpose |
|---------|------|---------|
| **Grid Event Service** | `grid-event.service.ts` | AG Grid event handling |
| **Grid Report Service** | `grid.report.service.ts` | Grid-based reporting |
| **Export Utility Service** | `export-utility.service.ts` | Data export functionality |
| **Data Grid Utility Service** | `data-grid-utility.service.ts` | Grid utilities |

---

## 🔐 Authentication System

The application uses **Keycloak** for authentication and authorization.

### Auth Components (`src/app/auth/`)

| File | Purpose |
|------|---------|
| `auth.interceptor.ts` | HTTP request interceptor for auth tokens |
| `keycloak-authentication.guard.ts` | Keycloak-based route protection |
| `logged-in-users.guard.ts` | Guard for authenticated users |
| `roles-based-auth.gaurd.ts` | Role-based access control |
| `business-view-filter.guard.ts` | Business view access control |
| `custom-redirect.guard.ts` | Custom redirect handling |
| `permission.guard.ts` | Permission checking |

### Authentication Flow

1. Application bootstraps with Keycloak initialization (`app.module.ts`)
2. `kcInitializer` function handles SSO and token management
3. Route guards (`LoggedInUsersGuard`, `RoleBasedAuthGuard`) protect routes
4. `KeycloakBearerInterceptor` attaches tokens to API requests

---

## 🌍 Environment Configuration

### Environment Files

| File | Purpose |
|------|---------|
| `src/environments/environment.ts` | Development environment |
| `src/environments/environment.prod.ts` | Production environment |

### Environment Variables

```typescript
// environment.prod.ts
export const environment = {
  production: true  // Enable production mode
};
```

> **Note**: Additional environment-specific variables (API URLs, Keycloak config, etc.) may be configured at runtime or through deployment configuration.

### Keycloak Configuration

Keycloak settings are typically configured via:
- Cookie-based token storage
- Runtime configuration from backend API calls
- Environment-specific Keycloak realm/client settings

---

## 💻 Development Setup

### Prerequisites

- **Node.js**: v14.x or higher recommended
- **npm**: v6.x or higher
- **Angular CLI**: v15.x

### Installation

```bash
# Clone the repository
git clone <repository-url>

# Navigate to project directory
cd frontendapplication-i2oretail

# Install dependencies
npm install
```

### Running Development Server

```bash
# Start development server
npm start

# Or using Angular CLI directly
ng serve
```

Navigate to `http://localhost:4200/`. The app auto-reloads on file changes.

### Running Tests

```bash
# Unit tests
npm test

# End-to-end tests
npm run e2e

# Linting
npm run lint
```

---

## 🚀 Build & Deployment

### Development Build

```bash
npm run build
```

### Production Build

```bash
npm run build_prod
```

Build artifacts are stored in `dist/i2o-retail/`.

### Build Configuration

Key build settings in `angular.json`:
- **Output Hashing**: Enabled for production
- **AOT Compilation**: Enabled by default
- **Source Maps**: Enabled for dev, disabled for prod
- **Budget**: 5MB warning, 20MB error limit

---

## 📄 Key Files Reference

| File | Description |
|------|-------------|
| `src/main.ts` | Application entry point, AG Grid license setup |
| `src/app/app.module.ts` | Root module with Keycloak initialization |
| `src/app/app-routing.module.ts` | Main routing configuration (800+ lines) |
| `src/app/app.component.ts` | Root component |
| `angular.json` | Angular CLI workspace configuration |
| `package.json` | Dependencies and npm scripts |
| `tsconfig.json` | TypeScript compiler options |
| `karma.conf.js` | Unit test configuration |
| `src/styles.scss` | Global SCSS styles |
| `src/index.html` | Main HTML template |

---

## 📐 Coding Guidelines

### Component Structure

```
component-name/
├── component-name.component.ts      # Component class
├── component-name.component.html    # Template
├── component-name.component.scss    # Styles (or .css)
└── component-name.component.spec.ts # Unit tests
```

### Module Structure

```
module-name/
├── module-name.module.ts            # Module definition
├── module-name-routing.module.ts    # Routing (if lazy-loaded)
├── components/                      # Module components
├── services/                        # Module-specific services
└── models/                          # Interfaces & types
```

### Naming Conventions

- **Components**: `kebab-case` for folders and files
- **Services**: `*.service.ts`
- **Guards**: `*.guard.ts`
- **Pipes**: `*.pipe.ts`
- **Interfaces**: PascalCase, prefixed with `I` (optional)

### Best Practices

1. **Lazy Loading**: Use lazy loading for feature modules
2. **Shared Module**: Use `modules/common/` for shared components
3. **Services**: Injectable services should be provided in root or specific modules
4. **State Management**: Use RxJS BehaviorSubjects for state
5. **Type Safety**: Prefer interfaces and strong typing

---

## 📊 Third-Party Integrations

| Integration | Purpose | Documentation |
|-------------|---------|---------------|
| **Keycloak** | Identity & Access Management | [Keycloak Docs](https://www.keycloak.org/documentation) |
| **AG Grid Enterprise** | Data Grid | [AG Grid Docs](https://www.ag-grid.com/documentation/) |
| **ECharts** | Data Visualization | [ECharts Docs](https://echarts.apache.org/en/index.html) |
| **FusionCharts** | Business Charts | [FusionCharts Docs](https://www.fusioncharts.com/dev/) |
| **PrimeNG** | UI Components | [PrimeNG Docs](https://primeng.org/) |
| **Userpilot** | User Onboarding | [Userpilot Docs](https://userpilot.com/docs/) |
| **Socket.io** | Real-time Communication | [Socket.io Docs](https://socket.io/docs/) |

---

## 🆘 Troubleshooting

### Common Issues

**Memory Issues During Build**
```bash
# Scripts already use --max_old_space_size=8192
# If still failing, increase in package.json scripts
```

**Keycloak Connection Issues**
- Check network connectivity to Keycloak server
- Verify realm and client configuration
- Check browser console for CORS issues

**AG Grid License Warning**
- License key is set in `src/main.ts`
- Ensure license is valid and not expired

---

## 📞 Support

For questions or issues, contact the development team or refer to internal documentation.

---

*Last Updated: February 2026*
