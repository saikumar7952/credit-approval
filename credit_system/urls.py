from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Credit Approval API is running"})

urlpatterns = [
    path("", home),
    path("", include("customers.urls")),
    path("", include("loans.urls")),
]
