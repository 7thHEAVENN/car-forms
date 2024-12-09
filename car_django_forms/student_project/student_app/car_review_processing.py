from sklearn.feature_extraction.text import TfidfVectorizer
from .models import CarReview  # Importing CarReview model

def extract_trending_keywords(top_n=5):
    reviews = CarReview.objects.all()
    # Correct code: Accessing 'review' field
    review_texts = [review.review for review in reviews]

    
    # Vectorize the review texts
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(review_texts)
    
    # Get feature names and sum up TF-IDF scores
    feature_names = vectorizer.get_feature_names_out()
    summed_tfidf = X.sum(axis=0).A1
    word_scores = {feature_names[i]: summed_tfidf[i] for i in range(len(feature_names))}
    
    # Sort words by score in descending order
    sorted_words = sorted(word_scores.items(), key=lambda x: x[1], reverse=True)
    trending_keywords = [word for word, score in sorted_words[:top_n]]
    
    return trending_keywords
