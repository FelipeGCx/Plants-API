from plants.models.plant import Plant
from plants.models.plantStock import PlantStock
from plants.models.plantFavorite import PlantFavorite
from rest_framework.response import Response
from rest_framework.views import APIView
import math

class PlantsStockUserView(APIView):
    class item:
        pass   
    class Data:
        results=[]
    page_size = 30
    page = 1
    
    def get_plant(self, obj):
        # id_plant = obj.id_plant.replace("Plant object (","").replace(")","") 
        plants = Plant.objects.get(id=int(obj.__dict__["id_plant_id"]))
        return plants.__dict__
    
    def add_plant(self,obj):
        item = self.item()
        item.id = obj.__dict__["id"]
        item.quantity = obj.__dict__["quantity"]
        item.discount = obj.__dict__["discount"]
        item.price = obj.__dict__["price"]
        item.state = obj.__dict__["state"]
        plant = self.get_plant(obj)
        item.name =  plant.get("name")
        other_names = plant.get("other_names")
        item.other_names = other_names
        description = plant.get("description")
        item.description = description
        species = plant.get("species")
        item.species = species
        group = plant.get("group")
        item.group = group
        light = plant.get("light")
        item.light = light
        irrigation = plant.get("irrigation")
        item.irrigation = irrigation
        temperature = plant.get("temperature")
        item.temperature = temperature
        precautions = plant.get("precautions")
        item.precautions = precautions
        flowering = plant.get("flowering")
        item.flowering = flowering
        size = plant.get("size")
        item.size = size
        image_front =  plant.get("image_front")
        item.image_front =  image_front
        render =  plant.get("render")
        item.render =  render
        inside =  plant.get("inside")
        item.inside =  inside
        created_at =  plant.get("created_at")
        item.created_at =  created_at
        return item
    
    def get(self, request, user=None, format=None):
        page = int(request.query_params.get('page', None)) if request.query_params.get('page', None) is not None else self.page
        page_size = int(request.query_params.get('page_size', None)) if request.query_params.get('page_size', None) is not None else self.page_size
            
        plantStock = PlantStock.objects.all()
        plantisStock = self.Data()
        plantisStock.results = [self.add_plant(obj) for obj in plantStock]
        plantisStock = plantisStock.results
        
        name = self.request.query_params.get('name', None)
        if name is not None:
            # plantisStock = plantisStock.filter(name__contains = name) or plantisStock.filter(other_names__contains = name) 
            plantisStock = list(filter(lambda x: name.lower() in x.name.lower() or name.lower() in x.other_names.lower(), plantisStock))
            
        species = self.request.query_params.get('species', None)
        if species is not None:
            # plantisStock = plantisStock.filter(species = species) 
            plantisStock = list(filter(lambda x: x.species.lower() == species.lower(), plantisStock))
            
        group = self.request.query_params.get('group', None)
        if group is not None:
            # plantisStock = plantisStock.filter(group = group) 
            plantisStock = list(filter(lambda x: x.group.lower() == group.lower(), plantisStock))
        
        irrigation = self.request.query_params.get('irrigation', None)
        if irrigation is not None:
            irrigation = irrigation.split(",")
            for i in irrigation:
                # plantisStock =  plantisStock.filter(irrigation__contains=i)
                plantisStock = list(filter(lambda x: i.lower() in x.irrigation.lower(), plantisStock))
                                                    
        flowering = self.request.query_params.get('flowering', None)
        if flowering is not None:
            # plantisStock = plantisStock.filter(flowering = flowering)
            plantisStock = list(filter(lambda x: x.flowering == flowering, plantisStock))
            
        inside = self.request.query_params.get('inside', None)
        if inside is not None:
            # plantisStock = plantisStock.filter(inside = inside)
            plantisStock = list(filter(lambda x: x.inside == inside, plantisStock))
            
        price_first = self.request.query_params.get('priceFirst', None)
        if price_first is not None:
            price_second = self.request.query_params.get('priceSecond', None)
            if price_second is not None:
                # plantisStock =  plantisStock.filter(price__gte=price_first,price__lte=price_second)
                plantisStock = list(filter(lambda x: x.price >= int(price_first) and x.price <= int(price_second), plantisStock))
            
        # order = self.request.query_params.get('order', None)
        # if order is not None:
        #     # plantisStock = plantisStock.order_by(order)
        #     # plantisStock = sorted(plantisStock, key=lambda x: x["price"], reverse=True if "-" in order else False)
        #     plantisStock = plantisStock.sort(key=lambda x: x.price, reverse=True if "-" in order else False)
        
        data = []
        for item in plantisStock:
            if item.state:
                fav = PlantFavorite.objects.filter(id_user= user,id_plant = item.id)
                val = {
                    "id":item.id,
                    "name": item.name,
                    "otherNames": [n.removeprefix(" ") for n in item.other_names.split(",")],
                    "description": item.description,
                    "species": item.species,
                    "group": item.group,
                    "light": [l.removeprefix(" ") for l in item.light.split(",")],
                    "irrigation": item.irrigation,
                    "temperature": item.temperature,
                    "precautions": [p.removeprefix(" ") for p in item.precautions.split(",")],
                    "flowering": item.flowering,
                    "size": item.size,
                    "imageFront": item.image_front,
                    "render": item.render,
                    "inside": item.inside,
                    "quantity": item.quantity,
                    "price": item.price,
                    "discount": item.discount,
                    "createdAt": item.created_at,
                    "state": item.state,
                    "favorite": True if fav else False  
                }
                data.append(val)
                
        order = self.request.query_params.get('order', None)
        if order is not None:
            data = sorted(data, key=lambda x: x[str(order).replace("-","")], reverse=True if "-" in order else False)
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
