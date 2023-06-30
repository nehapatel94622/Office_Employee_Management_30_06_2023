from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_detail/', views.view_all, name='view_detail'),
    path('add/', views.add_emp, name='add'),
    path('remove/', views.remove_emp, name='remove'),
    path('remove/<int:emp_id>', views.remove_emp, name='remove'),
    path('filter/', views.filter_emp, name='filter'),
]
