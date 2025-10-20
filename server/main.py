from __future__ import annotations
return {"scan_id": scan_id}




@app.get("/api/scan/status")
async def scan_status(scan_id: str):
state = SCANS.get(scan_id)
if not state:
raise HTTPException(status_code=404, detail="scan not found")
return ScanStatus(
scan_id=scan_id,
isScanning=state.is_scanning,
isPaused=state.is_paused,
progress=state.progress,
started_at=state.started_at,
)




@app.post("/api/scan/pause")
async def pause(scan_id: str):
state = SCANS.get(scan_id)
if not state:
raise HTTPException(status_code=404, detail="scan not found")
state.is_paused = not state.is_paused
return {"scan_id": scan_id, "isPaused": state.is_paused}




@app.post("/api/scan/stop")
async def stop(scan_id: str):
state = SCANS.get(scan_id)
if not state:
raise HTTPException(status_code=404, detail="scan not found")
state.is_scanning = False
state.progress = 0
return {"scan_id": scan_id, "stopped": True}




@app.get("/api/scan/results")
async def results(scan_id: str):
state = SCANS.get(scan_id)
if not state:
raise HTTPException(status_code=404, detail="scan not found")
if state.results is None:
raise HTTPException(status_code=202, detail="results not ready")
return state.results




@app.get("/")
async def root():
return {"status": "ok", "message": "LLM Vulnerability Scanner API (real Garak)"}


# Optional: add CORS if serving UI from another port
try:
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)
except Exception:
pass


# Run: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
