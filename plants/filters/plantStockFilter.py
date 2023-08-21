from django_filters import rest_framework as filters
from plants.models import PlantStock

class PlantStockFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name',method='filter_name')
    species = filters.CharFilter(method='filter_species')
    group = filters.CharFilter(method='filter_group')
    light = filters.CharFilter(method='filter_light')
    temperature = filters.CharFilter(method='filter_temperature')
    irrigation = filters.CharFilter(method='filter_irrigation')
    zone = filters.CharFilter(method='filter_zone')
    flowering = filters.BooleanFilter(field_name='flowering')
    state = filters.BooleanFilter(field_name='state')
    min_price = filters.NumberFilter(method='filter_min_price')
    max_price = filters.NumberFilter(method='filter_max_price')

    def filter_name(self, queryset, name, value):
        return  queryset.filter(id_plant__name__icontains=value) or queryset.filter(id_plant__other_names__icontains=value)

    def filter_species(self, queryset, name, value):
        return queryset.filter(id_plant__species__icontains=value)

    def filter_group(self, queryset, name, value):
        return queryset.filter(id_plant__group__icontains=value)

    def filter_light(self, queryset, name, value):
        light_list = [l.strip() for l in value.split(',')]
        return queryset.filter(id_plant__light__in=light_list)

    def filter_irrigation(self, queryset, name, value):
        irrigation_list = [i.strip() for i in value.split(',')]
        return queryset.filter(id_plant__irrigation__in=irrigation_list)

    def filter_zone(self, queryset, name, value):
        zone_list = [i.strip() for i in value.split(',')]
        return queryset.filter(id_plant__zone__in=zone_list)
    
    def filter_min_price(self, queryset, name, value):
        return queryset.filter(price__gte=value)

    def filter_max_price(self, queryset, name, value):
        return queryset.filter(price__lte=value)

    class Meta:
        model = PlantStock
        fields = []
