import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import CarReview  # Importing CarReview model

def get_car_recommendations(car_model, top_n=3):
    reviews = CarReview.objects.all()
    review_texts = [review.review for review in reviews]  # Change to 'review' field
    car_models = [review.car_model for review in reviews]

    # Vectorize the review texts
    vectorizer = TfidfVectorizer()
    review_vectors = vectorizer.fit_transform(review_texts)

    # Get the vector for the specified car_model
    try:
        car_index = car_models.index(car_model)
    except ValueError:
        return []

    car_vector = review_vectors[car_index]

    # Compute cosine similarity with other reviews
    similarity_scores = cosine_similarity(car_vector, review_vectors).flatten()
    
    # Get indices of top similar cars
    similar_indices = np.argsort(-similarity_scores)[1:top_n+1]
    similar_cars = [(car_models[i], similarity_scores[i]) for i in similar_indices]
    
    return similar_cars
