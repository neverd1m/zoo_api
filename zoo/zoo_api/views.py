from django.shortcuts import render
from django.utils import timezone

# Create your views here.
from rest_framework import viewsets
from django_filters import rest_framework as filters
from django.utils import timezone

from .models import *
from .serializers import *

'''Кастомный фильтр по животным, 
включая фильтрацию по датам создания-изменения их укрытий.
'''


class AnimalsFilter(filters.FilterSet):
    # staff = filters.CharFilter(field_name='staff__name')
    shelter = filters.CharFilter(field_name='shelter__name')
    animal_type = filters.CharFilter(field_name='animal_type__name')
    created_at = filters.DateTimeFilter(
        field_name='created_at', lookup_expr='date')
    updated_at = filters.DateTimeFilter(
        field_name='updated_at', lookup_expr='date')
    linked_duration = filters.DateFilter(
        field_name='linked_staff_date', lookup_expr='lte')
    shelter_created = filters.DateTimeFilter(
        field_name='shelter__created_at', lookup_expr='date')
    shelter_updated = filters.DateTimeFilter(
        'shelter__updated_at', lookup_expr='date')

    class Meta:
        model = Animal
        fields = ['name']


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    filterset_class = AnimalsFilter
    ordering_fields = ['created_at', 'updated_at', 'name', 'quantity']

# по умолчанию ordering и так работает согласно OrderingFilter
# поэтому убрал ordering_fields параметр


class AnimalTypeViewSet(viewsets.ModelViewSet):
    queryset = AnimalType.objects.all()
    serializer_class = AnimalTypeSerializer
    filterset_fields = '__all__'


class ShelterViewSet(viewsets.ModelViewSet):
    queryset = Shelter.objects.all().order_by('created_at')
    serializer_class = ShelterSerializer
    filterset_fields = '__all__'
    ordering_fields = ['created_at', 'updated_at', 'name']


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by('created_at')
    serializer_class = StaffSerializer
    filterset_fields = '__all__'
    ordering_fields = ['created_at', 'updated_at', 'name']

    # Согласно обратной связи можно залезть в значения связанной модели,
    # и так получить желаемый фильтр! Ура!
    def get_queryset(self):
        queryset = Staff.objects.all()
        duration = self.request.query_params.get('duration', None)
        if duration is not None:
            result_queryset = []
            queryset = Staff.objects.filter(
                animalconnection__connection_date__lte=timezone.now() - timezone.timedelta(int(duration)))
        return queryset
