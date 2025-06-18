from django.urls import path
from .views import AccountTypeListCreateView, AccountTypeRetrieveUpdateDestroy


urlpatterns = [
    path('api/v1/type/', AccountTypeListCreateView.as_view(), name='account_type-list-create'),
    path('api/v1/type/<int:id>', AccountTypeRetrieveUpdateDestroy.as_view(), name='account_type-retrieve-update-destroy'),
]
