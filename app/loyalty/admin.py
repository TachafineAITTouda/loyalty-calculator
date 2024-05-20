from django.contrib import admin
from .models import Customer, Purchase, Review, Engagement

admin.site.register(Customer)
admin.site.register(Purchase)
admin.site.register(Review)
admin.site.register(Engagement)
