import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Choix du modèle GPT via un selectbox
model_options = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-instruct",
    "gpt-3.5-turbo-1106",
    "gpt-3.5-turbo-0125"
]

selected_model = st.selectbox(
    "Choisis un modèle GPT",
    model_options,
    index=model_options.index(st.session_state.get("openai_model", "gpt-3.5-turbo"))
)

st.session_state["openai_model"] = selected_model

# Choix du nombre de jetons via un slider
max_tokens = st.slider(
    "Nombre maximum de jetons générés",
    min_value=0,
    max_value=500,
    value=200
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
            max_tokens=max_tokens,
        )
        response = st.write_stream(stream)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    stream = client.chat.completions.create(
    model=st.session_state["openai_model"],
    messages=[
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
    ],
    stream=True,
    max_tokens=max_tokens,
)

