# ✨ Real-Time Collaborative Text Editor with AI Suggestions

A simple FastAPI-based real-time collaborative text editor that supports:
- Live document collaboration via WebSocket
- AI-generated writing suggestions while typing

> ⚠️ This version does **not include any database integration**. All edits are stored in memory and lost on restart.

---

## 🚀 Features

- Real-time multi-user editing using WebSockets
- Instant AI suggestions as you type (using `/suggest` endpoint)
- Lightweight frontend with vanilla HTML + JavaScript
- Powered by FastAPI + WebSockets

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

4. Run the application
bash
Copy
Edit
uvicorn app.main:app --reload
🌐 Access the App
Once the server is running, open your browser and go to:

arduino
Copy
Edit
http://localhost:8000
You’ll see a text editor where multiple users can collaborate in real-time.

🧠 AI Suggestions
As you type, the app sends your input to /suggest via AJAX and returns writing suggestions using a basic language model or rule (customizable).

📁 Project Structure
csharp
Copy
Edit
app/
├── main.py         # FastAPI app entry point
├── routes.py       # WebSocket + suggestion logic
├── templates/
│   └── editor.html # Frontend HTML editor
├── static/
│   └── script.js   # JavaScript logic (WebSocket + suggestions)
└── utils.py        # Suggestion helper function
✅ TODO / Future Improvements
Add persistent storage (SQLite/PostgreSQL)

Track document version history

Implement authentication

Improve AI suggestions (e.g. GPT-based)

