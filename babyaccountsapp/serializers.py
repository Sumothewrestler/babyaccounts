# serializers.py
from rest_framework import serializers
from .models import Accounting, Business, Mode, Ledger, Head, Type

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['id', 'name']  # Include the fields you want to return
    
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name'] 

class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mode
        fields = ['id', 'name']

class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ['id', 'name']

class HeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Head
        fields = ['id', 'name']

class AccountingSerializer(serializers.ModelSerializer):
    business = serializers.PrimaryKeyRelatedField(queryset=Business.objects.all())  # Use ID for posting
    ledger = serializers.PrimaryKeyRelatedField(queryset=Ledger.objects.all())  # Use ID for posting
    head = serializers.PrimaryKeyRelatedField(queryset=Head.objects.all())           # Use ID for posting
    mode = serializers.PrimaryKeyRelatedField(queryset=Mode.objects.all())          # Use ID for posting

    class Meta:
        model = Accounting
        fields = '__all__'  # Include all fields for posting

    def to_representation(self, instance):
        """Customize the representation for reading."""
        representation = super().to_representation(instance)
        representation['business'] = BusinessSerializer(instance.business).data  # Return full object for reading
        representation['ledger'] = LedgerSerializer(instance.ledger).data      # Return full object for reading
        representation['head'] = HeadSerializer(instance.head).data             # Return full object for reading
        representation['mode'] = ModeSerializer(instance.mode).data                # Return full object for reading
        return representation
    