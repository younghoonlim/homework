"""brw_prac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from prac1 import views, urls
from prac2 import urls as prac2_urls
from prac1.views import list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('prac1/', include(urls)),
    path('prac2/', include(prac2_urls)),
    path('list/', list, name="list"),
]
