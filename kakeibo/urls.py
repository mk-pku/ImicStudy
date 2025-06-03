from django.urls import path
from . import views

urlpatterns = [
    path('api/transaction/<int:transaction_id>/', views.get_transaction_by_id_sqlalchemy, name='api_get_transaction_sqlalchemy'),
]