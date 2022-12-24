from rest_framework import routers
from plants.viewsets.userViewsets import UserViewSet

router = routers.DefaultRouter()

router.register("api/v1/users", UserViewSet, "users")

urlpatterns = router.urls