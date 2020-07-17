
from django.urls import path

from . import views
urlpatterns = [
    path('', views.give_task, name='index'),
    path('create/employee/', views.create_employee, name='create_employee'),
    path('login/', views.login_in, name='login'),
    path('logout/', views.logout_out, name='logout'),
    path('employee-task/', views.employee_task, name='employee_task'),
    path('<int:worker_id>/sample/', views.sample, name='sample'),
]
