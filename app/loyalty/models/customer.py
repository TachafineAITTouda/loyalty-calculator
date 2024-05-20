from django.db import models
from django.utils import timezone
from loyalty.score_calculator import ScoreCalculator

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    first_joined_at = models.DateTimeField()
    loyalty_score = models.FloatField(default=0.0)
    score_last_calculated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def calculate_loyalty_score(self):
        calculator = ScoreCalculator(self)
        self.loyalty_score = calculator.calculate_loyalty_score()
        self.score_last_calculated = timezone.now()
        self.save()
        return self.loyalty_score

    def update_loyalty_score(self):
        self.loyalty_score = self.calculate_loyalty_score()
        self.score_last_calculated = timezone.now()
        self.save()