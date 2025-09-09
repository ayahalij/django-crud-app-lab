from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('plants/', views.plants_index, name='plants_index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='plant_detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
    path('care-logs/', views.all_care_logs, name='all_care_logs'),
    path('plants/<int:plant_id>/care_logs/', views.care_logs_index, name='care_logs_index'),
    path('plants/<int:plant_id>/care_logs/create/', views.CareLogCreate.as_view(), name='care_logs_create'),
    path('care_logs/<int:pk>/update/', views.CareLogUpdate.as_view(), name='care_logs_update'),
    path('care_logs/<int:pk>/delete/', views.CareLogDelete.as_view(), name='care_logs_delete'),
    path('logout/', views.logout_view, name='logout'),
]