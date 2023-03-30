from django.urls import path

from .views import financial_literacy_view, insurance_policy_view, transfer_view, loans_view, women_view, feedback_view

app_name = 'transactions'


urlpatterns = [
    path("literacy/", financial_literacy_view, name="literacy"),
    path("insurance/", insurance_policy_view, name="insurance"),
    path("transfer/", transfer_view, name="transfer"),
    path("loans/", loans_view, name="loans"),
    path("women/", women_view, name="women"),
    path("feedback/", feedback_view, name="feedback"),
]
