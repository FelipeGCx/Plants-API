from plants.models.crystal import Crystal
from plants.models.crystalStock import CrystalStock
from plants.models.crystalFavorite import CrystalFavorite
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

class CrystalStockUserView(APIView):
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10
    pagination_class.max_page_size = 50
    
    def get(self, request, user=None, format=None):
        crystalStock = CrystalStock.objects.all()
        data = []
        for item in crystalStock:
            crystal = Crystal.objects.get(id=item.id)
            fav = CrystalFavorite.objects.filter(id_user= user,id_crystal = item.id, )
            val = {
                "id":item.id,
                "name": crystal.name,
                "description": crystal.description,
                "vibration": crystal.vibration,
                "benefits": [b.removeprefix(" ") for b in crystal.benefits.split(",")],
                "properties": [p.removeprefix(" ") for p in crystal.properties.split(",")],
                "zodiac": [z.removeprefix(" ") for z in crystal.zodiac.split(",")],
                "planets": [p.removeprefix(" ") for p in crystal.planets.split(",")],
                "elements": [e.removeprefix(" ") for e in crystal.elements.split(",")],
                "chakras": [c.removeprefix(" ") for c in crystal.chakras.split(",")],
                "image_crystal": crystal.image_crystal,
                "image_gemstone": crystal.image_gemstone,
                "quantity": item.quantity,
                "price": item.price,
                "state": item.state,
                "favorite": True if fav else False  
            }
            data.append(val)
        paginated_queryset = self.paginate_queryset(data)
        return self.get_paginated_response(paginated_queryset)
        # return Response(data, status=200)
