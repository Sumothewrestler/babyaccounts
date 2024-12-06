# forms.py
from django import forms
from .models import Accounting, Business, Mode, Ledger, Head

class AccountingForm(forms.ModelForm):
    class Meta:
        model = Accounting
        fields = ['date', 'business', 'ledger', 'cr', 'dr', 'gst', 'mode', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'cr': forms.NumberInput(attrs={'step': '0.01'}),
            'dr': forms.NumberInput(attrs={'step': '0.01'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name']

class ModeForm(forms.ModelForm):
    class Meta:
        model = Mode
        fields = ['name']

class LedgerForm(forms.ModelForm):
    class Meta:
        model = Ledger
        fields = ['name']  # Only include the fields that exist in the Ledger model

class HeadForm(forms.ModelForm):
    class Meta:
        model = Head
        fields = ['name']  # Include fields for Head