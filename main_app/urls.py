from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('plants/', views.plants_index, name='plants_index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='plant_detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
]