from rest_framework import routers
from plants.viewsets.plantStockViewsets import PlantStockViewSet

router = routers.DefaultRouter()

router.register("api/v1/plants/stock", PlantStockViewSet, "plants stock")

urlpatterns = router.urls