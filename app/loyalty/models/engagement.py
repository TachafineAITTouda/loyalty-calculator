from django.db import models
from .customer import Customer

class Engagement(models.Model):
    customer = models.OneToOneField(Customer, related_name='engagement', on_delete=models.CASCADE)
    login_count = models.PositiveIntegerField(default=0)
    product_views = models.PositiveIntegerField(default=0)
    time_spent = models.PositiveIntegerField(default=0)  # Time in minutes
    date = models.DateTimeField()
    def __str__(self):
        return f"Engagement for {self.customer}"
