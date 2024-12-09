import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
from .models import CarReview

def get_car_recommendations(car_model, top_n=3):
    reviews = CarReview.objects.all()
    review_texts = [review.review for review in reviews]
    car_models = [review.car_model for review in reviews]

    # Vectorize the review texts
    vectorizer = TfidfVectorizer()
    review_vectors = vectorizer.fit_transform(review_texts)

    # Get the vector for the specified car_model
    if car_model in car_models:
        car_index = car_models.index(car_model)
        car_vector = review_vectors[car_index]
        similarity_scores = cosine_similarity(car_vector, review_vectors).flatten()
        
        similar_indices = np.argsort(-similarity_scores)[1:top_n+1]
        similar_cars = [(car_models[i], similarity_scores[i]) for i in similar_indices]
        return similar_cars
    return []

def extract_trending_keywords(top_n=5):
    reviews = CarReview.objects.all()
    review_texts = [review.review_text for review in reviews]
    
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(review_texts)
    feature_names = vectorizer.get_feature_names_out()
    summed_tfidf = X.sum(axis=0).A1
    
    word_scores = {feature_names[i]: summed_tfidf[i] for i in range(len(feature_names))}
    sorted_words = sorted(word_scores.items(), key=lambda x: x[1], reverse=True)
    trending_keywords = [word for word, _ in sorted_words[:top_n]]
    
    return trending_keywords
