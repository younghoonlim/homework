from django.urls import path
from . import views

urlpatterns=[
    path('first/',views.first, name="first"),
    path('second/',views.second),
    path('third/',views.third),
    path('firth/',views.firth, name="firth"),
]