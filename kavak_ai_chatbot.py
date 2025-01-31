import openai
import streamlit as st

# Load OpenAI API key securely
openai_client = openai.OpenAI(api_key=st.secrets["openai_api_key"])

def kavak_chatbot(prompt):
    response = openai_client.chat.completions.create(
        model="gpt-4",  # Use "gpt-4-turbo" for lower cost
        messages=[
            {"role": "system", "content": "You are Kavak's AI Assistant, specialized in car valuation, auction listing, and internal process support."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("Kavak AI Assistant")
st.write("Ask me about car valuation, auction listing, and internal processes!")

user_input = st.text_input("Enter your question:")
if user_input:
    response = kavak_chatbot(user_input)
    st.write("**Kavak AI Assistant:**", response)
