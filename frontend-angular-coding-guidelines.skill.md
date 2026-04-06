---
source: /Users/sandeepofficial/Downloads/frontend-angular-coding-guidelines.pdf
total_pages: 13
extracted_at: 2026-03-17T05:02:37.639667+00:00
from_cache: false
images_dir: images
---

## Frontend Coding Standards

## Component Structure & Size

Component Size Limits

- Components: Keep components under 300 lines. Extract into child components if exceed

- Templates: Keep templates under 200 lines. Use templateUrl for larger templates

- Methods: Keep component methods under 30 lines

- Services: Limit services to 400 lines. Split into multiple focused services

## File Organization

```ts
// ✅ Good component structure
user-profile/
├── user-profile.component.ts      (< 300 lines)
├── user-profile.component.html    (< 200 lines)
├── user-profile.component.scss
└── user-profile.component.spec.ts
```

## Naming Conventions

## Files & Classes

- Components: user-profile.component.ts  → UserProfileComponent

- Services: user-data.service.ts  → UserDataService

- Pipes: currency-format.pipe.ts  → CurrencyFormatPipe

- Guards: auth.guard.ts  → AuthGuard

Interceptors: http-error.interceptor.ts  → HttpErrorInterceptor

## Variables & Properties

```ts
// ✅ Descriptive naming
currentUser: User;
isLoadingUserData: boolean;
userPermissions: Permission[];
```
```ts
// ✅ Observable naming with $ suffix
user$: Observable<User>;
loadingState$: Observable<boolean>;
```
```ts
// ✅ Boolean properties with is/has/can/should
isLoggedIn: boolean;
hasPermissions: boolean;
canEditProfile: boolean;
shouldShowNotification: boolean;
```
```ts
// ❌ Avoid abbreviations
usr: User;           // Bad
u: User;            // Bad
currentUser: User;   // Good
```

## Methods

```ts
// ✅ Action methods - verb + noun
getUserById(id: string): Observable<User>
updateUserProfile(profile: UserProfile): void
validateEmailFormat(email: string): boolean
deleteUserAccount(): void
```
7 // ✅ Event handlers - on + Event
8 onUserClick(): void
9 onFormSubmit(): void
10 onDataLoad(): void
```ts
// ✅ Private methods with underscore prefix (optional)
private _validateInput(data: any): boolean
private _handleError(error: Error): void
```

## TypeScript Best Practices

## Type Safety

```ts
// ✅ Strong typing
interface User {
readonly id: string;
name: string;
email: string;
createdAt: Date;
roles: UserRole[];
}
```
```ts
// ✅ Use enums for constants
enum UserRole {
ADMIN = 'admin',
USER = 'user',
MODERATOR = 'moderator'
}
```
```ts
// ✅ Union types for state
type LoadingState = 'idle' | 'loading' | 'success' | 'error';
```
```ts
// ❌ Avoid 'any' type
const userData: any = response; // Bad
const userData: User = response; // Good
```

## Component Properties

```ts
@Component({
selector: 'app-user-profile',
templateUrl: './user-profile.component.html',
styleUrls: ['./user-profile.component.scss']
})
export class UserProfileComponent implements OnInit, OnDestroy {
// ✅ Input/Output with proper types
@Input() user!: User;
@Input() readonly: boolean = false;
@Output() userUpdated = new EventEmitter<User>();
```
```ts
// ✅ Public properties first
displayName: string = '';
isEditing: boolean = false;
```

```ts
// ✅ Private properties last
private destroy$ = new Subject<void>();
```

18 }

## Component Architecture

## Single Responsibility

```ts
// ✅ Good: Single purpose component
@Component({
selector: 'app-user-avatar',
template: `
<img [src]="user.avatarUrl"
[alt]="user.name"
class="avatar">
`
})
export class UserAvatarComponent {
@Input() user!: User;
@Input() size: 'small' | 'medium' | 'large' = 'medium';
}
```
```ts
// ❌ Bad: Multiple responsibilities
@Component({
selector: 'app-user-dashboard-with-notifications-and-settings'
// Too many concerns in one component
})
```

## Lifecycle Methods Order

```ts
export class UserComponent implements OnInit, OnDestroy {
// 1. Properties
user: User | null = null;
```
```ts
// 2. Constructor
constructor(private userService: UserService) {}
```
```ts
// 3. Lifecycle hooks in order
ngOnInit(): void {
this.loadUser();
}
```
```ts
ngOnDestroy(): void {
this.destroy$.next();
this.destroy$.complete();
}
```
```ts
// 4. Public methods
loadUser(): void {
// Implementation
}
```
```ts
// 5. Private methods
private handleError(error: any): void {
// Implementation
}
}
```

## Service Best Practices

Service Structure

```ts
@Injectable({ providedIn: 'root' })
export class UserDataService {
private readonly apiUrl = 'api/users';
```
```ts
constructor(
private http: HttpClient,
private logger: LoggerService
) {}
```
```ts
// ✅ Always return observables from service methods
getUser(id: string): Observable<User> {
return this.http.get<User>(`${this.apiUrl}/${id}`).pipe(
catchError(this.handleError.bind(this))
);
}
```
```ts
updateUser(user: User): Observable<User> {
return this.http.put<User>(`${this.apiUrl}/${user.id}`, user);
}
```
```ts
// ✅ Use observables for multiple operations
getUserWithPermissions(id: string): Observable<UserWithPermissions> {
return forkJoin({
user: this.getUser(id),
permissions: this.getPermissions(id)
}).pipe(
map(({ user, permissions }) => ({ user, permissions }))
);
}
```
```ts
private handleError(error: HttpErrorResponse): Observable<never> {
this.logger.error('API Error:', error);
return throwError(() => error);
}
}
```
```ts
// ❌ NEVER use async/await or Promises in services
class BadUserService {
async getUser(id: string): Promise<User> {  // Bad
const response = await this.http.get<User>('/api/user').toPromise();
return response;
}
}
Error Handling with Observables Only
// ✅ Handle errors in observable streams
getUserData(): void {
this.user$ = this.userService.getUser(this.userId).pipe(
startWith(null), // Initial value
catchError(error => {
this.logger.error('Failed to load user', error);
this.notificationService.showError('Unable to load user data');
return of(null); // Return fallback value
}),
finalize(() => {
// Cleanup logic
this.isLoading = false;
}),
takeUntil(this.destroy$)
```

## Error Handling with Observables Only

```ts
);
}
```
```ts
// ✅ Template subscription with async pipe
// <div *ngIf="user$ | async as user; else loadingTemplate">
//   {{ user.name }}
// </div>
```
```ts
// ❌ NEVER use try/catch with async/await
async badGetUserData(): Promise<void> {  // ❌ Forbidden
try {
this.user = await this.userService.getUser(this.userId).toPromise();
} catch (error) {
this.handleError(error);
}
}
```

## Template Best Practices

## Template Size & Structure

```ts
<!-- ✅ Keep templates under 200 lines -->
<div class="user-profile">
<app-user-header [user]="user"></app-user-header>
```
```ts
<div class="user-content">
<app-user-details
[user]="user"
[readonly]="!canEdit"
(userUpdated)="onUserUpdated($event)">
</app-user-details>
</div>
```
```ts
<app-user-actions
[user]="user"
(delete)="onUserDelete()">
</app-user-actions>
</div>
```

## Data Binding

```ts
<!-- ✅ Use async pipe for observables -->
<div *ngIf="user$ | async as user">
<h1>{{ user.name }}</h1>
</div>
```
```ts
<!-- ✅ Use trackBy for ngFor -->
<div *ngFor="let user of users; trackBy: trackByUserId">
{{ user.name }}
</div>
```
```ts
<!-- ✅ Safe navigation operator -->
<span>{{ user?.profile?.displayName }}</span>
```

## Reactive Programming Rules

## Observable-Only Pattern

```ts
// ✅ ALWAYS use Observables - NEVER use Promises or async/await
export class UserComponent implements OnInit, OnDestroy {
```

```ts
user$: Observable<User>;
loading$: Observable<boolean>;
error$: Observable<string | null>;
```
7 private destroy$ = new Subject<void>();
```ts
ngOnInit(): void {
// ✅ Observable chain
this.user$ = this.route.params.pipe(
switchMap(params => this.userService.getUser(params['id'])),
shareReplay(1),
takeUntil(this.destroy$)
);
```
```ts
// ✅ Subscribe in template with async pipe
// <div *ngIf="user$ | async as user">{{ user.name }}</div>
}
}
```
```ts
// ❌ FORBIDDEN: async/await, Promises, toPromise()
export class BadUserComponent {
async ngOnInit(): Promise<void> {  // ❌ Never do this
try {
const user = await this.userService.getUser(this.userId).toPromise();
this.user = user;
} catch (error) {
this.error = error;
}
}
```
```ts
async loadData(): Promise<User[]> {  // ❌ Never do this
return await this.http.get<User[]>('/api/users').toPromise();
}
}
Service Observable Patterns
@Injectable({ providedIn: 'root' })
export class UserDataService {
private usersSubject = new BehaviorSubject<User[]>([]);
users$ = this.usersSubject.asObservable();
```
```ts
// ✅ All methods return Observables
getUsers(): Observable<User[]> {
return this.http.get<User[]>('/api/users').pipe(
tap(users => this.usersSubject.next(users)),
catchError(this.handleError)
);
}
```
```ts
createUser(user: User): Observable<User> {
return this.http.post<User>('/api/users', user).pipe(
tap(newUser => {
const currentUsers = this.usersSubject.value;
this.usersSubject.next([...currentUsers, newUser]);
}),
catchError(this.handleError)
);
}
```
```ts
// ✅ Complex operations with observables
getUsersWithStats(): Observable<UserWithStats[]> {
return forkJoin({
users: this.getUsers(),
stats: this.getStats()
```

## Service Observable Patterns

```ts
}).pipe(
map(({ users, stats }) =>
users.map(user => ({
...user,
stats: stats.find(s => s.userId === user.id)
}))
)
);
}
```
```ts
private handleError = (error: HttpErrorResponse): Observable<never> => {
return throwError(() => new Error(`API Error: ${error.message}`));
};
}
```

## Memory Management

```ts
export class UserComponent implements OnInit, OnDestroy {
private destroy$ = new Subject<void>();
```
```ts
ngOnInit(): void {
// ✅ Always unsubscribe
this.userService.getUsers().pipe(
takeUntil(this.destroy$)
).subscribe(users => {
this.users = users;
});
}
```
```ts
ngOnDestroy(): void {
this.destroy$.next();
this.destroy$.complete();
}
}
```

## Observable Composition

```ts
// ✅ Combine related observables
ngOnInit(): void {
this.userWithPermissions$ = combineLatest([
this.userService.getCurrentUser(),
this.permissionService.getUserPermissions()
]).pipe(
map(([user, permissions]) => ({ user, permissions })),
takeUntil(this.destroy$)
);
}
```
```ts
// ❌ Do NOT use async/await or Promises
// Use observables and RxJS operators instead
async getUserData(): Promise<User> {  // Bad
return await this.http.get<User>('/api/user').toPromise();
}
```
```ts
// ✅ Use observables
getUserData(): Observable<User> {  // Good
return this.http.get<User>('/api/user');
}
```

## Module Organization

## Feature Module Structure

1 // ✅ Feature module organization
2 @NgModule({
3 declarations: [
4 UserListComponent,
5 UserDetailComponent,
6 UserFormComponent
7 ],
8 imports: [
9 CommonModule,
10 UserRoutingModule,
11 SharedModule
12 ],
13 providers: [
14 UserService,
15 UserResolver
16 ]
17 })
18 export class UserModule {}

## Barrel Exports

```ts
// user/index.ts
export * from './user.component';
export * from './user.service';
export * from './user.model';
```
```ts
// Import usage
import { UserComponent, UserService } from './user';
```

## Performance Guidelines

## Change Detection

```ts
// ✅ Use OnPush when possible
@Component({
selector: 'app-user-card',
changeDetection: ChangeDetectionStrategy.OnPush
})
export class UserCardComponent {
@Input() user!: User;
}
```

## Lazy Loading

```ts
// ✅ Lazy load feature modules
const routes: Routes = [
{
path: 'users',
loadChildren: () => import('./user/user.module').then(m => m.UserModule)
}
];
```

## Storybook Integration

Story Structure

```ts
// user-card.stories.ts
import type { Meta, StoryObj } from '@storybook/angular';
import { UserCardComponent } from './user-card.component';
import { User } from '../models/user.model';
```
```ts
const mockUser: User = {
id: '1',
name: 'John Doe',
email: 'john.doe@example.com',
avatarUrl: 'https://example.com/avatar.jpg',
role: 'user'
};
```
```ts
const meta: Meta<UserCardComponent> = {
title: 'Components/UserCard',
component: UserCardComponent,
parameters: {
layout: 'centered',
},
tags: ['autodocs'],
argTypes: {
size: {
control: { type: 'select' },
options: ['small', 'medium', 'large'],
},
readonly: {
control: { type: 'boolean' },
}
},
};
```
```ts
export default meta;
type Story = StoryObj<UserCardComponent>;
```
```ts
// ✅ Default story
export const Default: Story = {
args: {
user: mockUser,
size: 'medium',
readonly: false
},
};
```
```ts
// ✅ Variant stories
export const Small: Story = {
args: {
user: mockUser,
size: 'small',
},
};
```
```ts
export const Readonly: Story = {
args: {
user: mockUser,
readonly: true,
},
};
```
```ts
export const WithoutAvatar: Story = {
args: {
user: { ...mockUser, avatarUrl: '' },
},
```

63 };

## Component Story Requirements

- Every component must have a corresponding .stories.ts file

- Minimum 3 stories: Default, variant state, edge case

- Interactive controls for all @Input() properties

- Mock data should be realistic and consistent

- Documentation in story descriptions

## Storybook File Naming

```ts
user-card/
├── user-card.component.ts
├── user-card.component.html
├── user-card.component.scss
├── user-card.component.spec.ts
└── user-card.stories.ts          // Required for all components
```

## Story Organization

```ts
// ✅ Group stories by feature
const meta: Meta<UserCardComponent> = {
title: 'Features/User/UserCard',  // Organized hierarchy
component: UserCardComponent,
};
```
```ts
// ✅ Use consistent story naming
export const Default: Story = {};
export const Loading: Story = {};
```

```ts
export const Error: Story = {};
export const Empty: Story = {};
```

## Mock Data Standards

1 // ✅ Create reusable mock data files
2 // mocks/user.mock.ts
3 export const MOCK_USER: User = {
4 id: '1',
5 name: 'John Doe',
6 email: 'john.doe@example.com',
7 role: 'user',
8 createdAt: new Date('2023-01-01'),
9 isActive: true
10 };
12 export const MOCK_ADMIN_USER: User = {
13 ...MOCK_USER,
14 id: '2',
15 role: 'admin',
16 name: 'Jane Admin'
17 };
```ts
// Use in stories
import { MOCK_USER, MOCK_ADMIN_USER } from '../mocks/user.mock';
```

## Testing Standards

Component Testing with Storybook

```ts
describe('UserComponent', () => {
let component: UserComponent;
let fixture: ComponentFixture<UserComponent>;
let userService: jasmine.SpyObj<UserService>;
```
```ts
beforeEach(() => {
const spy = jasmine.createSpyObj('UserService', ['getUser']);
```
```ts
TestBed.configureTestingModule({
declarations: [UserComponent],
providers: [
{ provide: UserService, useValue: spy }
]
});
```
```ts
fixture = TestBed.createComponent(UserComponent);
component = fixture.componentInstance;
userService = TestBed.inject(UserService) as jasmine.SpyObj<UserService>;
});
```
```ts
it('should create', () => {
expect(component).toBeTruthy();
});
```
```ts
it('should load user observable on init', () => {
const mockUser: User = { id: '1', name: 'John Doe' };
userService.getUser.and.returnValue(of(mockUser));
```
```ts
component.userId = '1';
component.ngOnInit();
```
```ts
// ✅ Test observable streams
component.user$.subscribe(user => {
expect(user).toEqual(mockUser);
});
```
```ts
expect(userService.getUser).toHaveBeenCalledWith('1');
});
```
```ts
// ✅ Test error handling in observables
it('should handle user loading errors', () => {
const error = new Error('API Error');
userService.getUser.and.returnValue(throwError(() => error));
```
```ts
component.userId = '1';
component.ngOnInit();
```
```ts
component.user$.subscribe({
next: (user) => expect(user).toBeNull(),
error: fail // Should not reach error handler due to catchError
});
});
}
```
```ts
// ✅ Storybook Visual Testing Integration
describe('UserCard Stories', () => {
it('should match Default story snapshot', () => {
// Test that matches Storybook story
const mockUser = MOCK_USER; // Use same mock as story
component.user = mockUser;
fixture.detectChanges();
```

```ts
expect(fixture).toMatchSnapshot();
});
});
```

## Storybook Coverage Requirements

- 100% component coverage: Every component must have stories

- Visual regression testing: Use Chromatic or similar tools

- Accessibility testing: Enable a11y addon in Storybook

Documentation: Use JSDoc comments that appear in Storybook docs

## Code Quality Rules

## ESLint Configuration

```ts
{
"extends": ["@angular-eslint/recommended"],
"rules": {
"@angular-eslint/component-max-inline-declarations": [
"error",
{ "template": 10, "styles":
}
],
"@angular-eslint/no-input-rename": "error",
"@angular-eslint/no-output-rename": "error",
"@typescript-eslint/no-explicit-any": "error"
}
}
```

## Formatting Standards

Use Prettier for consistent code formatting

- 2 spaces for indentation

- Single quotes for strings

- Trailing commas in objects and arrays

Semicolons at the end of statements

## Documentation Requirements

## Component Documentation

1 /**
2 * Displays user profile information with edit capabilities
3 *
4 * @example
5 * <app-user-profile
6 *   [user]="currentUser"
7 *   [readonly]="!canEdit"
8 *   (userUpdated)="handleUserUpdate($event)">
9 * </app-user-profile>
10 */
11 @Component({
12 selector: 'app-user-profile'
13 })

```ts
export class UserProfileComponent {
/** The user to display */
```

- 16 @Input() user!: User;

```ts
/** Whether the profile is in read-only mode */
@Input() readonly: boolean = false;
```

```ts
/** Emitted when user data is updated */
@Output() userUpdated = new EventEmitter<User>();
}
```

## README for Features

- 1 # User Management Feature

- 3 ## Components
4 - `UserListComponent` - Displays paginated list of users
5 - `UserDetailComponent` - Shows detailed user information
6 - `UserFormComponent` - Form for creating/editing users

- 8 ## Services

- 9 - `UserDataService` - Handles user CRUD operations

- 10 - `UserValidationService` - Validates user input
12 ## Usage
13 Import `UserModule` into your feature module to use user components.

---

## Extracted Images

No images extracted.
