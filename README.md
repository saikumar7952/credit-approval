Credit Approval Backend

A minimal Django REST API for managing customers, loans, and eligibility checks.
Supports local development with SQLite and production deployment on Render with PostgreSQL.

🚀 Features

Register customers (/register/)

Check loan eligibility (/check-eligibility/)

Create loan (/create-loan/)

View a single loan (/view-loan/<loan_id>/)

View all loans of a customer (/view-loans/<customer_id>/)

Seed test data with python manage.py seed_data

🖥️ Local Development (SQLite)

Clone repo

Create venv

Install requirements

Create .env

Run migrations

Seed data (optional)

Start server

👉 See detailed steps above.

☁️ Deploy on Render (Free Tier)

Push to GitHub

Create Web Service on Render

Add PostgreSQL

Add Environment Variables

Deploy

Seed DB on Render

👉 See detailed steps above.

🔗 Example API Calls & Responses
1. Register Customer

Request

POST /register/
{
  "first_name": "Sai",
  "last_name": "Kumar",
  "age": 30,
  "monthly_income": 25000,
  "phone_number": "9999999999"
}


Response

{
  "id": 1,
  "first_name": "Sai",
  "last_name": "Kumar",
  "age": 30,
  "monthly_income": "25000.00",
  "phone_number": "9999999999",
  "approved_limit": 900000,
  "current_debt": "0.00"
}

2. Check Eligibility

Request

POST /check-eligibility/
{
  "customer_id": 1,
  "loan_amount": 100000,
  "interest_rate": 10,
  "tenure": 24
}


Response

{
  "customer_id": 1,
  "approval": true,
  "interest_rate": 10.0,
  "corrected_interest_rate": 10.0,
  "monthly_installment": 4614.48
}

3. Create Loan

Request

POST /create-loan/
{
  "customer_id": 1,
  "loan_amount": 100000,
  "interest_rate": 10,
  "tenure": 24
}


Response

{
  "id": 1,
  "customer": 1,
  "loan_amount": "100000.00",
  "tenure": 24,
  "interest_rate": "10.00",
  "monthly_repayment": "4614.48",
  "emis_paid_on_time": 0,
  "start_date": null,
  "end_date": null,
  "is_active": true
}

4. View Loan

Request

GET /view-loan/1/


Response

{
  "id": 1,
  "customer": 1,
  "loan_amount": "100000.00",
  "tenure": 24,
  "interest_rate": "10.00",
  "monthly_repayment": "4614.48",
  "emis_paid_on_time": 0,
  "start_date": null,
  "end_date": null,
  "is_active": true
}

5. View All Loans of a Customer

Request

GET /view-loans/1/


Response

[
  {
    "id": 1,
    "customer": 1,
    "loan_amount": "100000.00",
    "tenure": 24,
    "interest_rate": "10.00",
    "monthly_repayment": "4614.48",
    "emis_paid_on_time": 0,
    "start_date": null,
    "end_date": null,
    "is_active": true
  }
]

📂 Project Structure
credit-approval-backend/
├─ manage.py
├─ requirements.txt
├─ Procfile
├─ runtime.txt
├─ README.md
├─ .gitignore
├─ credit_system/
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ customers/
│  ├─ models.py
│  ├─ views.py
│  ├─ urls.py
│  └─ management/commands/seed_data.py
├─ loans/
   ├─ models.py
   ├─ views.py
   ├─ urls.py