from django.shortcuts import render, redirect,get_object_or_404
from django.shortcuts import render,redirect

from .forms import CarReviewForm, CarBidForm
from .models import CarReview, CarBid
from django.contrib import messages
from .recommendations import get_car_recommendations

#login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm



from django.contrib.auth import logout
from django.shortcuts import redirect

from .car_review_processing import extract_trending_keywords

def create_car_review(request):
    if request.method == 'POST':
        form = CarReviewForm(request.POST)
        if form.is_valid():
            form.save()  # Save the review
            return redirect('success_url')  # Redirect to a success page
    else:
        form = CarReviewForm()

    return render(request, 'car_review_form.html', {'form': form})

def car_reviews(request, car_model=None):
    # Fetch the latest review as an example
    review = CarReview.objects.latest('created_at') if car_model is None else CarReview.objects.filter(car_model=car_model).first()
    recommendations = get_car_recommendations(review.car_model) if review else []
    trending_keywords = extract_trending_keywords()

    return render(request, 'student_app/car_reviews.html', {
        'review': review,
        'recommendations': recommendations,
        'trending_keywords': trending_keywords,
    })

def home(request):
    # Fetch the most recent review based on the highest id
    review = CarReview.objects.latest('id')

    # Get recommendations based on the car model of the latest review
    recommendations = get_car_recommendations(review.car_model, top_n=3)

    # Get trending keywords across all reviews
    trending_keywords = extract_trending_keywords(top_n=5)

    context = {
        'review': review,
        'recommendations': recommendations,
        'trending_keywords': trending_keywords,
    }
    return render(request, 'student_app/home.html', context)


def car_review_form(request):
    if request.method == 'POST':
        form = CarReviewForm(request.POST)
        if form.is_valid():
            form.save()  # Save the review
            return redirect('redirect_options')  # Redirect to options page
    else:
        form = CarReviewForm()
    return render(request, 'student_app/car_review_form.html', {'form': form})


def car_bid_form(request):
    if request.method == 'POST':
        form = CarBidForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bid submitted successfully!')
            
            # Get the next page from the query parameters
            next_page = request.GET.get('next', 'success')  # Default to 'success' page if no next param
            return redirect(next_page)  # Redirect to the next page or success page
    else:
        form = CarBidForm()
    
    return render(request, 'student_app/car_bid_form.html', {'form': form})


def car_detail(request, car_model):
    # Fetch the car review details
    review = get_object_or_404(CarReview, car_model=car_model)
    
    # Get recommendations for this car model
    recommendations = get_car_recommendations(car_model)
    
    # Pass both the review and recommendations to the template
    return render(request, 'student_app/car_detail.html', {
        'review': review,
        'recommendations': recommendations,
    })



def service(request):
    return render(request, 'student_app/service.html')

def book_service(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')

        # Add a success message
        messages.success(request, f"Thank you, {name}! Your service booking in {city} has been successfully submitted.")

        # Redirect back to the service page to reset the form
        return redirect('service')

    return render(request, 'student_app/service.html')


def review_list(request):
    reviews = CarReview.objects.all()  # Get all car reviews from the database
    return render(request, 'student_app/review_list.html', {'reviews': reviews})

#here login

def car_review_form(request):
    if request.method == 'POST':
        form = CarReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('redirect_options')
    else:
        form = CarReviewForm()
    return render(request, 'student_app/car_review_form.html', {'form': form})




@login_required
def review_list(request):
    reviews = CarReview.objects.all()
    return render(request, 'student_app/review_list.html', {'reviews': reviews})

def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect('home')


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # 
        else:
            messages.error(request, 'Invalid username or password.')  # Display error message
    else:
        form = AuthenticationForm()
    
    return render(request, 'student_app/login.html', {'form': form})



def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('home')  


def success(request, message):
    return render(request, 'student_app/success.html', {'message': message})

def redirect_options(request):
    return render(request, 'student_app/redirect_options.html')

def success(request):
    return render(request, 'student_app/success.html')
