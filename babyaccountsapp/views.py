# views.py
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Accounting, Business, Mode, Ledger, Head, Type
from .serializers import AccountingSerializer, BusinessSerializer, ModeSerializer, LedgerSerializer, HeadSerializer, TypeSerializer
from .forms import AccountingForm, BusinessForm, ModeForm

class AccountingViewSet(viewsets.ModelViewSet):
    queryset = Accounting.objects.all()
    serializer_class = AccountingSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class ModeViewSet(viewsets.ModelViewSet):
    queryset = Mode.objects.all()
    serializer_class = ModeSerializer

class LedgerViewSet(viewsets.ModelViewSet):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer

class HeadViewSet(viewsets.ModelViewSet):
    queryset = Head.objects.all()
    serializer_class = HeadSerializer