from rest_framework import serializers
from .models import *

'''Стандартные модели сериализаторов.
Определяю поля для связанных моделей'''


class AnimalSerializer(serializers.ModelSerializer):
    staff = serializers.PrimaryKeyRelatedField(
        many=True, allow_empty=False, queryset=Staff.objects.all())

    class Meta:
        model = Animal
        fields = '__all__'


class AnimalTypeSerializer(serializers.ModelSerializer):
    animals = serializers.StringRelatedField(many=True)

    class Meta:
        model = AnimalType
        fields = '__all__'


class ShelterSerializer(serializers.ModelSerializer):
    animals = serializers.StringRelatedField(many=True, allow_null=True)
    staff = serializers.StringRelatedField(many=True, allow_null=True)

    class Meta:
        model = Shelter
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    animals = serializers.PrimaryKeyRelatedField(
        many=True, allow_empty=False, queryset=Animal.objects.all())

    class Meta:
        model = Staff
        fields = '__all__'
