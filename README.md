https://github.com/user-attachments/assets/779959b5-1bd6-4629-ae12-be92371b1c21


# Task Management System (Django)

A simple, focused task management system for individuals who value time, clarity, and reliability.

This project was built intentionally as a backend-first system. While the domain is simple, the implementation reflects production-aware engineering decisions: clear invariants, explicit constraints, ownership boundaries, and environment-driven configuration. The goal is not to showcase features, but to demonstrate how a small system can be designed and shipped responsibly.

Live application:

* [https://todo.miestudio.live/](https://todo.miestudio.live/)

API and documentation:

* /api
* /api/docs
* /api/redoc

Note: The interactive API documentation requires authentication. Use the standard web login flow at /auth/login/ before exploring protected endpoints.

## What this system is

* A server-rendered web application for managing personal tasks
* A multi-user system with strict data ownership guarantees
* A backend that exposes a documented API suitable for future frontend clients

This is not a demo-only application. It is structured as a small but complete system that can be reasoned about, tested, deployed, and extended.

## Core engineering principles

The following principles guided all implementation decisions:

* Invariants are enforced at the data, view, and API layers
* All state-changing operations require authentication
* A user can only access and mutate their own data
* Configuration is environment-driven, not hardcoded
* Development and production behaviors are intentionally different
* Simplicity is preferred over premature abstraction

## Architecture overview

* Django for server-side rendering and request handling
* Django REST Framework for API exposure
* SQLite for local development
* PostgreSQL support via environment configuration
* Bootstrap 5 for mobile-first, SSR-friendly UI
* drf-spectacular for OpenAPI schema and documentation

The project is organized into clearly scoped Django apps:

* core

  * authentication views
  * shared layout and navigation
  * dashboard
* todos

  * domain model and business logic
  * SSR views and forms
  * API serializers and viewsets

## Development phases and decisions

### Phase 0 - Define scope and constraints

* Explicitly limited the MVP to core task management
* Avoided speculative features and premature scaling
* Chose SSR-first to reduce complexity and improve reliability

### Phase 1 - Project setup and configuration hygiene

* Initialized Django project with clear app boundaries
* Introduced environment variables early for:

  * SECRET_KEY
  * DEBUG
  * ALLOWED_HOSTS
  * database configuration
* Static files and templates configured deliberately from day one

### Phase 2 - Data layer

* Designed a minimal but realistic Todo model
* Enforced ownership through foreign keys
* Used migrations consistently from the start
* Verified admin functionality for operational visibility

### Phase 3 - Authentication

* Implemented server-rendered authentication flows
* Protected all application routes behind login
* Ensured logout is explicit and state-safe
* Reflected authentication state clearly in the UI

### Phase 4 - Server-rendered UI

* Built mobile-first pages using Bootstrap
* Used Django Forms and ModelForms for validation
* Ensured ownership checks in all SSR views
* Treated server-side validation as authoritative

### Phase 5 - Progressive interactivity

* Introduced HTMX selectively to improve UX
* Avoided full page reloads where unnecessary
* Preserved SSR correctness as the primary model

### Phase 6 - API layer

* Exposed Todo resources via Django REST Framework
* Enforced authentication and ownership at the API level
* Filtered querysets by the authenticated user
* Added pagination and ordering defaults

### Phase 7 - OpenAPI and documentation

* Generated schema automatically using drf-spectacular
* Exposed interactive documentation at /api/docs
* Exposed reference documentation at /api/redoc
* Verified that authentication requirements are visible in docs

### Phase 8 - Production readiness

* Added structured logging with environment-based behavior
* Enabled CSRF protection for SSR forms
* Configured secure cookie settings for production
* Introduced a `.env.example` to document required configuration
* Added minimal tests covering authentication and core CRUD paths

### Phase 9 - Database portability

* Added PostgreSQL support without changing application code
* Switched databases entirely via environment variables
* Ensured migrations run cleanly across engines

### Phase 10 - Deployment

* Deployed to Render using a production WSGI server
* Added explicit startup steps:

  * database migrations
  * static file collection
* Performed end-to-end smoke testing post-deploy

## Running the application locally

### Requirements

* Python 3.10 or newer
* Virtual environment tooling

### Setup

* Clone the repository

* Create and activate a virtual environment

* Install dependencies

* Create a `.env` file based on `.env.example`

* Set DEBUG=True

* Use the default SQLite configuration

### Run

* python manage.py migrate
* python manage.py runserver

The application will use SQLite and development logging.

## Running in a production-like environment

This project supports running locally with production settings to validate behavior.

* Set DEBUG=False
* Configure a PostgreSQL DATABASE_URL
* Configure secure cookie and host settings

Then run:

* python manage.py migrate
* python manage.py collectstatic --no-input
* gunicorn config.wsgi

This mirrors the deployment setup used on Render.

## API usage

* All API endpoints require authentication
* Session authentication is supported via the SSR login flow
* Once logged in, the interactive docs at /api/docs can be used

This API is intentionally designed to be stable and frontend-consumable.

## Intended value

This system is designed for users who value:

* clarity over complexity
* correctness over novelty
* tools that respect time and focus

From an engineering perspective, it demonstrates how to take a small problem domain and treat it with production-level discipline.

## Status

* Phases completed: 0 through 10
* Phase 11 intentionally deferred

**Phase 11** focuses on making the backend fully handoff-ready for a frontend developer by freezing the API contract, validating request and response shapes, exporting the OpenAPI specification, and providing concise frontend integration notes covering base URLs, authentication flow, key endpoints, and sample payloads; it was deliberately deferred until after Phase 10 so the data model, behavior, and deployment characteristics were stable, making an API freeze meaningful and executable without refactoring or breaking changes.

The project is considered complete and stable at this stage.
