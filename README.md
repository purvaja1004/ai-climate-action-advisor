# AI Climate Action Advisor
 A small capstone project aligned with SDG 13 (Climate Action).
   This app accepts a user's daily activity (natural language), classifies it, analyzes environmental impact, and returns concise suggestions.
    Project structure\n- `agent.py` → LangGraph-style AI agent that calls Google Generative AI (Gemini) or uses a fallback\n- `backend.py` → Flask API that exposes `/analyze` and serves the frontend\n- `frontend/` → `index.html`, `style.css`, `script.js`\n- `requirements.txt` → Python dependencies
