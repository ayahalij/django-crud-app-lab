from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Plant type choices
PLANT_TYPES = (
    ('F', 'Flower'),
    ('C', 'Cactus'),
    ('T', 'Tree'),
    ('S', 'Succulent'),
    ('H', 'Herb'),
    ('V', 'Vegetable'),
    ('O', 'Other'),
)

# Watering frequency choices
WATERING_FREQUENCIES = (
    ('D', 'Daily'),
    ('W', 'Weekly'),
    ('B', 'Bi-weekly'),
    ('M', 'Monthly'),
    ('R', 'Rarely'),
)

# Care activity choices
CARE_ACTIVITIES = (
    ('W', 'Watering'),
    ('F', 'Fertilizing'),
    ('P', 'Pruning'),
    ('R', 'Repotting'),
    ('I', 'Inspection'),
    ('T', 'Treatment'),
    ('O', 'Other'),
)

class Plant(models.Model):
    name = models.CharField(max_length=100)
    plant_type = models.CharField(
        max_length=1,
        choices=PLANT_TYPES,
        default=PLANT_TYPES[0][0]
    )
    watering_frequency = models.CharField(
        max_length=1,
        choices=WATERING_FREQUENCIES,
        default=WATERING_FREQUENCIES[0][0]
    )
    notes = models.TextField(max_length=500, blank=True)
    image = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plant_detail', kwargs={'plant_id': self.id})
    
    def get_plant_type_display_custom(self):
        return dict(PLANT_TYPES)[self.plant_type]
    
    def get_watering_frequency_display_custom(self):
        return dict(WATERING_FREQUENCIES)[self.watering_frequency]

class CareLog(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='care_logs')
    activity = models.CharField(
        max_length=1,
        choices=CARE_ACTIVITIES,
        default=CARE_ACTIVITIES[0][0]
    )
    date = models.DateField()
    notes = models.TextField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
    
    def __str__(self):
        return f"{self.get_activity_display()} - {self.plant.name} on {self.date}"
    
    def get_absolute_url(self):
        return reverse('plant_detail', kwargs={'plant_id': self.plant.id})