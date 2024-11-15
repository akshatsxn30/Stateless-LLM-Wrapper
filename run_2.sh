#!/bin/bash

# Step 1: Run 'ollama serve' in the background and sleep for 10 seconds
ollama serve &
echo "Starting ollama serve..."
sleep 10

# Step 2: Pull the phi3.5 model and wait until it's ready
echo "Pulling phi3.5 model. This may take some time..."
ollama pull phi3.5

# Check if the pull was successful
if [ $? -eq 0 ]; then
    echo "phi3.5 available for use"
else
    echo "Failed to pull phi3.5 model"
fi
