from django.urls import path
from recognition import views

urlpatterns = [
    path('', views.search, name='search'),
]
