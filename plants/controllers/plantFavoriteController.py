from rest_framework import routers
from plants.viewsets.plantFavoriteViewsets import PlantFavoriteViewSet

router = routers.DefaultRouter()

router.register("api/v1/plants/favorites", PlantFavoriteViewSet, "plants favorites")

urlpatterns = router.urls