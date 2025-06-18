from django.urls import path
from .views import AccountTypeListCreateView


urlpatterns = [
    path('api/v1/type/', AccountTypeListCreateView.as_view(), name='account_type-list-create'),
]
