from django.urls import path

from .views import (
    CustomerListCreate,
    CustomerUpdateDelete
)

urlpatterns = [
    path('list_create/', CustomerListCreate.as_view(), name="customer-list-create"),
    path('update_delete/<str:customer_pk>/', CustomerUpdateDelete.as_view(), name="customer-update-delete")
]
