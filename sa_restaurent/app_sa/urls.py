from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path("add_data/",views.add_data),
]
                