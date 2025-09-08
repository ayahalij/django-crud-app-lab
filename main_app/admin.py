from django.contrib import admin
from .models import Plant

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'plant_type', 'watering_frequency', 'created_at')
    list_filter = ('plant_type', 'watering_frequency', 'created_at')
    search_fields = ('name', 'notes')
    list_per_page = 20