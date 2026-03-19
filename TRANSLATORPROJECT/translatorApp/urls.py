from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('history/', views.history, name='history'),
    path('edit/<int:id>/', views.edit_translation, name='edit'),
    path('create/', views.create_translation, name='create_translation'),
    path('delete/<int:id>/', views.delete_translation, name='delete'),
    
]