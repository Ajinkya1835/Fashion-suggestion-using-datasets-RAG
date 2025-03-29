import pandas as pd
from pathlib import Path

def preprocess_data():
    try:
        # 1. Locate and load the raw data file
        current_dir = Path(__file__).parent
        input_path = current_dir / "Fashion(Data Points) - Form responses 1.csv"
        
        print(f"Loading data from: {input_path}")
        df = pd.read_csv(input_path, encoding='utf-8')
        
        # 2. Show all available columns for reference
        print("\nOriginal columns in your CSV:")
        print(df.columns.tolist())
        
        # 3. Map your exact column names to our required names
        column_mapping = {
            "gender": "  2.Gender  ",
            "outfit_style": "Section 2: Style Preferences\n4. How would you describe your go-to daily outfit? (Select one)  ",
            "color_palette": " 5. What's your favorite color palette for clothing?  ",
            "wardrobe_type": "  7.Which of these best describes your wardrobe?  ",
            "footwear": " 13. What kind of footwear do you wear most often?  ",
            "lifestyle_activity": "14. How active is your daily lifestyle?  "
        }
        
        # 4. Verify and apply column mapping
        available_columns = []
        for our_name, actual_name in column_mapping.items():
            if actual_name in df.columns:
                available_columns.append(our_name)
                print(f"Mapped: '{actual_name}' → '{our_name}'")
            else:
                print(f"Warning: Column '{actual_name}' not found")
        
        if not available_columns:
            raise ValueError("None of the expected columns were found")
            
        # 5. Create cleaned dataset
        cleaned_df = df.rename(columns={v:k for k,v in column_mapping.items() if v in df.columns})
        cleaned_df = cleaned_df[available_columns].fillna("Unknown")
        
        # 6. Save cleaned data
        output_path = current_dir / "cleaned_fashion_data.csv"
        cleaned_df.to_csv(output_path, index=False)
        
        print("\nSuccessfully created cleaned data with columns:")
        print(cleaned_df.columns.tolist())
        print(f"\nSaved to: {output_path}")
        
        return True
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        return False

if __name__ == "__main__":
    preprocess_data()