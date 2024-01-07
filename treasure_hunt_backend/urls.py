"""
URL configuration for treasure_hunt_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework import routers
from .views import TreasureViewSets, ProfileViewSets, UserViewSets, LoginView
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

router = routers.DefaultRouter()
router.register('users', UserViewSets)
router.register('profiles', ProfileViewSets)
router.register('treasures', TreasureViewSets)

urlpatterns = [
    path('download-schema', SpectacularAPIView.as_view(), name='download-schema'),
    path('', SpectacularSwaggerView.as_view(url_name='download-schema'), name='schema'),
    path('login', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
    path('admin', admin.site.urls)
]