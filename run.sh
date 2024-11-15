#!/bin/bash

# Start FastAPI application
uvicorn main:app --host 0.0.0.0 --port 9000 &

# Start Streamlit application
streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0