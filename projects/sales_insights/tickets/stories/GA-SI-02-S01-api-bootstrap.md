# Story GA-SI-02-S01: New `sales-insights-api` Project Bootstrap & Cloud SQL Config

**Epic:** GA-SI-EPIC-02 — Sales Insights API — Multi-Region Aggregation Service  
**Story ID:** GA-SI-02-S01  
**Priority:** P0  
**Estimate:** 1 day  
**Status:** Draft

---

## Story

**As a** developer,  
**I want** a new `sales-insights-api` Spring Boot project initialized with Cloud SQL connectivity, Keycloak JWT security, and OpenAPI documentation,  
**so that** the team has a runnable, deployable skeleton ready for feature development.

---

## Acceptance Criteria

1. New Maven project `sales-insights-api` created at repo root `i2o-retail/sales-insights-api`
2. Spring Boot version 3.1.7, Java 17 (aligned with `i2o-scheduler`)
3. Cloud SQL socket factory configured: `spring.datasource.url` using `jdbc:postgresql://google/{db}?cloudSqlInstance={project}:{region}:{instance}&socketFactory=com.google.cloud.sql.postgres.SocketFactory`
4. Keycloak JWT security configured: all routes under `/api/v1/sales-insights/**` require a valid Keycloak bearer token; `OPTIONS` preflight and `/actuator/health` excluded
5. Swagger UI accessible at `/swagger-ui/index.html` with `springdoc-openapi-starter-webmvc-ui`
6. `application-local.properties` allows running against a local PostgreSQL Docker container
7. `Dockerfile` created: `FROM eclipse-temurin:17-jre-slim` packaging the JAR
8. Project compiles and `mvn test` passes with no failures
9. `GET /actuator/health` returns `{"status":"UP"}` when running locally

---

## Tasks / Subtasks

- [ ] Initialize Maven project with Spring Initializr or manual `pom.xml` (AC: 1, 2)
  - [ ] Dependencies: `spring-boot-starter-web`, `spring-boot-starter-data-jpa`, `spring-boot-starter-security`, `spring-boot-starter-actuator`, `spring-boot-starter-oauth2-resource-server`, `postgresql`, `cloud-sql-connector-jdbc-postgresql`, `flyway-core`, `springdoc-openapi-starter-webmvc-ui`, `lombok`
- [ ] Configure Cloud SQL datasource (AC: 3, 6)
  - [ ] `application-dev.properties`: Cloud SQL socket factory config
  - [ ] `application-local.properties`: `jdbc:postgresql://localhost:5432/salesinsights`
- [ ] Configure Spring Security JWT (AC: 4)
  - [ ] `SecurityConfig.java`: `http.oauth2ResourceServer(oauth2 -> oauth2.jwt(...))` 
  - [ ] `spring.security.oauth2.resourceserver.jwt.issuer-uri=https://{keycloak}/realms/i2o`
  - [ ] Permit `/actuator/health`, `OPTIONS` requests; require auth for all else
- [ ] Configure Swagger/OpenAPI (AC: 5)
  - [ ] `@OpenAPIDefinition` annotation on main class with title, version, description
  - [ ] `springdoc.swagger-ui.path=/swagger-ui/index.html`
- [ ] Create `Dockerfile` (AC: 7)
- [ ] Write smoke test: `@SpringBootTest(webEnvironment = RANDOM_PORT)` verifies context loads (AC: 8, 9)
- [ ] Add `README.md` with local setup instructions and env variable list

---

## Dev Notes

**New repository:** `i2o-retail/sales-insights-api` — create as new GitHub repo following `i2o-scheduler` as reference model.

**pom.xml key sections (reference `i2o-scheduler/pom.xml`):**
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.1.7</version>
</parent>
<properties>
    <java.version>17</java.version>
</properties>
```

**Cloud SQL dependency:**
```xml
<dependency>
    <groupId>com.google.cloud.sql</groupId>
    <artifactId>postgres-socket-factory</artifactId>
    <version>1.15.2</version>
</dependency>
```

**Dockerfile:**
```dockerfile
FROM eclipse-temurin:17-jre-slim
WORKDIR /app
COPY target/sales-insights-api-*.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

**Environment variables for Cloud Run deployment:**
```
SPRING_PROFILES_ACTIVE=dev
SPRING_DATASOURCE_PASSWORD=<from Secret Manager>
KEYCLOAK_ISSUER_URI=https://keycloak.internal/realms/i2o
```

**Main class package:** `com.corecompete.i2o.salesinsights.SalesInsightsApiApplication`

### Testing

- **Location:** `src/test/java/.../SalesInsightsApiApplicationTest.java`
- **Framework:** Spring Boot Test (`@SpringBootTest`)
- **Test config:** `application-test.properties` using H2 in-memory DB (disable Flyway for context load test: `spring.flyway.enabled=false`)
- **Test:** `contextLoads()` test; `actuatorHealth()` test calling `GET /actuator/health`

---

## Change Log

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2026-02-26 | 1.0 | Initial story generation | AI Agent |

---

## Dev Agent Record
*(Populated during implementation)*

### Agent Model Used
_TBD_

### Debug Log References
_None yet_

### Completion Notes List
_None yet_

### File List
_None yet_

---

## QA Results
*(Populated by QA Agent)*
