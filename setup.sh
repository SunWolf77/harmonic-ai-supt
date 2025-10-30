#!/bin/bash

# Setup script for Harmonic AI SUPT Scoring Engine

echo "🔧 Starting Harmonic AI setup..."

# Step 1: Build and start the Docker container
echo "📦 Building Docker container..."
docker-compose up --build -d

# Step 2: Wait for API to be available
sleep 5

# Step 3: Run example prompts through the scoring API
echo "🧪 Running example prompts..."

EXAMPLES_FILE="examples/prompts.jsonl"

while IFS= read -r line; do
  PROMPT=$(echo "$line" | jq -r '.prompt')
  echo -e "\nPrompt: $PROMPT"
  curl -s -X POST http://localhost:8000/score \
    -H "Content-Type: application/json" \
    -d "{\"prompt\": \"$PROMPT\"}" | jq
  sleep 1
done < "$EXAMPLES_FILE"

echo -e "\n✅ Setup complete. Harmonic API running at http://localhost:8000/score"
echo "You may now run your own prompts or integrate with your tools."
