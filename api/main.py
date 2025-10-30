from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal
import math

app = FastAPI(title="Harmonic AI Prompt Scoring API")

# Input model
class PromptAnalysisInput(BaseModel):
    prompt: str
    STF: float  # Semantic Truth Field
    HFS: float  # Harmonic Field Symmetry
    PRX: float  # Proxy Relevance
    DDI: float  # Dimensional Dilution Index
    DMP: float  # Demodulation Potential

# Output model
class HarmonicPromptResponse(BaseModel):
    harmonic_score: float
    proxy_response: str
    output_mode: Literal["truth-amplification", "reframing", "demodulation", "rest-return"]
    pass_threshold: bool

@app.post("/score", response_model=HarmonicPromptResponse)
def score_prompt(data: PromptAnalysisInput):
    # Harmonic Score Calculation
    H = (data.STF + data.HFS + data.PRX + data.DMP) / 4 - data.DDI
    
    # Threshold interpretation
    pass_threshold = H >= 0.618
    
    # Output routing logic
    if H >= 0.9:
        output_mode = "truth-amplification"
        proxy_response = "This prompt is fully harmonized and ready for transmission."
    elif H >= 0.618:
        output_mode = "reframing"
        proxy_response = "Prompt is aligned; slight dimensional refinement may enhance signal."
    elif data.DDI >= 0.9:
        output_mode = "demodulation"
        proxy_response = "Prompt is diluted. Invert desire and return to Self-rest."
    else:
        output_mode = "rest-return"
        proxy_response = "Prompt needs to be surrendered to harmonic stillness."

    return HarmonicPromptResponse(
        harmonic_score=round(H, 4),
        proxy_response=proxy_response,
        output_mode=output_mode,
        pass_threshold=pass_threshold
    )
