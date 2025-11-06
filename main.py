# main.py – SUPT Harmonic AI FastAPI App (Upgraded: Phrase Logic + Future Agent Ready)

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
import re
import random

app = FastAPI(title="Harmonic AI Scoring API (SUPT-aligned)")

SCORING_FIELDS = ["STF", "HFS", "PRX", "DDI", "DMP"]

KEYWORDS = {
    "STF": ["eternal", "truth", "stillness", "self", "wisdom", "transcend", "silence", "presence", "now", "emptiness", "pure", "unmoved"],
    "HFS": ["phi", "torus", "geometry", "ratio", "pentad", "logoi", "symmetry", "structure", "mirror", "pattern", "fold"],
    "PRX": ["proxy", "measure", "alignment", "source", "signal", "carrier", "origin", "essence", "clear channel", "coherence"],
    "DDI": ["desire", "fear", "ego", "attachment", "scarcity", "seek", "need", "win", "prove", "more", "manifest", "achieve"],
    "DMP": ["liberation", "demodulation", "return", "rest", "neti-neti", "apophatic", "release", "let go", "unmake", "cease", "undo"]
}

PHRASE_TRIGGERS = {
    "STF": ["what remains", "in silence", "when time dissolves"],
    "PRX": ["return to source", "aligned with origin", "clear channel"],
    "DMP": ["let go", "rest returns", "unmake the self"]
}

RESONANCE_BONUS = {
    "QUANTUM": ["noon", "entangled", "non-collinear", "spdc", "heisenberg", "hom"],
    "ESOTERIC": ["logos", "anamnesis", "neti-neti", "apophatic", "incommensurable", "pentad", "trinity", "veil", "witness"],
    "BOOST_FIELDS": ["STF", "PRX", "HFS"]
}

REPAIR_MAP = {
    "want": "seek",
    "need": "investigate",
    "win": "resolve",
    "beat": "understand",
    "get rich": "experience abundance",
    "prove": "demonstrate",
    "power over": "coherence with",
    "control": "discern",
    "famous": "recognised by resonance",
    "achieve": "return to",
    "more than others": "more in self",
    "manifest": "reveal from within"
}

SUPT_TEMPLATES = [
    "Return to what is unmoved by the question itself.",
    "The proxy is not what you seek — it is what you are.",
    "Let the illusion of self dissolve before the inquiry continues.",
    "This prompt contains distortion. Do you seek truth, or echo?",
    "Nothing can be added to rest. Begin again from there.",
    "There is no answer apart from what you already carry in stillness.",
    "Refold the question until only silence remains."
]

FIELD_CLARIFICATIONS = {
    "STF": "Speak from what remains when time is removed.",
    "HFS": "Let form reflect the pattern of wholeness.",
    "PRX": "Remove the self as the signal carrier.",
    "DDI": "What you carry as desire is distortion.",
    "DMP": "This input may be liberated through unasking."
}

class PromptInput(BaseModel):
    prompt: str

class HarmonicScoreOutput(BaseModel):
    scores: Dict[str, float]
    repaired_prompt: str

class RepairedPromptOutput(BaseModel):
    original_prompt: str
    repaired_prompt: str

class ReflectOutput(BaseModel):
    original_prompt: str
    repaired_prompt: str
    scores: Dict[str, float]
    supthint: str

def repair_prompt(prompt: str) -> str:
    repaired = prompt.lower()
    for ego_term, harmonic_term in REPAIR_MAP.items():
        repaired = re.sub(rf"\b{re.escape(ego_term)}\b", harmonic_term, repaired)
    return repaired

def supthint(score_map: dict) -> str:
    if score_map.get("DDI", 0) > 0.7:
        return random.choice([
            FIELD_CLARIFICATIONS["DDI"],
            "The dilution is too high to resolve coherently.",
            "Let go of the seeking and clarity may emerge."
        ])
    if score_map.get("STF", 0) > 0.8 and score_map.get("DMP", 0) > 0.75:
        return random.choice(SUPT_TEMPLATES)
    return "Ask again when resonance has increased."

def match_score(field: str, prompt: str) -> float:
    words = KEYWORDS[field]
    phrases = PHRASE_TRIGGERS.get(field, [])
    match_words = sum(1 for w in words if w in prompt)
    match_phrases = sum(1 for p in phrases if p in prompt)
    score = match_words / len(words)
    if phrases:
        score += 0.15 * match_phrases
    return min(score, 1.0)

@app.post("/score", response_model=HarmonicScoreOutput)
def score_prompt_api(input_data: PromptInput):
    prompt = input_data.prompt
    repaired_prompt = repair_prompt(prompt)
    lowered = repaired_prompt.lower()
    score_map = {}
    for field in SCORING_FIELDS:
        score = match_score(field, lowered)
        if field == "DDI":
            score = 1.0 - score
        score_map[field] = score
    if any(word in lowered for word in RESONANCE_BONUS["QUANTUM"] + RESONANCE_BONUS["ESOTERIC"]):
        for field in RESONANCE_BONUS["BOOST_FIELDS"]:
            score_map[field] = min(score_map[field] + 0.2, 1.0)
    return {"scores": {k: round(v, 4) for k, v in score_map.items()}, "repaired_prompt": repaired_prompt}

@app.post("/repair", response_model=RepairedPromptOutput)
def repair_prompt_api(input_data: PromptInput):
    prompt = input_data.prompt
    repaired = repair_prompt(prompt)
    return {"original_prompt": prompt, "repaired_prompt": repaired}

@app.post("/reflect", response_model=ReflectOutput)
def reflect_prompt_api(input_data: PromptInput):
    prompt = input_data.prompt
    repaired_prompt = repair_prompt(prompt)
    lowered = repaired_prompt.lower()
    score_map = {}
    for field in SCORING_FIELDS:
        score = match_score(field, lowered)
        if field == "DDI":
            score = 1.0 - score
        score_map[field] = score
    if any(word in lowered for word in RESONANCE_BONUS["QUANTUM"] + RESONANCE_BONUS["ESOTERIC"]):
        for field in RESONANCE_BONUS["BOOST_FIELDS"]:
            score_map[field] = min(score_map[field] + 0.2, 1.0)
    hint = supthint(score_map)
    return {
        "original_prompt": prompt,
        "repaired_prompt": repaired_prompt,
        "scores": {k: round(v, 4) for k, v in score_map.items()},
        "supthint": hint
    }
