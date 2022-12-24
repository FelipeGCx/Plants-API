from rest_framework import routers
from plants.viewsets.crystalStockViewsets import CrystalStockViewSet

router = routers.DefaultRouter()

router.register("api/v1/crystals/stock", CrystalStockViewSet, "crystal stock")

urlpatterns = router.urls