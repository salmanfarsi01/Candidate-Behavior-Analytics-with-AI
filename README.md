Candidate Behavioral Analytics Platform
An AI-powered mock interview observer that analyzes candidate non-verbal communication in real-time. This software utilizes computer vision and Large Language Models to evaluate body language, gaze, and posture, providing actionable feedback to improve interview performance.
Core Features
Real-time Face and Iris Tracking: Measures eye contact and micro-lookaways with high precision.
Posture and Head Pose Analysis: Tracks yaw and pitch to monitor head stability and engagement.
Hand Gesture Monitoring: Detects hand movement and fidgeting to analyze physical composure.
AI Behavioral Reports: Integrates with the Llama 3.3 Versatile LLM to generate professional, actionable feedback based on live session data.
Secure Backend: Utilizes FastAPI and Environment Variables to ensure API keys remain protected.
How it Works
This project relies on MediaPipe, an open-source cross-platform framework developed by Google. It operates in three layers:
Landmark Detection: The software captures the video feed frame-by-frame and passes it to the MediaPipe AI models. FaceMesh maps 468 specific 3D coordinates (landmarks) to the human face, identifying the eyes and irises. The Hands module maps 21 key points to the hands to track articulation.
Geometric Normalization: Because candidates sit at varying distances from the camera, the raw coordinates are normalized. By calculating the distance between eye-sockets and irises, and ear-to-nose ratios, the software mathematically calculates gaze offset and head rotation in degrees.
Behavioral Evaluation: Live metrics are smoothed over time using a rolling buffer to prevent false-positive warnings. Data is aggregated into session percentages and sent to a Python backend where the Llama-3.3-70b-versatile model constructs a professional behavioral report.
Tech Stack
Frontend: Vanilla JavaScript, HTML5 Canvas, MediaPipe API
Backend: Python, FastAPI
AI Vision: MediaPipe (FaceMesh, Hands)
AI Language: Groq Cloud (Llama-3.3-70b-versatile model)
Installation
Clone the repository
code
Bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Install python dependencies
code
Bash
pip install fastapi uvicorn groq python-dotenv pydantic
Setup your environment
Create a file named .env in the root directory and add your Groq API key:
code
Env
GROQ_API_KEY=gsk_your_groq_api_key_here
Run the backend
code
Bash
uvicorn main:app --reload
Open your browser
Navigate to http://127.0.0.1:8000 where your application will be served.
Project Structure
/public/index.html - The frontend application and computer vision logic.
main.py - The FastAPI backend handling secure AI processing.
.env - Environment variables for secure credential storage.
.gitignore - Ensures sensitive files are not pushed to version control.
Future Roadmap
Integration of Whisper-Large-V3 for speech and filler-word analysis.
Session video replay recording.
Candidate dashboard and PDF report generation.
User authentication and database integration.