import random
from faker import Faker
from datetime import datetime, timedelta
from django.utils import timezone
from loyalty.models import Customer, Purchase, Review, Engagement

fake = Faker()
start_date = datetime(2024, 1, 1, tzinfo=timezone.utc)  # Make start_date timezone aware

class CustomerFactory:
    @staticmethod
    def create_customer():
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        first_joined_at = timezone.make_aware(fake.date_time_between(start_date=start_date, end_date="now"))
        return Customer.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            first_joined_at=first_joined_at
        )

class EngagementFactory:
    @staticmethod
    def create_engagement(customer):
        return Engagement.objects.create(
            customer=customer,
            login_count=random.randint(0, 10),
            product_views=random.randint(0, 30),
            time_spent=random.randint(0, 200),
            date=timezone.make_aware(fake.date_time_between(start_date=start_date, end_date="now"))
        )

class PurchaseFactory:
    @staticmethod
    def create_purchase(customer):
        return Purchase.objects.create(
            customer=customer,
            product_name=fake.word(),
            amount=random.randint(1, 20),
            purchased_at=timezone.make_aware(fake.date_time_between(start_date=start_date, end_date="now"))
        )

class ReviewFactory:
    @staticmethod
    def create_review(customer):
        return Review.objects.create(
            customer=customer,
            review_text=fake.text(max_nb_chars=200),
            rating=random.randint(1, 5),
            created_at=timezone.make_aware(fake.date_time_between(start_date=start_date, end_date="now"))
        )
