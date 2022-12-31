from rest_framework import routers
from plants.viewsets.crystalViewsets import CrystalViewSet
from plants.viewsets.crystalFavoriteViewsets import CrystalFavoriteViewSet
from plants.viewsets.crystalStockViewsets import CrystalStockViewSet
from plants.viewsets.orderPurchaseViewsets import OrderPurchaseViewSet
from plants.viewsets.orderSaleViewsets import OrderSaleViewSet
from plants.viewsets.plantFavoriteViewsets import PlantFavoriteViewSet
from plants.viewsets.plantStockViewsets import PlantStockViewSet
from plants.viewsets.plantViewsets import PlantViewSet
from plants.viewsets.peToOpViewsets import ProductEntryToOrderPurchaseViewSet
from plants.viewsets.poToOsViewsets import ProductOrderToOrderSaleViewSet
from plants.viewsets.potViewset import PotViewSet
from plants.viewsets.productEntryViewsets import ProductEntryViewSet
from plants.viewsets.productOrderViewsets import ProductOrderViewSet
from plants.viewsets.userViewsets import UserViewSet

router = routers.DefaultRouter()

# Crystals
router.register("api/v1/crystals", CrystalViewSet, "crystals")
# Crystals Favorite
router.register("api/v1/favorite/crystals", CrystalFavoriteViewSet, "favorite crystals")
# Crystals Stock
router.register("api/v1/stock/crystals", CrystalStockViewSet, "stock crystals")
# Order Purchases
router.register("api/v1/order/purchase", OrderPurchaseViewSet    , "order purchase")
# Order Sales
router.register("api/v1/order/sale", OrderSaleViewSet , "order sale")
# Plants
router.register("api/v1/plants", PlantViewSet, "plants")
# Plants Favorite
router.register("api/v1/favorite/plants", PlantFavoriteViewSet , "favorite plants")
# Plants Stock
router.register("api/v1/stock/plants", PlantStockViewSet, "stock plants")
# Product Entry To Order Purchase
router.register("api/v1/potoop", ProductEntryToOrderPurchaseViewSet, "petoop")
# Product Order To Order Sale
router.register("api/v1/potoos", ProductOrderToOrderSaleViewSet, "potoos")
# Pots
router.register("api/v1/pots", PotViewSet, "pots")
# Products Entry
router.register("api/v1/entry/products/",  ProductEntryViewSet, "product entry")
# Products Order
router.register("api/v1/order/products", ProductOrderViewSet , "product order")
# User
router.register("api/v1/user", UserViewSet, "users")

urlpatterns = router.urls