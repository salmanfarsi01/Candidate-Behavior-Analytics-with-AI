from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

app = FastAPI()

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Define the data structure we expect from the frontend
class AnalysisRequest(BaseModel):
    eyeScore: str
    headScore: str
    handScore: str
    lookaways: int
    duration: str

@app.post("/api/analyze")
async def analyze_interview(data: AnalysisRequest):
    prompt = f"""
    You are an expert body-language and interview coach. Analyze this candidate's mock interview data:
    - Session Duration: {data.duration}
    - Eye Contact Score: {data.eyeScore}
    - Head Posture Score: {data.headScore}
    - Hand Stability Score: {data.handScore}
    - Micro-Lookaways Detected: {data.lookaways}

    Write a brief, direct evaluation. Format exactly like this:
    **The Good:**
    (Highlight what they did well regarding their eyes, head, or hands)

    **What Needs Improvement:**
    (Highlight specific areas of their body language that need work and give 1 actionable tip)
    """
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=400
        )
        return {"result": chat_completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Serve the HTML frontend
# (Make sure this is at the bottom of the file)
app.mount("/", StaticFiles(directory="public", html=True), name="public")