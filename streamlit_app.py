
import streamlit as st
import requests
import uuid

# Define FastAPI backend URL
API_URL = "http://fastapi:9000/query"

# Page configuration
st.set_page_config(page_title="Conversational AI with phi3.5")
st.title("Conversational AI with phi3.5")

# Initialize session state for conversations and current chat
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = {}
    initial_id = str(uuid.uuid4())
    st.session_state.conversation_history[initial_id] = []
    st.session_state.current_chat = initial_id

# Initialize input handling state
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "widget" not in st.session_state:
    st.session_state.widget = ""

def on_input_change():
    st.session_state.user_input = st.session_state.widget

def on_submit():
    if st.session_state.user_input.strip():
        handle_query(st.session_state.user_input, selected_chat)
        st.session_state.widget = ""
        st.session_state.user_input = ""

def start_new_conversation():
    conversation_id = str(uuid.uuid4())
    st.session_state.conversation_history[conversation_id] = []
    st.session_state.current_chat = conversation_id
    return conversation_id

def handle_query(query, conversation_id):
    if query.strip():
        try:
            request_data = {"query": query}
            response = requests.post(API_URL, json=request_data)
            
            if response.status_code == 200:
                result = response.json()
                st.session_state.conversation_history[conversation_id].append({
                    "query": query,
                    "response": result["response"]
                })
            else:
                error_message = response.json().get("detail", "Unknown error")
                st.session_state.conversation_history[conversation_id].append({
                    "query": query,
                    "response": f"Error: {error_message}"
                })
        except Exception as e:
            st.session_state.conversation_history[conversation_id].append({
                "query": query,
                "response": f"Error connecting to the backend: {str(e)}"
            })

# Sidebar with conversation management
with st.sidebar:
    if st.button("➕ Start New Chat", key="sidebar_new_chat", 
                 help="Click to start a new conversation"):
        start_new_conversation()
        st.rerun()
    
    st.header("Your Chats")
    tabs = list(st.session_state.conversation_history.keys())
    selected_chat = st.radio(
        "Select a chat",
        options=tabs,
        format_func=lambda x: f"Chat {tabs.index(x) + 1}",
        key="chat_selector"
    )
    
    st.session_state.current_chat = selected_chat

# Main chat interface
st.subheader(f"Chat {tabs.index(selected_chat) + 1}")

# Query input and submit button
st.text_input(
    "Your Query",
    key="widget",
    on_change=on_input_change,
    label_visibility="visible"
)
st.button("Send", key=f"submit_{selected_chat}", on_click=on_submit)

# Display conversation
if selected_chat in st.session_state.conversation_history:
    messages = st.session_state.conversation_history[selected_chat]
    
    if not messages:
        st.info("No messages yet. Start a conversation by typing above!")
    else:
        chat_container = st.container()
        with chat_container:
            for msg in messages:
                st.markdown(f"**You:** {msg['query']}")
                st.markdown(f"**AI:** {msg['response']}")
                st.markdown("---")
