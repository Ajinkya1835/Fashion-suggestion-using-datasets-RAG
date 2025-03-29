import pandas as pd
from pathlib import Path
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def generate_features():
    try:
        # 1. Load cleaned data
        current_dir = Path(__file__).parent
        input_path = current_dir / "cleaned_fashion_data.csv"
        
        print(f"Loading cleaned data from: {input_path}")
        df = pd.read_csv(input_path)
        
        # 2. Show available features
        print("\nAvailable features in cleaned data:")
        print(df.columns.tolist())
        
        # 3. Create combined text features from all available columns
        df["text_features"] = df.apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
        
        # 4. Generate TF-IDF features
        tfidf = TfidfVectorizer(stop_words='english', max_features=500)
        tfidf_matrix = tfidf.fit_transform(df["text_features"])
        
        # 5. Save the generated features
        output_files = {
            "tfidf_matrix.pkl": tfidf_matrix,
            "tfidf_features.pkl": tfidf.get_feature_names_out(),
            "processed_data.csv": df
        }
        
        print("\nSaving generated features:")
        for filename, data in output_files.items():
            filepath = current_dir / filename
            if isinstance(data, pd.DataFrame):
                data.to_csv(filepath, index=False)
            else:
                with open(filepath, "wb") as f:
                    pickle.dump(data, f)
            print(f"- {filename}")
        
        print("\nFeature engineering completed successfully!")
        return True
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Make sure preprocess.py ran successfully first")
        print("2. Verify cleaned_fashion_data.csv exists")
        if 'df' in locals():
            print("\nCurrent columns:", df.columns.tolist())
        return False

if __name__ == "__main__":
    generate_features()