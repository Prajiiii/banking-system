from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView
from django.shortcuts import render

from transactions.models import Transaction

def financial_literacy_view(request):
       return render(request, 'transactions/literacy.html')

def insurance_policy_view(request):
       return render(request, 'transactions/insurance.html')

def transfer_view(request):
       return render(request, 'transactions/transfer.html')

def loans_view(request):
       return render(request, 'transactions/loans.html')

def women_view(request):
       return render(request, 'transactions/women.html')

def feedback_view(request):
       return render(request, 'transactions/feedback.html')
