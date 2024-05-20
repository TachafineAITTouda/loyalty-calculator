from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Customer, Purchase, Review, Engagement
from django.utils import timezone

class CustomerAPITestCase(APITestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            first_joined_at=timezone.now()
        )
        Engagement.objects.create(customer=self.customer, login_count=5, product_views=10, time_spent=100)

    def test_add_customer(self):
        url = reverse('customer-list')
        data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com",
            "first_joined_at": "2024-01-01T00:00:00Z"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)
        self.assertEqual(Customer.objects.get(id=response.data['id']).first_name, "Jane")

    def test_get_customers(self):
        url = reverse('customer-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['email'], self.customer.email)

    def test_get_customer_score(self):
        self.customer.update_loyalty_score()
        url = reverse('customer-score', args=[self.customer.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['loyalty_score'], self.customer.loyalty_score)

    def test_get_customer_purchases(self):
        Purchase.objects.create(customer=self.customer, product_name="Product 1", amount=100)
        url = reverse('customer-purchases', args=[self.customer.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['product_name'], "Product 1")
