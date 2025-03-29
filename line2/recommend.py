import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path

class FashionRecommender:
    def __init__(self):
        self.current_dir = Path(__file__).parent
        self.load_models()
        
    def load_models(self):
        # Load all required files
        self.df = pd.read_csv(self.current_dir / "processed_data.csv")
        with open(self.current_dir / "tfidf_matrix.pkl", "rb") as f:
            self.tfidf_matrix = pickle.load(f)
        with open(self.current_dir / "tfidf_features.pkl", "rb") as f:
            self.features = pickle.load(f)
        
        # Initialize vectorizer with existing features
        from sklearn.feature_extraction.text import TfidfVectorizer
        self.tfidf = TfidfVectorizer(vocabulary=self.features)

    def recommend(self, query, n=5):
        # Vectorize the user query
        query_vec = self.tfidf.fit_transform([query])
        
        # Calculate similarity scores
        similarity = cosine_similarity(query_vec, self.tfidf_matrix)
        
        # Get top N recommendations
        top_indices = similarity.argsort()[0][-n:][::-1]
        return self.df.iloc[top_indices].to_dict('records')

if __name__ == "__main__":
    recommender = FashionRecommender()
    while True:
        query = input("\nDescribe your fashion needs (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break
            
        results = recommender.recommend(query)
        print("\nTop Recommendations:")
        for i, rec in enumerate(results, 1):
            print(f"\nRecommendation #{i}:")
            for key, value in rec.items():
                if key != 'text_features':  # Skip the technical field
                    print(f"{key.replace('_', ' ').title()}: {value}")