from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_insert),
    # path('/insert', views.api_insert)
]   