from django_filters import rest_framework as filters
from plants.models import CrystalStock
from django.db.models import Q


class CrystalStockFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', method='filter_name')
    zodiac = filters.CharFilter(method='filter_zodiac')
    planet = filters.CharFilter(method='filter_planet')
    element = filters.CharFilter(method='filter_element')
    chakra = filters.CharFilter(method='filter_chakra')
    min_vibration = filters.NumberFilter(method='filter_min_vibration')
    max_vibration = filters.NumberFilter(method='filter_max_vibration')
    state = filters.BooleanFilter(field_name='state')
    min_price = filters.NumberFilter(method='filter_min_price')
    max_price = filters.NumberFilter(method='filter_max_price')

    def filter_name(self, queryset, name, value):
        return queryset.filter(id_crystal__name__icontains=value)

    def filter_zodiac(self, queryset, name, value):
        zodiac_list = [l.strip() for l in value.split(',')]
        q_objects = Q()
        for zodiac_value in zodiac_list:
            q_objects &= Q(id_crystal__zodiac__icontains=zodiac_value)
        return queryset.filter(q_objects)

    def filter_planet(self, queryset, name, value):
        planets_list = [l.strip() for l in value.split(',')]
        q_objects = Q()
        for planets_value in planets_list:
            q_objects &= Q(id_crystal__planets__icontains=planets_value)
        return queryset.filter(q_objects)

    def filter_element(self, queryset, name, value):
        elements_list = [l.strip() for l in value.split(',')]
        q_objects = Q()
        for elements_value in elements_list:
            q_objects &= Q(id_crystal__elements__icontains=elements_value)
        return queryset.filter(q_objects)

    def filter_chakra(self, queryset, name, value):
        chakras_list = [l.strip() for l in value.split(',')]
        q_objects = Q()
        for chakras_value in chakras_list:
            q_objects &= Q(id_crystal__chakras__icontains=chakras_value)
        return queryset.filter(q_objects)

    def filter_min_vibration(self, queryset, name, value):
        return queryset.filter(id_crystal__vibration__gte=value)

    def filter_max_vibration(self, queryset, name, value):
        return queryset.filter(id_crystal__vibration__lte=value)

    def filter_min_price(self, queryset, name, value):
        return queryset.filter(price__gte=value)

    def filter_max_price(self, queryset, name, value):
        return queryset.filter(price__lte=value)

    class Meta:
        model = CrystalStock
        fields = []
