from django.db import models
from .customer import Customer

class Review(models.Model):
    customer = models.ForeignKey(Customer, related_name='reviews', on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveIntegerField()  # Assuming rating out of 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.review_text[:20]} - {self.rating}"
