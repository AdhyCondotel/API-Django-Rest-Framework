from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ('id', 'users_id', 'name', 'delivery', 'status', 'photo', 'created_at', 'updated_at')

class TenantDetailSerializer(serializers.ModelSerializer):
    price = PriceSerializer(many=True)
    class Meta:
        model = Tenant
        fields = ('id', 'users_id', 'name', 'delivery', 'status', 'photo', 'price', 'created_at', 'updated_at')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'phone', 'email', 'role', 'photo', 'created_at', 'updated_at')

# class UserSerializer(serializers.ModelSerializer):
#     tenant = serializers.SerializerMethodField()
#     class Meta:
#         model = User
#         fields = ('id', 'name', 'phone', 'email', 'role', 'photo', 'tenant', 'created_at', 'updated_at')
#     def get_tenant(self, obj):
#         obj = obj.tenant.all().values('id', 'name', 'delivery')
#         if obj:
#             return obj[0]
#         return {}        


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'
