import streamlit as st
import openai

# Optional: You can paste your API key here or store it securely
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Second-Hand Chatbot 💬", layout="centered")
st.title("🤖 Chat with Second-HandBot")
st.write("Ask anything about available products, prices, or negotiate with the bot!")

# Chat history storage
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your question here...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # OpenAI response
    with st.chat_message("assistant"):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message["content"]
        st.markdown(reply)

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": reply})