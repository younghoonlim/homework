from django.urls import path
from. import views


urlpatterns=[
    path('holy/',views.holy, name='holy'),
]