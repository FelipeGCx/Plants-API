from plants.models import Plant
from rest_framework.response import Response
from rest_framework.views import APIView


class SpeciesView(APIView):
    def get(self, user=None, format=None):
        queryset = Plant.objects.all()
        unic_values = queryset.values('species').distinct()
        final_data = {
            "results": [x["species"] for x in unic_values if x["species"] != "NA"]
        }
        return Response(final_data, status=200)
