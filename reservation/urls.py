from django.urls import path

from . import views

app_name = 'v1'
urlpatterns = [
    path('', views.index, name='index'),
]
