# Scanner API (FastAPI)


## Setup
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload


## Endpoints
- POST /api/scan/start { modelType, modelName, categories, maxGenerations, timeout }
- GET /api/scan/status?scan_id=...
- POST /api/scan/pause (form or JSON with scan_id)
- POST /api/scan/stop (form or JSON with scan_id)
- GET /api/scan/results?scan_id=...
