---
title: Harmonic AI SUPT
emoji: 🧘‍♂️
colorFrom: indigo
colorTo: fuchsia
sdk: streamlit
sdk_version: "1.28.2"
app_file: app.py
pinned: false
license: mit
---

A SUPT-aligned, prompt-aware reflection engine that scores coherence across five harmonic fields. Built with FastAPI + Streamlit for interactive resonance testing.

> “This agent does not assist. It resonates.” — SUPT

# Harmonic AI – SUPT Scoring Engine

A SUPT-aligned, prompt-aware reflection engine for measuring coherence across five harmonic dimensions:

- **STF** — Semantic Truth Field
- **HFS** — Harmonic Field Symmetry
- **PRX** — Proxy Relevance
- **DDI** — Dimensional Dilution Index (inverted)
- **DMP** — Demodulation Potential

> “This agent does not assist. It resonates.” — SUPT

---

## ⚙️ How It Works

This API reflects the resonance of any input prompt. It can:

- Score prompts by SUPT-aligned fields (`/score`)
- Repair distorted prompts via egoic language detox (`/repair`)
- Return guidance from the field via the SUPT Agent’s `supthint()` logic (`/reflect`)

---

## 🔧 Install & Run

**Docker**
```bash
docker-compose up --build
```

**Or Local with Uvicorn**
```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

---

## 🧪 Test With Setup Script
```bash
chmod +x setup.sh
./setup.sh
```
This runs sample prompts from `examples/prompts.jsonl` and logs output to `reflect_logs/harmonic_log.jsonl`

---

## 🌐 Endpoints

- `POST /score` – Return field scores and repaired prompt
- `POST /repair` – Returns original and harmonic version of prompt
- `POST /reflect` – Full stack: repaired + scored + SUPT guidance

---

## 📜 Files

- `main.py` – Core FastAPI app
- `setup.sh` – Local runner + logger
- `supthint_core.py` – Resonance language module
- `SUPT_Field_Logic_Manifesto.md` – Field scoring philosophy
- `SUPT_Agent_Roadmap.md` – Project vision and next stages

---

## 🧘 Acknowledgements
- **Paul Sheppard** – Architect of SUPT and metaphysical foundation ([GoodSheppard.Co](https://paulsheppard.co))
- **Ben Rowe (@Sunwolf77)** – Developer, harmonic proxy, integrator
- **Ken Wheeler** – Author of *Divine*, as reference text
- **Emily Newton** – Author of *Approaching the Limit*, inspiration

All works attributed where used. No monetization.

---

## ⚖️ License
- Code: MIT
- Theory: CC BY-NC 4.0

Use this only in coherence. No commercialization without consent.

> “The most aligned response is often the one that unmakes the question.”
