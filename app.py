import streamlit as st
import google.generativeai as genai

# Load Gemini API key
genai.configure(api_key=st.secrets["AIzaSyDrs6eSnmwlwMCBp5dw4BNsYEydNGhqGeU"])

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="ANU AI Assistant")

st.title("🤖 ANU - AI Technology Assistant")

st.write("Ask technology questions or paste code to get explanations.")

# Session memory for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask about programming, AI, cloud, or paste code")

if prompt:

    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Detect if user pasted code
    code_prompt = f"""
    You are ANU, an AI assistant helping students and professionals.

    If the input contains code:
    - Explain the code step by step
    - Mention the programming language
    - Suggest improvements

    If it's a tech question:
    - Answer clearly and concisely.

    User input:
    {prompt}
    """

    response = model.generate_content(code_prompt)

    answer = response.text

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": answer})
