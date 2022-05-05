"""unidades URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path

from vehicle.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('metrobus/',VehicleViewSet.as_view(),name='Unidades'),
    path('metrobus/<int:pk>',DetailVehicleGenericView.as_view(),name='Unidad'),
    path('metrobus/alcaldias/',TownhallGenericView.as_view(),name='Alcaldias'),
    path('metrobus/alcaldias/disponibles/',disponibles,name='lista-alcaldias')
]

urlpatterns = format_suffix_patterns(urlpatterns)