from django.urls import path
from . import views

app_name = 'fruits'

urlpatterns = [
    path("create", views.CreateFruitView.as_view(), name='create'),
    path("", views.DisplayFruitListView.as_view(), name='index'),
    path('validate_fruit/', views.validate_fruit, name='validate_fruit'),
]