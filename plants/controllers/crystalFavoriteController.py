from rest_framework import routers
from plants.viewsets.crystalFavoriteViewsets import CrystalFavoriteViewSet

router = routers.DefaultRouter()

router.register("api/v1/crystals/favorites", CrystalFavoriteViewSet, "crystals favorites")

urlpatterns = router.urls