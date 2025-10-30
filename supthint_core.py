#!/bin/bash

# Setup script for Harmonic AI SUPT Scoring Engine with /reflect logging

LOG_FILE="reflect_logs/harmonic_log.jsonl"
mkdir -p reflect_logs
> "$LOG_FILE"

echo "🔧 Starting Harmonic AI setup..."

# Step 1: Build and start the Docker container
echo "📦 Building Docker container..."
docker-compose up --build -d

# Step 2: Wait for API to be available
sleep 5

# Step 3: Run example prompts through the full reflection API
echo "🧪 Running example prompts with repair + scores + supthint..."

EXAMPLES_FILE="examples/prompts.jsonl"

while IFS= read -r line; do
  PROMPT=$(echo "$line" | jq -r '.prompt')
  echo -e "\n📝 Original Prompt: $PROMPT"

  RESPONSE=$(curl -s -X POST http://localhost:8000/reflect \
    -H "Content-Type: application/json" \
    -d "{\"prompt\": \"$PROMPT\"}")

  echo "$RESPONSE" | jq
  echo "$RESPONSE" >> "$LOG_FILE"

  sleep 1
done < "$EXAMPLES_FILE"

echo -e "\n✅ Setup complete. Harmonic Agent active at:"
echo "  - /score for raw scoring"
echo "  - /repair for prompt detox"
echo "  - /reflect for full agent guidance"
echo "📜 Log written to $LOG_FILE"

echo "🧠 Local entrypoint: main.py"
echo "Run locally with: uvicorn main:app --reload"
