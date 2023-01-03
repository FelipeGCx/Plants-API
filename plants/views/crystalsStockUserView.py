from plants.models.crystal import Crystal
from plants.models.crystalStock import CrystalStock
from plants.models.crystalFavorite import CrystalFavorite
from rest_framework.response import Response
from rest_framework.views import APIView
import math

class CrystalStockUserView(APIView):
    page_size = 30
    page = 1
    
    def get(self, request, user=None, format=None):
        page = int(request.query_params.get('page', None)) if request.query_params.get('page', None) is not None else self.page
        page_size = int(request.query_params.get('page_size', None)) if request.query_params.get('page_size', None) is not None else self.page_size
            
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
        total_items = len(data)
        total_pages = math.ceil(total_items/page_size)
        l_item = page*page_size
        f_item = l_item - page_size
        
        paginated_data = data[f_item:l_item]
        final_data = {
            "totalItems": total_items,
            "totalPages": total_pages,
            "page": page,
            "results": paginated_data
        }
        return Response(final_data, status=200)
