from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializers import *


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all().order_by('created_at')
    serializer_class = AnimalSerializer
    filterset_fields = ['shelter__name', 'animal_type__name', 'staff__name']


class AnimalTypeViewSet(viewsets.ModelViewSet):
    queryset = AnimalType.objects.all().order_by('created_at')
    serializer_class = AnimalTypeSerializer


class ShelterViewSet(viewsets.ModelViewSet):
    queryset = Shelter.objects.all().order_by('created_at')
    serializer_class = ShelterSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by('created_at')
    serializer_class = StaffSerializer
