# Frontend Coding Standards

## Component Structure & Size

### Component Size Limits

-   **Components**: Keep components under **300 lines**. Extract into
    child components if exceeded.
-   **Templates**: Keep templates under **200 lines**. Use `templateUrl`
    for larger templates.
-   **Methods**: Keep component methods under **30 lines**.
-   **Services**: Limit services to **400 lines**. Split into multiple
    focused services.

### Good Component Structure

``` text
user-profile/
├── user-profile.component.ts (< 300 lines)
├── user-profile.component.html (< 200 lines)
├── user-profile.component.scss
└── user-profile.component.spec.ts
```

------------------------------------------------------------------------

## Naming Conventions

### Files & Classes

  ------------------------------------------------------------------------
  Type          File Name                         Class Name
  ------------- --------------------------------- ------------------------
  Component     user-profile.component.ts         UserProfileComponent

  Service       user-data.service.ts              UserDataService

  Pipe          currency-format.pipe.ts           CurrencyFormatPipe

  Guard         auth.guard.ts                     AuthGuard

  Interceptor   http-error.interceptor.ts         HttpErrorInterceptor
  ------------------------------------------------------------------------

------------------------------------------------------------------------

## Variables & Properties

### Descriptive Naming

``` ts
currentUser: User;
isLoadingUserData: boolean;
userPermissions: Permission[];
```

### Observable Naming (`$` suffix)

``` ts
user$: Observable<User>;
loadingState$: Observable<boolean>;
```

### Boolean Naming (is/has/can/should)

``` ts
isLoggedIn: boolean;
hasPermissions: boolean;
canEditProfile: boolean;
shouldShowNotification: boolean;
```

### Avoid Abbreviations

``` ts
usr: User; // ❌ Bad
u: User;   // ❌ Bad
currentUser: User; // ✅ Good
```

------------------------------------------------------------------------

## Methods

### Action Methods (Verb + Noun)

``` ts
getUserById(id: string): Observable<User>
updateUserProfile(profile: UserProfile): void
validateEmailFormat(email: string): boolean
deleteUserAccount(): void
```

### Event Handlers (`on + Event`)

``` ts
onUserClick(): void
onFormSubmit(): void
onDataLoad(): void
```

### Private Methods (Optional `_` prefix)

``` ts
private _validateInput(data: any): boolean
private _handleError(error: Error): void
```

------------------------------------------------------------------------

## TypeScript Best Practices

### Strong Typing

``` ts
interface User {
  readonly id: string;
  name: string;
  email: string;
  createdAt: Date;
  roles: UserRole[];
}
```

### Enums for Constants

``` ts
enum UserRole {
  ADMIN = 'admin',
  USER = 'user',
  MODERATOR = 'moderator'
}
```

### Union Types

``` ts
type LoadingState = 'idle' | 'loading' | 'success' | 'error';
```

### Avoid `any`

``` ts
const userData: any = response; // ❌ Bad
const userData: User = response; // ✅ Good
```

------------------------------------------------------------------------

## Component Structure Example

``` ts
@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.scss']
})
export class UserProfileComponent implements OnInit, OnDestroy {

  @Input() user!: User;
  @Input() readonly: boolean = false;
  @Output() userUpdated = new EventEmitter<User>();

  displayName: string = '';
  isEditing: boolean = false;

  private destroy$ = new Subject<void>();
}
```

------------------------------------------------------------------------

## Service Best Practices

### Always Return Observables

``` ts
@Injectable({ providedIn: 'root' })
export class UserDataService {

  private readonly apiUrl = 'api/users';

  constructor(
    private http: HttpClient,
    private logger: LoggerService
  ) {}

  getUser(id: string): Observable<User> {
    return this.http.get<User>(`${this.apiUrl}/${id}`).pipe(
      catchError(this.handleError.bind(this))
    );
  }

  private handleError(error: HttpErrorResponse): Observable<never> {
    this.logger.error('API Error:', error);
    return throwError(() => error);
  }
}
```

------------------------------------------------------------------------

## Template Best Practices

### Use Async Pipe

``` html
<div *ngIf="user$ | async as user">
  <h1>{{ user.name }}</h1>
</div>
```

### Use `trackBy`

``` html
<div *ngFor="let user of users; trackBy: trackByUserId">
  {{ user.name }}
</div>
```

------------------------------------------------------------------------

## Performance Guidelines

### Use OnPush

``` ts
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush
})
```

### Lazy Loading

``` ts
const routes: Routes = [
  {
    path: 'users',
    loadChildren: () =>
      import('./user/user.module').then(m => m.UserModule)
  }
];
```

------------------------------------------------------------------------

## Storybook Standards

-   Every component must have a `.stories.ts` file.
-   Minimum **3 stories**: Default, variant, edge case.
-   Interactive controls for all `@Input()` properties.
-   Realistic mock data.
-   Documentation in story descriptions.

------------------------------------------------------------------------

## Formatting Standards

-   Prettier
-   2 spaces indentation
-   Single quotes
-   Trailing commas
-   Semicolons required
