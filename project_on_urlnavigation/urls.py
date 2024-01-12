"""
URL configuration for project_on_urlnavigation project.

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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Hidden_places_in_india/',Hidden_places_in_india,name='Hidden_places_in_india'),
    path('Gandikota/',Gandikota,name='Gandikota'),
    path('Gurez_valley/',Gurez_valley,name='Gurez_valley'),
    path('lakshadweep/',lakshadweep,name='lakshadweep'),
    path('Ziro_valley/',Ziro_valley,name='Ziro_valley'),
    path('sandakphu/',sandakphu,name='sandakphu'),
    

]
