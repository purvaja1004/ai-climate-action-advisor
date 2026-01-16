# AI Climate Action Advisor\n\n
1. A small capstone project aligned with SDG 13 (Climate Action).\nThis app accepts a user's daily activity (natural language), classifies it,\nanalyzes environmental impact, and returns concise suggestions.\n\n## Project structure\n- `agent.py` → LangGraph-style AI agent that calls Google Generative AI (Gemini) or uses a fallback\n- `backend.py` → Flask API that exposes `/analyze` and serves the frontend\n- `frontend/` → `index.html`, `style.css`, `script.js`\n- `requirements.txt` → Python dependencies\n\n## Setup (Windows PowerShell)\n1. Create and activate a virtual environment:\n
```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:\n
```powershell
pip install -r requirements.txt
```

3. (Optional) To enable real Gemini calls, set your Google API key as an environment variable:\n
```powershell
$env:GOOGLE_API_KEY = "AIzaSyBVSFTvimg4FgNfnoWUUweQdaE_QQVhs5Q"
```

4. Run the Flask backend:\n
```powershell
python backend.py
```


5. Open your browser to `http://127.0.0.1:5000/` and try the UI.\n\n## Notes\n- If you do not provide `GOOGLE_API_KEY` or the `google-generativeai` package is not installed, the agent uses a deterministic fallback to keep demos working offline.\n- Responses are intentionally concise (max ~5 lines).\n- For production or real billing usage, ensure you configure Google Cloud credentials and use approved SDK patterns.\n\n## Ethical usage\n- Keep user data private; do not send sensitive personal information to the LLM.\n- Use the tool to guide sustainable behavior, avoid judgemental or shaming language.\n
