"""plantscrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from plants import views

version = 'api/v1/'
urlpatterns = [
    path("admin/", admin.site.urls),
    path(version +'user/login/', TokenObtainPairView.as_view(), name="token"),
    path(version +'user/refresh/', TokenRefreshView.as_view(), name="refresh"),
    path(version +'user/verify/', views.VerifyTokenView.as_view(), name="verify"),
    path(version +'v/plants/', views.PlantView.as_view(), name="plants"),
    path(version +'v/plants/<int:pk>/', views.PlantView.as_view(), name="plant"),
    path(version +'v/plants/stock/', views.PlantStockView.as_view(), name="plantsStock"),
    path(version +'v/plants/stock/<int:pk>/', views.PlantStockView.as_view(), name="plantStock"),
    path(version +'v/plants/stock/user/<int:pk>/', views.PlantStockFavView.as_view(), name="plantsStockUser"),
    path(version +'v/crystals/', views.CrystalView.as_view(), name="crystals"),
    path(version +'v/crystals/<int:pk>/', views.CrystalView.as_view(), name="crystal"),
    path(version +'v/crystals/stock', views.CrystalStockView.as_view(), name="crystalStock"),
    path(version +'v/crystals/stock/<int:pk>/', views.CrystalStockView.as_view(), name="crystalsStock"),
    path(version +'crystalis/<int:user>/',
         views.CrystalStockUserView.as_view(), name="crystalsFavs"),
    path(version +'plantis/<int:user>/',
         views.PlantsStockUserView.as_view(), name="plantsFavs"),
    path(version +'species/', views.SpeciesView.as_view(), name="species"),
    path("", include("plants.controller")),
]
