from rest_framework import serializers
from .models import *

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProdSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prod
        fields = "__all__"

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class MethodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Method
        fields = "__all__"

class FactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = "__all__"