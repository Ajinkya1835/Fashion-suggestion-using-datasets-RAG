import streamlit as st
from recommend import FashionRecommender
import sys
from pathlib import Path

def main():
    st.set_page_config(page_title="Fashion Recommender", layout="wide")
    
    try:
      
        recommender = FashionRecommender()
        
        # Web interface
        st.title("🎨 Fashion Outfit Recommender")
        st.markdown("Describe your style needs to get personalized recommendations")
        
        with st.form("recommendation_form"):
            user_input = st.text_input(
                "Example: 'professional outfit for women' or 'casual summer look'",
                placeholder="What outfit are you looking for?"
            )
            n_recs = st.slider("Number of recommendations", 1, 10, 3)
            submitted = st.form_submit_button("Get Recommendations")
            
            if submitted and user_input:
                with st.spinner("Finding the best fashion matches..."):
                    results = recommender.recommend(user_input, n_recs)
                    
                st.subheader(f"Top {len(results)} Recommendations")
                cols = st.columns(2)
                
                for i, rec in enumerate(results):
                    with cols[i%2]:
                        with st.expander(f"Recommendation #{i+1}", expanded=True):
                            for key, value in rec.items():
                                if key != 'text_features':
                                    st.markdown(f"**{key.replace('_', ' ').title()}:** {value}")
            
            elif submitted and not user_input:
                st.warning("Please describe what you're looking for")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Please ensure:")
        st.info("1. You've run preprocess.py and feature_engineering.py first")
        st.info("2. All data files exist in the same folder")

if __name__ == "__main__":
    if 'streamlit' in sys.modules:
        main()
    else:
        print("\n⚠️ Please run this app using:")
        print("streamlit run app.py")
        print("\nDon't run it as a normal Python script!")