from django.core.management.base import BaseCommand
from customers.models import Customer
from loans.models import Loan
from datetime import date, timedelta
from loans.views import compute_emi

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Customer.objects.all().delete()
        Loan.objects.all().delete()

        c1 = Customer.objects.create(
            first_name="Sai",
            last_name="Kumar",
            age=30,
            monthly_income=25000,
            phone_number="9999999999",
            approved_limit=36*25000
        )
        c2 = Customer.objects.create(
            first_name="Anita",
            last_name="Sharma",
            age=28,
            monthly_income=40000,
            phone_number="8888888888",
            approved_limit=36*40000
        )

        emi1 = compute_emi(100000, 10, 24)
        Loan.objects.create(
            customer=c1,
            loan_amount=100000,
            tenure=24,
            interest_rate=10,
            monthly_repayment=emi1,
            emis_paid_on_time=20,
            start_date=date.today(),
            end_date=date.today()+timedelta(days=730)
        )

        emi2 = compute_emi(200000, 12, 36)
        Loan.objects.create(
            customer=c2,
            loan_amount=200000,
            tenure=36,
            interest_rate=12,
            monthly_repayment=emi2,
            emis_paid_on_time=30,
            start_date=date.today(),
            end_date=date.today()+timedelta(days=1095)
        )

        self.stdout.write(self.style.SUCCESS("Seed data created."))
