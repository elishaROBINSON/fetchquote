
from rest_framework import serializers
from fetchcrypto.models import CurrentCryptoPrice

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentCryptoPrice
        fields = ["updated_at", "current_price", "pair_name"]