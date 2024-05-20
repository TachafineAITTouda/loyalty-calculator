from django.core.management.base import BaseCommand
from loyalty.models import Customer

class Command(BaseCommand):
    help = 'Update loyalty scores for all customers'

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()
        self.stdout.write(f"Updating loyalty scores for {len(customers)} customers")
        for customer in customers:
            try:
                score = customer.calculate_loyalty_score()
                self.stdout.write(self.style.SUCCESS(f"Updated loyalty score for customer {customer.id} to {score}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to update loyalty score for customer {customer.id}: {str(e)}"))
        self.stdout.write(self.style.SUCCESS('Successfully updated loyalty scores for all customers'))