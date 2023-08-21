from django_filters import rest_framework as filters
from plants.models import Plant

class PlantFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name',method='filter_name')
    species = filters.CharFilter(method='filter_species')
    group = filters.CharFilter(method='filter_group')
    light = filters.CharFilter(method='filter_light')
    temperature = filters.CharFilter(method='filter_temperature')
    irrigation = filters.CharFilter(method='filter_irrigation')
    zone = filters.CharFilter(method='filter_zone')
    flowering = filters.BooleanFilter(field_name='flowering')

    def filter_name(self, queryset, name, value):
        return  queryset.filter(name__icontains=value) or queryset.filter(other_names__icontains=value)

    def filter_species(self, queryset, name, value):
        return queryset.filter(species__icontains=value)

    def filter_group(self, queryset, name, value):
        return queryset.filter(group__icontains=value)

    def filter_light(self, queryset, name, value):
        light_list = [l.strip() for l in value.split(',')]
        return queryset.filter(light__in=light_list)

    def filter_irrigation(self, queryset, name, value):
        irrigation_list = [i.strip() for i in value.split(',')]
        return queryset.filter(irrigation__in=irrigation_list)

    def filter_zone(self, queryset, name, value):
        zone_list = [i.strip() for i in value.split(',')]
        return queryset.filter(zone__in=zone_list)

    class Meta:
        model = Plant
        fields = []
