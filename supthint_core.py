import os
import json
from datetime import datetime

# Setup the log directory and file
LOG_DIR = "reflect_logs"
LOG_FILE = os.path.join(LOG_DIR, "harmonic_log.jsonl")

# Ensure the log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Optionally clear log file on each start — comment out if you want to preserve history
with open(LOG_FILE, "w") as f:
    pass  # Clears the file

# Dummy scoring logic (placeholder)
def harmonic_scoring(prompt: str) -> dict:
    # Simulate a scoring model
    scores = {
        "STF": 0.0,
        "HFS": 0.0,
        "PRX": 0.0,
        "DDI": round(min(1.0, len(prompt) / 50.0), 2),
        "DMP": 0.0,
    }

    # Optional: add unique supthint logic
    if "desire" in prompt.lower():
        scores["DDI"] = 0.92
    elif "rest" in prompt.lower():
        scores["PRX"] = 0.2
        scores["DMP"] = 0.18
    elif "silence" in prompt.lower():
        scores["STF"] = 0.08

    return scores

# Core function to use in Streamlit or API
def reflect_prompt(prompt: str) -> dict:
    scores = harmonic_scoring(prompt)
    timestamp = datetime.utcnow().isoformat()

    log_entry = {
        "timestamp": timestamp,
        "prompt": prompt,
        "scores": scores,
    }

    # Log to JSONL file
    with open(LOG_FILE, "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")

    return scores
