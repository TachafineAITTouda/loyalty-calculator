import random
from django.core.management.base import BaseCommand
from loyalty.factories import CustomerFactory, EngagementFactory, PurchaseFactory, ReviewFactory

class Command(BaseCommand):
    help = 'Populate the database with fake user behavior data'

    def handle(self, *args, **kwargs):
        num_customers = 100

        for _ in range(num_customers):
            customer = CustomerFactory.create_customer()
            EngagementFactory.create_engagement(customer)

            customer_type = random.choice(['activity_only', 'activity_and_purchases', 'activity_purchases_reviews'])

            if customer_type in ['activity_and_purchases', 'activity_purchases_reviews']:
                num_purchases = random.randint(1, 20)  
                for _ in range(num_purchases):
                    PurchaseFactory.create_purchase(customer)

                if customer_type == 'activity_purchases_reviews':
                    num_reviews = random.randint(1, num_purchases) 
                    for _ in range(num_reviews):
                        ReviewFactory.create_review(customer)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake data'))
