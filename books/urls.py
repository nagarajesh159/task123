from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_book/', views.save_book, name='save_book'),
    path('getAllBooks/', views.get_all_books, name='book_list'),
]
