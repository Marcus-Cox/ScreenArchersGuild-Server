"""screenarchersguild URL Configuration

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
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from rest_framework import routers
from screenarchersguildapi.views.screenshot import ScreenshotView
from screenarchersguildapi.views.guide import GuideView
from screenarchersguildapi.views.capturetool import CaptureToolView
from screenarchersguildapi.views.editingtool import EditingToolView
from screenarchersguildapi.views.category import CategoryView
from screenarchersguildapi.views.archer import ArcherView
from screenarchersguildapi.views.auth import register_user, login_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'screenshots', ScreenshotView, 'screenshots')
router.register(r'guides', GuideView, 'guide')
router.register(r'archers',ArcherView,"archers")
router.register(r'capturetools',CaptureToolView,"capturetools")
router.register(r'editingtools',EditingToolView,"editingtools")
router.register(r'categorys',CategoryView,"categorys")
urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
