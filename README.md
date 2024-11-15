# Stateless-LLM-Wrapper

A software wrapper that integrates a base Language Model (LLM) with LangChain to provide enhanced reasoning capabilities, focusing on real-time interactions without maintaining conversation history.

This project implements a conversational AI chatbot using the phi3.5 model from Ollama, with FastAPI as the backend API and Streamlit as the frontend for user interaction. It integrates with LangChain to enable prompt templates and a modular chatbot design.

Features

1. Conversational AI: Powered by the phi3.5 model.
2. FastAPI Backend: Provides an API for interacting with the model.
3. Streamlit UI: A user-friendly interface to chat with the model.
4. Dockerized Setup: All components run seamlessly using Docker Compose.

Tech Stack

1. Model: Phi3.5 (Ollama)
2. Backend Framework: FastAPI
3. Frontend UI: Streamlit
4. LangChain Integration: For prompt templates and conversation design.
5. Containerization: Docker and Docker Compose for easy deployment.

Requirements
System Requirements

1. Docker
2. Docker Compose

Setup

1. Clone the Repository
   git clone https://github.com/akshatsxn30/Stateless-LLM-Wrapper.git  
   cd Stateless-LLM-Wrapper

2. Run the Application Using Docker Compose
   docker-compose up --build

3. Access the Application
   Streamlit UI: Navigate to http://localhost:8501 to chat with the model.
   FastAPI Docs: Visit http://localhost:8000/docs for the API documentation.

Project Structure

├── streamlit_app.py # Streamlit UI for chatbot interaction.  
 ├── main.py # FastAPI backend application.  
 ├── Dockerfile # Dockerfile for building the app image.  
 ├── docker-compose.yml # Docker Compose configuration.  
 ├── requirements.txt # Python dependencies.  
 ├── README.md # Project documentation.

Usage

Interacting with the Chatbot

1. Open the Streamlit UI at http://localhost:8501.
2. Enter your query in the text box and receive a response powered by the phi3.5 model.

API Access
The backend provides an API to interact with the chatbot programmatically.

1. Endpoint: POST /query
2. Example Request:
   {  
    "query": "Hi how are you?"  
   }
3. Example Response:
   {  
    "response": "I'm Phi, an artificial intelligence, so I don't have feelings, but I'm fully operational and ready to assist you! How can I help you today?"  
   }

Docker Configuration
Docker Compose Services 1. phi3.5 Model Service: Runs the Ollama model on port 12341. 2. FastAPI Service: Handles backend API requests on port 8000. 3. Streamlit Service: Frontend UI on port 8501.

Dockerfile 1. The Dockerfile is configured to set up the application with the required dependencies.

API Documentation
FastAPI automatically generates API documentation. Visit:

    1. Swagger UI: http://localhost:8000/docs
    2. ReDoc: http://localhost:8000/redoc

Future Enhancements

1. Add advanced conversation handling using LangChain tools.
2. extend the chatbot functionality with custom prompts and RAG framework for fetching results to personalised documents.
3. Integrate authentication for API endpoints
