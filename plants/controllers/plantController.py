from rest_framework import routers
from plants.viewsets.plantViewsets import PlantViewSet

router = routers.DefaultRouter()

router.register("api/v1/plants", PlantViewSet, "plants")

urlpatterns = router.urls