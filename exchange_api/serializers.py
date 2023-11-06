from rest_framework import serializers
from exchange_api.models import CurrencyData

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model=CurrencyData
        fields=('code','value')