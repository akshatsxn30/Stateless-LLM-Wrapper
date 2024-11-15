from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# from typing import List
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import subprocess
import os
from contextlib import asynccontextmanager

app = FastAPI(title="LangChain API with Phi-3.5", version="1.0.0")

# Define request and response models
class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str

# Initialize ChatOllama model with desired configuration
llm = ChatOllama(
    model="phi3.5",
    temperature=0,
)

# Define the prompt template using LangChain
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that answers questions based on the given query.",
        ),
        ("human", "{query}"),
    ]
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup tasks
    script_path = "./run_2.sh"
    os.chmod(script_path, 0o755)  # Set executable permissions

    try:
        subprocess.run([script_path], check=True)
        print("run_2.sh executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute run_2.sh: {e}")

    yield  # FastAPI will continue to run the application after this point

    # Shutdown tasks (if any) can go here

app = FastAPI(lifespan=lifespan)

@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    try:
        # Prepare the prompt for input
        prompt_text = {
            "query": request.query
        }

        # Invoke the model with the prepared prompt
        response_text = prompt | llm
        ai_response = response_text.invoke(prompt_text)
        final_ans = ai_response.content
        return QueryResponse(response=final_ans)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing query: {str(e)}"
        )

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "python_version": "3.11",
        "model": "phi3.5",
        "backend": "ollama"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)

