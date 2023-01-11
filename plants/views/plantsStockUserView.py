from plants.models.plant import Plant
from plants.models.plantStock import PlantStock
from plants.models.plantFavorite import PlantFavorite
from rest_framework.response import Response
from rest_framework.views import APIView
import math

class PlantsStockUserView(APIView):
    page_size = 30
    page = 1
    
    def get(self, request, user=None, format=None):
        page = int(request.query_params.get('page', None)) if request.query_params.get('page', None) is not None else self.page
        page_size = int(request.query_params.get('page_size', None)) if request.query_params.get('page_size', None) is not None else self.page_size
            
        plantStock = PlantStock.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            plantStock = plantStock.filter(name__contains = name) or plantStock.filter(other_names__contains = name) 
            
        species = self.request.query_params.get('species', None)
        if species is not None:
            plantStock = plantStock.filter(species = species) 
            
        group = self.request.query_params.get('group', None)
        if group is not None:
            plantStock = plantStock.filter(group = group) 
        
        irrigation = self.request.query_params.get('irrigation', None)
        if irrigation is not None:
            irrigation = irrigation.split(",")
            for i in irrigation:
                plantStock =  plantStock.filter(irrigation__contains=i)
            
        flowering = self.request.query_params.get('flowering', None)
        if flowering is not None:
            plantStock = plantStock.filter(flowering = flowering)
            
        inside = self.request.query_params.get('inside', None)
        if inside is not None:
            plantStock = plantStock.filter(inside = inside)
            
        price_first = self.request.query_params.get('priceFirst', None)
        if price_first is not None:
            price_second = self.request.query_params.get('priceSecond', None)
            if price_second is not None:
                plantStock =  plantStock.filter(price__gte=price_first,price__lte=price_second)
            
        order = self.request.query_params.get('order', None)
        if order is not None:
            plantStock = plantStock.order_by(order)
        
        data = []
        for item in plantStock:
            plant = Plant.objects.get(id=item.id)
            fav = PlantFavorite.objects.filter(id_user= user,id_plant = item.id)
            val = {
                "id":item.id,
                "name": plant.name,
                "otherNames": [n.removeprefix(" ") for n in plant.other_names.split(",")],
                "description": plant.description,
                "species": plant.species,
                "group": plant.group,
                "light": [l.removeprefix(" ") for l in plant.light.split(",")],
                "irrigation": plant.irrigation,
                "temperature": plant.temperature,
                "precautions": [p.removeprefix(" ") for p in plant.precautions.split(",")],
                "flowering": plant.flowering,
                "size": plant.size,
                "imageFront": plant.image_front,
                "render": plant.render,
                "inside": plant.inside,
                "quantity": item.quantity,
                "price": item.price,
                "discount": item.discount,
                "createdAt": plant.created_at,
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
