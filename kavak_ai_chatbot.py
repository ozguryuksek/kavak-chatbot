import openai
import streamlit as st

def kavak_chatbot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Using GPT-4 for better reasoning & context handling
        messages=[
            {"role": "system", "content": "You are Kavak's AI Assistant, specialized in car valuation, auction listing, and internal process support."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]

# Streamlit UI
st.title("Kavak AI Assistant")
st.write("Ask me about car valuation, auction listing, and internal processes!")

user_input = st.text_input("Enter your question:")
if user_input:
    response = kavak_chatbot(user_input)
    st.write("**Kavak AI Assistant:**", response)
