# student_app/admin.py
from django.contrib import admin
from .models import CarReview, CarBid  # Updated models

admin.site.register(CarReview)
admin.site.register(CarBid)
