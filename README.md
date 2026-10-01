# Backend Automation Framework

A professional backend test automation framework built with **Python, Pytest, Requests, FastAPI, PostgreSQL, SQLAlchemy, Docker, and Allure**.

The project demonstrates API automation, database validation, end-to-end testing, negative testing, test data generation, reusable framework components, test isolation, reporting, and CI/CD integration.

---

## 🚀 Project Overview

This project simulates a backend order management system and provides automated validation across multiple layers:

* REST API testing
* Database validation
* End-to-end API + DB flows
* Positive and negative testing
* Test data generation with Faker
* Reusable API client architecture
* Database client abstraction
* Automatic test cleanup
* Allure reporting
* Dockerized PostgreSQL
* GitHub Actions CI/CD
* GitHub Pages test reporting

The framework is designed with maintainability and scalability in mind, following common automation framework practices used in professional QA environments.

---

## 🛠️ Tech Stack

| Technology           | Purpose                      |
| -------------------- | ---------------------------- |
| Python               | Test automation language     |
| Pytest               | Test framework               |
| Requests             | REST API automation          |
| FastAPI              | Application under test       |
| PostgreSQL           | Relational database          |
| SQLAlchemy           | ORM / database integration   |
| Psycopg2             | Direct PostgreSQL validation |
| Docker               | Database environment         |
| Faker                | Dynamic test data generation |
| Allure               | Test reporting               |
| GitHub Actions       | CI/CD                        |
| pytest-xdist         | Parallel test execution      |
| pytest-rerunfailures | Test retry support           |

---

## 🏗️ Architecture

The framework separates test logic from reusable infrastructure components.

```text
Tests
 │
 ├── API Tests
 ├── DB Tests
 ├── E2E Tests
 ├── Negative Tests
 └── Smoke Tests
       │
       ▼
   API Clients
       │
       ▼
   Base Client
       │
       ▼
     REST API
       │
       ▼
   FastAPI Application
       │
       ▼
   PostgreSQL Database
```

Database validation is performed independently through a dedicated database client.

---

## 📁 Project Structure

```text
Backend Automation/
│
├── .github/
│   └── workflows/
│       └── backend-automation.yml
│
├── clients/
│   └── order_client.py
│
├── config/
│   └── settings.py
│
├── core/
│   ├── api/
│   │   └── base_client.py
│   ├── database/
│   │   └── db_client.py
│   ├── exceptions/
│   │   └── api_exception.py
│   └── logging/
│       └── logger.py
│
├── data/
│   └── factories/
│       └── order_factory.py
│
├── docker/
│   └── docker-compose.yml
│
├── fixtures/
│   ├── api_fixtures.py
│   ├── cleanup_fixtures.py
│   └── db_fixtures.py
│
├── repositories/
│   └── order_repository.py
│
├── services/
│
├── tests/
│   ├── api/
│   ├── db/
│   ├── e2e/
│   ├── negative/
│   └── smoke/
│
├── validators/
│
├── utils/
│
├── app.py
├── conftest.py
├── database.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧪 Test Coverage

The test suite covers multiple testing layers.

### API Tests

Validate REST API behavior including:

* Health endpoint
* Order creation
* Order retrieval
* Customer endpoint behavior
* Request validation

### Database Tests

Validate that API operations are correctly persisted in PostgreSQL.

Examples:

* Verify order persistence
* Validate stored product and quantity
* Validate database client behavior

### End-to-End Tests

Validate complete business flows across API and database layers.

Example:

```text
Create Order
     ↓
API Response Validation
     ↓
Database Validation
     ↓
Update Order Status
     ↓
Database Validation
```

### Negative Tests

Validate API behavior for invalid input and validation scenarios.

Examples:

* Invalid order payload
* Empty product value

### Smoke Tests

Provide fast validation that the application is available and operational.

---

## 🏷️ Pytest Markers

Tests are organized using Pytest markers:

```text
smoke
api
db
e2e
negative
regression
```

Examples:

Run only smoke tests:

```powershell
pytest -m smoke
```

Run API tests:

```powershell
pytest -m api
```

Run database tests:

```powershell
pytest -m db
```

Run end-to-end tests:

```powershell
pytest -m e2e
```

Run negative tests:

```powershell
pytest -m negative
```

Run the regression suite:

```powershell
pytest -m regression
```

---

# ▶️ Running the Project Locally

## 1. Activate the virtual environment

From the project root:

```powershell
.venv\Scripts\Activate.ps1
```

---

## 2. Start PostgreSQL with Docker

The project uses PostgreSQL running inside Docker.

From the project root:

```powershell
docker compose -f docker\docker-compose.yml up -d
```

Verify that the database container is running:

```powershell
docker ps
```

The PostgreSQL container should appear as:

```text
backend-automation-db
```

The database is exposed on:

```text
localhost:5432
```

---

## 3. Start the FastAPI application

Open a **second PowerShell terminal**.

Activate the virtual environment again:

```powershell
.venv\Scripts\Activate.ps1
```

Start the application:

```powershell
uvicorn app:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

Health endpoint:

```text
http://localhost:8000/health
```

FastAPI Swagger documentation:

```text
http://localhost:8000/docs
```

---

## 4. Run the automated tests

Keep the FastAPI server running.

Open a **third PowerShell terminal** and activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

Run the complete test suite:

```powershell
pytest -v
```

The tests will:

1. Send requests to the FastAPI application
2. Validate API responses
3. Validate data directly in PostgreSQL
4. Execute end-to-end flows
5. Generate Allure results
6. Automatically clean up test orders

---

# 📊 Allure Reporting

The project uses Allure for detailed test reporting.

Test results are automatically generated under:

```text
reports/allure-results
```

To open the Allure report locally:

```powershell
allure serve reports\allure-results
```

This starts a local Allure server and opens the report in the browser.

The report includes:

* Test status
* Test duration
* Severity
* Feature
* Story
* Test descriptions
* Pytest markers
* Steps
* Attachments

---

## 🧹 Test Isolation and Cleanup

The framework uses Pytest fixtures to maintain test isolation.

After each test, created orders are automatically removed from the database.

This prevents test data from accumulating between test runs and allows the suite to be executed repeatedly against the same database.

---

# 🐳 Docker

PostgreSQL is provided through Docker Compose.

Start the database:

```powershell
docker compose -f docker\docker-compose.yml up -d
```

Stop the database:

```powershell
docker compose -f docker\docker-compose.yml down
```

Check running containers:

```powershell
docker ps
```

---

# ⚙️ Configuration

Environment-specific configuration is handled through environment variables.

Example:

```text
ENVIRONMENT=qa
BASE_URL=http://localhost:8000
TIMEOUT=30

DB_HOST=localhost
DB_PORT=5432
DB_NAME=ecommerce
DB_USER=admin
DB_PASSWORD=admin
```

Sensitive environment configuration is stored in `.env` and excluded from Git through `.gitignore`.

---

# 🔄 CI/CD

The project includes a GitHub Actions pipeline that automatically runs on:

* Push to `main`
* Pull requests to `main`

The pipeline performs the following:

```text
Checkout Code
      ↓
Setup Python
      ↓
Setup Node.js
      ↓
Install Dependencies
      ↓
Start PostgreSQL
      ↓
Start FastAPI
      ↓
Run Pytest
      ↓
Generate Allure Report
      ↓
Upload Test Results
      ↓
Publish Allure Report
```

The CI environment uses PostgreSQL as a GitHub Actions service container.

---

# 📈 Continuous Test Reporting

Allure HTML reports generated by CI are published through **GitHub Pages**.

This allows the test results to be reviewed independently of the local development environment.

The project also stores:

* Allure test results as CI artifacts
* Generated Allure HTML report as a CI artifact

---

# 🧩 Framework Design

The framework demonstrates several reusable automation patterns.

### Base API Client

A reusable `BaseClient` handles:

* HTTP methods
* Base URL configuration
* Request timeout
* HTTP session management
* Logging
* API exception handling

### API Client Layer

Endpoint-specific clients encapsulate API operations.

Example:

```text
OrderClient
 ├── create_order()
 ├── get_order()
 ├── update_order()
 └── delete_order()
```

This keeps endpoint details out of individual tests.

### Database Client

The `DBClient` provides direct PostgreSQL access for backend validation.

Tests can validate that API operations are correctly reflected in the database.

### Test Data Factory

Faker is used to generate dynamic test data and reduce hard-coded test values.

### Fixtures

Reusable Pytest fixtures provide:

* API clients
* Database connections
* Automatic cleanup
* Shared test setup

---

# 🔍 Example End-to-End Validation

A typical order lifecycle test validates the complete flow:

```text
POST /orders
      ↓
Validate HTTP response
      ↓
Retrieve order from PostgreSQL
      ↓
Validate persisted data
      ↓
PUT /orders/{id}
      ↓
Validate updated API response
      ↓
Validate updated database status
      ↓
Automatic cleanup
```

This approach validates not only the API contract but also the integrity of the data persisted in the backend.

---

# 🎯 Quality Engineering Practices Demonstrated

This project demonstrates practical QA Automation and Quality Engineering practices including:

* API automation
* Backend validation
* Database testing
* End-to-end testing
* Negative testing
* Smoke and regression suites
* Dynamic test data
* Reusable automation components
* Test isolation
* Configuration management
* Logging
* Exception handling
* Docker-based test environments
* Allure reporting
* CI/CD automation
* Automated test reporting

---

# 🚀 Future Enhancements

Potential future improvements include:

* Docker Compose environment for the complete application stack
* Additional API endpoints and business scenarios
* Expanded schema validation
* Authentication and authorization testing
* Contract testing
* Parallel execution in CI
* Additional database repositories
* API performance testing
* Enhanced Allure attachments and request/response evidence

---

## 👩‍💻 Author

**Liat Karavani**

QA Automation Engineer with extensive experience in:

* Manual QA
* API Testing
* Web Testing
* Automation
* Python
* Playwright
* Selenium
* Backend Testing
* Database Validation
* CI/CD

GitHub:

https://github.com/liat159

---

## 📌 Quick Start

For a quick local run:

### Terminal 1 — PostgreSQL

```powershell
docker compose -f docker\docker-compose.yml up -d
```

### Terminal 2 — FastAPI

```powershell
.venv\Scripts\Activate.ps1
uvicorn app:app --reload
```

### Terminal 3 — Tests

```powershell
.venv\Scripts\Activate.ps1
pytest -v
```

### Allure Report

```powershell
allure serve reports\allure-results
```

> **Important:** Do not run `python -m http.server 8000` while the FastAPI application is running, because FastAPI uses port `8000`.
