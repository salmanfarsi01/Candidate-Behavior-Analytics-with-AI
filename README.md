# Candidate Behavioral Analytics Platform

> An AI-powered mock interview observer that analyzes candidate non-verbal communication in real-time using computer vision and large language models.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=flat&logo=fastapi&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Google-FF6F00?style=flat&logo=google&logoColor=white)
![Groq](https://img.shields.io/badge/LLM-Groq%20%7C%20Llama%203.3-F55036?style=flat)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat)

---
<img width="1919" height="838" alt="image AI" src="https://github.com/user-attachments/assets/a221dfe2-a835-44bc-82f7-9910f8afbeff" />


## Overview

The Candidate Behavioral Analytics Platform is a browser-based mock interview tool that uses Google's MediaPipe framework to track face landmarks, iris position, and hand gestures in real-time. Session data is aggregated and sent to a FastAPI backend, which calls the **Llama-3.3-70b-versatile** model via Groq Cloud to generate a professional behavioral feedback report — all without exposing API credentials to the frontend.

---

## Core Features

| Feature | Description |
|---|---|
| **Real-time Face & Iris Tracking** | Measures eye contact and micro-lookaways with rolling-buffer smoothing to prevent false positives |
| **Head Pose Analysis** | Tracks yaw and pitch in degrees to monitor head stability and candidate engagement |
| **Hand Gesture Monitoring** | Detects wrist movement and fidgeting with auto-calibrated baseline per session |
| **AI Behavioral Reports** | Integrates Llama 3.3 70B via Groq to generate structured, actionable feedback |
| **Secure Backend** | API keys stored in `.env` and handled exclusively server-side via FastAPI |

---

<img width="1920" height="779" alt="image2" src="https://github.com/user-attachments/assets/969b4320-79cf-48b5-a79a-ef2e55bc5f71" />


## How It Works

This project operates in three processing layers:

### 1. Landmark Detection
The webcam feed is captured frame-by-frame and passed to two MediaPipe AI models running in the browser:
- **FaceMesh** maps 468 3D coordinates to the face, isolating eyes, irises, nose, and jaw
- **Hands** maps 21 key points per hand to track wrist articulation and movement

### 2. Geometric Normalization
Raw landmark coordinates are normalized to account for varying candidate distances from the camera. The software calculates:
- **Gaze offset** — iris position relative to the eye socket width
- **Head rotation (yaw/pitch)** — nose-to-eye midpoint ratio and ear-to-chin distances converted to degrees
- **Hand motion** — wrist displacement relative to a per-session calibrated baseline with slow drift correction

### 3. Behavioral Evaluation
Live metrics are smoothed over a rolling buffer of 10 frames to suppress jitter. Aggregated session percentages and an event log are sent to the Python backend, where the **Llama-3.3-70b-versatile** model generates a professional behavioral report.

---

<img width="316" height="950" alt="image3" src="https://github.com/user-attachments/assets/49ac65ea-6b15-48c4-bbd3-5aff21986a0c" />


## Tech Stack

```
Frontend    ->  Vanilla JavaScript, HTML5 Canvas, MediaPipe (FaceMesh + Hands)
Backend     ->  Python, FastAPI, Uvicorn
AI Vision   ->  Google MediaPipe
AI Language ->  Groq Cloud (Llama-3.3-70b-versatile)
Config      ->  python-dotenv (.env)
```

---

## Project Structure

```
your-repo-name/
|
+-- public/
|   +-- index.html        # Frontend application and computer vision logic
|
+-- main.py               # FastAPI backend - secure AI report generation
+-- .env                  # Environment variables (never commit this)
+-- .gitignore            # Ensures .env and sensitive files are excluded
+-- README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Install Python dependencies

```bash
pip install fastapi uvicorn groq python-dotenv pydantic
```

### 3. Set up environment variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=gsk_your_groq_api_key_here
```

> Get your free API key at [console.groq.com](https://console.groq.com)

### 4. Run the backend

```bash
uvicorn main:app --reload
```

### 5. Open the application

Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000)

The FastAPI server serves the frontend from `/public/index.html` and handles all LLM requests server-side.

---

## Usage

1. Click **Start camera** and allow browser camera access
2. Position yourself so your face is clearly visible in the 16:9 preview window
3. Hold your hands still for ~3 seconds while the hand baseline calibrates
4. Conduct your mock interview session - metrics update in real-time
5. Click **Stop session** when finished
6. Click **Generate AI report** to receive a behavioral feedback report from Llama 3.3

---

## Detection Thresholds

| Metric | Good | Warning | Alert |
|---|---|---|---|
| Eye gaze deviation | < 0.20 (normalized) | - | >= 0.20 |
| Head yaw | < 28 deg | 22-32 deg | > 32 deg |
| Head pitch | < 22 deg | 18-28 deg | > 28 deg |
| Hand motion | < 12 px/f | 12-35 px/f | > 35 px/f |

All values are smoothed over a 10-frame rolling buffer before thresholds are applied.

---

## Security Notes

- The Groq API key is stored exclusively in `.env` and never sent to or exposed in the frontend
- `.env` is listed in `.gitignore` - confirm it is never committed to version control
- All LLM calls are made server-side through the FastAPI backend

---

## Future Roadmap

- [ ] **Speech Analysis** - Integration of Whisper-Large-V3 for filler-word detection and speech clarity scoring
- [ ] **Session Recording** - Video replay with synchronized metric overlay
- [ ] **PDF Reports** - Downloadable candidate behavioral report with charts
- [ ] **Candidate Dashboard** - Historical session comparison and progress tracking
- [ ] **User Authentication** - Login system with per-user session database

---

## License

This project is licensed under the MIT License.

---

*Built with [MediaPipe](https://mediapipe.dev), [FastAPI](https://fastapi.tiangolo.com), and [Groq](https://groq.com)*
