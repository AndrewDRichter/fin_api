from django.shortcuts import render
from rest_framework import generics
from .models import AccountType
from .serializers import AccountTypeSerializer


class AccountTypeListCreateView(generics.ListCreateAPIView):
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer


class AccountTypeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer
    lookup_field = 'id'
