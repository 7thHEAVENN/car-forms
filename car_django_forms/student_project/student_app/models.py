# student_app/models.py
from django.db import models

class CarReview(models.Model):
    car_model = models.CharField(max_length=100)
    reviewer_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    review = models.TextField()    

    def __str__(self):
        return f"{self.car_model} - {self.reviewer_name}"

class CarBid(models.Model):
    car_review = models.ForeignKey(CarReview, on_delete=models.CASCADE)  # Linking bid to review
    bidder_name = models.CharField(max_length=100)  # Define this field
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Define this field

    def __str__(self):
        return f"Bid for {self.car_review.car_model} by {self.bidder_name}"
