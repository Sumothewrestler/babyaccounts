# admin.py
from django.contrib import admin
from .models import Accounting, Business, Ledger, Mode, Head, Type
from .forms import AccountingForm

@admin.register(Accounting)
class AccountingAdmin(admin.ModelAdmin):
    list_display = ('date', 'business', 'type', 'ledger', 'cr', 'dr', 'gst', 'mode', 'description')
    search_fields = ('business__name', 'ledger__name', 'description')
    list_filter = ('gst', 'mode')

admin.site.register(Business)
admin.site.register(Ledger)
admin.site.register(Head)
admin.site.register(Mode)
admin.site.register(Type)