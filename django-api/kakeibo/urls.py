from django.urls import path
from . import views

urlpatterns = [
    path('transaction/<int:transaction_id>/', views.retrieve_transactions, name='retrieve_transactions'),
]