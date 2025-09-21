from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Loan
from customers.models import Customer
from .serializers import LoanSerializer
import math

def compute_emi(p, r, n):
    r = r/12/100
    if r==0: return p/n
    return p*r*(1+r)**n/((1+r)**n-1)

@api_view(['POST'])
def check_eligibility(request):
    cid = request.data['customer_id']
    amount = float(request.data['loan_amount'])
    rate = float(request.data['interest_rate'])
    tenure = int(request.data['tenure'])
    c = Customer.objects.get(id=cid)
    emi = compute_emi(amount, rate, tenure)
    approval = emi <= 0.5*float(c.monthly_income)
    return Response({
        'customer_id': cid,
        'approval': approval,
        'interest_rate': rate,
        'corrected_interest_rate': rate,
        'monthly_installment': emi
    })

@api_view(['POST'])
def create_loan(request):
    cid = request.data['customer_id']
    amount = float(request.data['loan_amount'])
    rate = float(request.data['interest_rate'])
    tenure = int(request.data['tenure'])
    c = Customer.objects.get(id=cid)
    emi = compute_emi(amount, rate, tenure)
    if emi > 0.5*float(c.monthly_income):
        return Response({'error': 'Not eligible'})
    loan = Loan.objects.create(
        customer=c, loan_amount=amount, tenure=tenure,
        interest_rate=rate, monthly_repayment=emi
    )
    return Response(LoanSerializer(loan).data)

@api_view(['GET'])
def view_loan(request, loan_id):
    loan = Loan.objects.get(id=loan_id)
    return Response(LoanSerializer(loan).data)

@api_view(['GET'])
def view_loans(request, customer_id):
    loans = Loan.objects.filter(customer_id=customer_id)
    return Response(LoanSerializer(loans, many=True).data)
