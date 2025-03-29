import streamlit as st
import requests

st.title("Fashion Outfit Recommender")

user_input = st.text_input("Describe your style (e.g., 'casual outfit for women'):")
if st.button("Get Recommendations"):
    response = requests.post(
        "http://localhost:5000/recommend",
        json={"query": user_input}
    ).json()
    
    for i, rec in enumerate(response, 1):
        st.subheader(f"Recommendation #{i}")
        st.write(f"**Gender:** {rec['gender']}")
        st.write(f"**Style:** {rec['outfit_style']}")
        st.write(f"**Colors:** {rec['color_palette']}")
        st.write(f"**Footwear:** {rec['footwear']}")
        st.write("---")