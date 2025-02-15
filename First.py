import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Load API Key from environment variable or hardcoded for now
api_key = "AIzaSyB3Iya6KRB0d96Kl0KeqDBxp5rKd5Dafbc"
genai.configure(api_key=api_key)  # Make sure to configure the Gemini API with the API key

# Streamlit App Configuration
st.set_page_config(page_title="DataQueryAI", page_icon="📊", layout="wide")

# Sidebar
st.sidebar.title("🔍 DataQueryAI")
st.sidebar.subheader("AI-Powered Data Analysis")

uploaded_file = st.sidebar.file_uploader("📂 Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read and display the uploaded CSV
    df = pd.read_csv(uploaded_file)

    # Display Data Preview
    st.write("## 📜 Data Preview")
    st.dataframe(df.head(10))

    # Data Summary
    st.write("## 🔢 Data Summary")
    st.write(df.describe())

    # Data Visualization
    st.write("## 📊 Data Visualization")
    selected_column = st.selectbox("Choose a column to visualize:", df.columns)
    
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df[selected_column], bins=20, kde=True, ax=ax, color="royalblue")
    st.pyplot(fig)

    # AI Query Section
    st.write("## 🤖 AI-Powered Data Insights")
    query = st.text_area("🔍 Ask a question about your data:")

    if st.button("Get AI Insights"):
        if query:
            prompt = f"Analyze the following data:\n{df.head().to_string()}\n\nAnswer the question: {query}"
            
            # Make the request to Gemini's API
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            
            # Display the AI's response in the Streamlit app
            st.success(response.text)
        else:
            st.warning("⚠ Please enter a query.")
