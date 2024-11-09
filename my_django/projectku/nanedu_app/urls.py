from django.urls import path
from nanedu_app import views

urlpatterns = [
    path('', views.index, name='index'),
]