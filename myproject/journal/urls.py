from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:pk>/', views.edit_entry, name='edit_entry'),
    path('delete/<int:pk>/', views.delete_entry, name='delete_entry'),
    path('toggle_complete/<int:pk>/', views.toggle_complete, name='toggle_complete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Маршрут для входа
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Маршрут для выхода
]
