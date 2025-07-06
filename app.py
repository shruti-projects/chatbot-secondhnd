import streamlit as st
import openai import OpenAI
import os

# Set your OpenAI API key
client = OpenAI()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Product list (you can update this later with real products)
product_list = {
    "second-hand iPhone": "₹18,000, gently used, 64GB, good battery health",
    "engineering books": "₹500 each, set of 3, like new",
    "used laptop": "₹25,000, Intel i5, 8GB RAM, 512GB SSD",
    "scientific calculator": "₹300, Casio fx-991ES, good condition"
}

# Convert product list to a string
product_info = "\n".join([f"{item}: {details}" for item, details in product_list.items()])

# Streamlit Page Setup
st.set_page_config(page_title="Second-Hand Chatbot 🤖", layout="centered")
st.title("💬 Chat with Second-HandBot")
st.write("Ask anything about available products, prices, or negotiate with the bot!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # System prompt using product info
    system_prompt = f"""
You are a helpful chatbot for a second-hand product website.
Here are the products currently available:
{product_info}

Answer ONLY based on the above product list.
If the product is not listed, politely say: "Sorry, it's not currently listed."
"""

    # OpenAI Chat Response
    client = OpenAI()
    response = client.Chat.Completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response.choices[0].message.content

    # Show reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
