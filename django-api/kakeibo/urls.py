from django.urls import path
from . import views


urlpatterns = [
    path(
        "transactions/",
        views.TransactionListCreateView.as_view(),
        name="transactions_list_create"
    ),
    path(
        "transactions/<int:transaction_id>/",
        views.TransactionDetailView.as_view(),
        name="transaction_detail"
    ),
]