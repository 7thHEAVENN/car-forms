# student_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', views.home, name='home'),
    path('car_review_form/', views.car_review_form, name='car_review_form'),
    path('car_bid_form/', views.car_bid_form, name='car_bid_form'),
    path('redirect_options/', views.redirect_options, name='redirect_options'),  # New URL pattern
    
    
    path('service/', views.service, name='service'), # Service Page
    path('book-service/', views.book_service, name='book_service'),
    path('reviews/', views.review_list, name='car_review_list'),
    
    
    path('login/', LoginView.as_view(), name='login'),  # This line adds the 'login' URL pattern
    path('logout/', views.logout_view, name='logout'),  # Example for a custom logout view
    # Other URL patterns
    path('success/', views.success, name='success'),  # Define success URL pattern
    
    
]
