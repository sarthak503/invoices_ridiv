from .models import Invoice,InvoiceDetail
from rest_framework import serializers

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=InvoiceDetail,
        field='__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    detail=InvoiceDetailSerializer(many=True,read_only=True)
    class Meta:
        model=Invoice,
        field='__all__'

