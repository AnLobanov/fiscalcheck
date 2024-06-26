"""
URL configuration for fiscalcheck project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, reverse_lazy, include
from django.views.generic.base import RedirectView
from kkm.views import *

admin.site.site_url = ''

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    path('admin-interface/logo/logo_hUmoN5m.png', RedirectView.as_view(url='/static/logo.png', permanent=True)),
    path('api/kkm', KKMAPIList.as_view()),
    path('api/kkm/<str:pk>', KKMAPIRetrieve.as_view()),
    path('api/error', ErrorAPIList.as_view())
]
