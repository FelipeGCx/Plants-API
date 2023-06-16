from plants.models.crystal import Crystal
from plants.models.crystalStock import CrystalStock
from plants.models.crystalFavorite import CrystalFavorite
from rest_framework.response import Response
from rest_framework.views import APIView

import math


class CrystalStockUserView(APIView):
    class item:
        pass

    class Data:
        results = []
    page_size = 30
    page = 1

    def get_crystal(self, obj):
        crystals = Crystal.objects.get(id=int(obj.__dict__["id_crystal_id"]))
        return crystals.__dict__

    def add_crystal(self, obj):
        item = self.item()
        item.id = obj.__dict__["id"]
        item.quantity = obj.__dict__["quantity"]
        item.price = obj.__dict__["price"]
        item.state = obj.__dict__["state"]
        crystal = self.get_crystal(obj)
        item.name = crystal.get("name")
        description = crystal.get("description")
        item.description = description
        vibration = crystal.get("vibration")
        item.vibration = vibration
        benefits = crystal.get("benefits")
        item.benefits = benefits
        properties = crystal.get("properties")
        item.properties = properties
        zodiac = crystal.get("zodiac")
        item.zodiac = zodiac
        planets = crystal.get("planets")
        item.planets = planets
        elements = crystal.get("elements")
        item.elements = elements
        chakras = crystal.get("chakras")
        item.chakras = chakras
        image_crystal = crystal.get("image_crystal")
        item.image_crystal = image_crystal
        image_gemstone = crystal.get("image_gemstone")
        item.image_gemstone = image_gemstone
        created_at = crystal.get("created_at")
        item.created_at = created_at
        return item

    def get(self, request, user=None, format=None):
        page = int(request.query_params.get('page', None)) if request.query_params.get(
            'page', None) is not None else self.page
        page_size = int(request.query_params.get('page_size', None)) if request.query_params.get(
            'page_size', None) is not None else self.page_size

        crystalStock = CrystalStock.objects.all()
        crystalisStock = self.Data()
        crystalisStock.results = [
            self.add_crystal(obj) for obj in crystalStock]
        crystalisStock = crystalisStock.results

        name = self.request.query_params.get('name', None)
        if name is not None:
            crystalStock = list(
                filter(lambda x: name.lower() in x.name.lower(), crystalisStock))

        vibration = self.request.query_params.get('vibration', None)
        if vibration is not None:
            crystalisStock = list(filter(lambda x: int(vibration) in x.vibration, crystalisStock)
                                  )

        zodiac = self.request.query_params.get('zodiac', None)
        if zodiac is not None:
            zodiac = zodiac.split(",")
            for z in zodiac:
                crystalisStock = list(
                    filter(lambda x: z.lower() in x.zodiac.lower(), crystalisStock))

        planets = self.request.query_params.get('planets', None)
        if planets is not None:
            planets = planets.split(",")
            for p in planets:
                crystalisStock = list(
                    filter(lambda x: p.lower()
                           in x.planets.lower(), crystalisStock)
                )

        chakras = self.request.query_params.get('chakras', None)
        if chakras is not None:
            chakras = chakras.split(",")
            for c in chakras:
                crystalisStock = list(
                    filter(lambda x: c.lower()
                           in x.chakras.lower(), crystalisStock)
                )

        elements = self.request.query_params.get('elements', None)
        if elements is not None:
            elements = elements.split(",")
            for e in elements:
                crystalisStock = list(
                    filter(lambda x: e.lower()
                           in x.elements.lower(), crystalisStock)
                )

        data = []
        for item in crystalisStock:
            fav = CrystalFavorite.objects.filter(
                id_user=user, id_crystal=item.id, )
            val = {
                "id": item.id,
                "name": item.name,
                "description": item.description,
                "vibration": item.vibration,
                "benefits": [b.removeprefix(" ") for b in item.benefits.split(",")],
                "properties": [p.removeprefix(" ") for p in item.properties.split(",")],
                "zodiac": [z.removeprefix(" ") for z in item.zodiac.split(",")],
                "planets": [p.removeprefix(" ") for p in item.planets.split(",")],
                "elements": [e.removeprefix(" ") for e in item.elements.split(",")],
                "chakras": [c.removeprefix(" ") for c in item.chakras.split(",")],
                "imageCrystal": item.image_crystal,
                "imageGemstone": item.image_gemstone,
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
