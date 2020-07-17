
from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('^ajax/validate_username/', views.validate_username, name='validate_username'),
]