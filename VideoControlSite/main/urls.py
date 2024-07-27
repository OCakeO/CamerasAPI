from django.urls import path
from . import views
from .views import CamDBDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('add_camdb/', views.add_camdb, name='add_camdb'),
    path('camdb_list/', views.camdb_list, name='camdb_list'),
    path('camdb/', views.camdb_list, name='camdb_list'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('delete_all_camdb/', views.delete_all_ads, name='delete_all_camdb'),
    path('register/', views.register, name='register'),
    path('api/camdb/<str:camdb_id>/', views.view_camdb_json, name='view_camdb_json'),
]
