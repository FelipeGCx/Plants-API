from rest_framework import routers
from plants.viewsets.crystalViewsets import CrystalViewSet

router = routers.DefaultRouter()

router.register("api/v1/crystals", CrystalViewSet, "crystals")

urlpatterns = router.urls