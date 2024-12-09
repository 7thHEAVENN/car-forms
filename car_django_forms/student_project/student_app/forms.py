# student_app/forms.py
from django import forms
from .models import CarReview, CarBid

class CarReviewForm(forms.ModelForm):
    class Meta:
        model = CarReview
        fields = ['car_model', 'reviewer_name', 'rating', 'review']
        widgets = {
            'car_model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car model'}),
            'reviewer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your review'}),
        }

class CarBidForm(forms.ModelForm):
    class Meta:
        model = CarBid
        fields = ['car_review', 'bidder_name', 'bid_amount']
        widgets = {
            'car_review': forms.Select(attrs={'class': 'form-control'}),
            'bidder_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'bid_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter bid amount'}),
        }

