from django_filters import rest_framework as filters
from plants.models import Crystal
from django.db.models import Q


class CrystalFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name',method='filter_name')
    zodiac = filters.CharFilter(method='filter_zodiac')
    planet = filters.CharFilter(method='filter_planet')
    element = filters.CharFilter(method='filter_element')
    chakra = filters.CharFilter(method='filter_chakra')
    min_vibration = filters.NumberFilter(method='filter_min_vibration')
    max_vibration = filters.NumberFilter(method='filter_max_vibration')

    def filter_name(self, queryset, name, value):
        return  queryset.filter(name__icontains=value) or queryset.filter(other_names__icontains=value)

    def filter_zodiac(self, queryset, name, value):
        zodiac_list = [l.strip() for l in value.split(',')]
        q_objects = Q()
        for zodiac_value in zodiac_list:
            q_objects &= Q(zodiac__icontains=zodiac_value)
        return queryset.filter(q_objects)

    def filter_planet(self, queryset, name, value):
        planets_list = [l.strip() for l in value.split(',')]
        q_objects = Q()
        for planets_value in planets_list:
            q_objects &= Q(planets__icontains=planets_value)
        return queryset.filter(q_objects)
    
    def filter_element(self, queryset, name, value):
        elements_list = [l.strip() for l in value.split(',')]
        q_objects = Q()
        for elements_value in elements_list:
            q_objects &= Q(elements__icontains=elements_value)
        return queryset.filter(q_objects)

    def filter_chakra(self, queryset, name, value):
        chakras_list = [l.strip() for l in value.split(',')]
        q_objects = Q()
        for chakras_value in chakras_list:
            q_objects &= Q(chakras__icontains=chakras_value)
        return queryset.filter(q_objects)
    
    def filter_min_vibration(self, queryset, name, value):
        return queryset.filter(vibration__gte=value)

    def filter_max_vibration(self, queryset, name, value):
        return queryset.filter(vibration__lte=value)

    class Meta:
        model = Crystal
        fields = []
