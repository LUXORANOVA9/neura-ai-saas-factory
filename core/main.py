from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import asyncio
import json
from typing import Dict, List
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("NEURA")

app = FastAPI(title="NEURA by LUXORANOVA")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WebSocket connections store
connections: Dict[str, WebSocket] = {}

# Agent status store
agent_status: Dict[str, Dict] = {}

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    connections[client_id] = websocket
    try:
        while True:
            data = await websocket.receive_text()
            await broadcast_message(f"Client {client_id}: {data}")
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
    finally:
        del connections[client_id]

async def broadcast_message(message: str):
    """Broadcast message to all connected clients"""
    for connection in connections.values():
        try:
            await connection.send_text(message)
        except Exception as e:
            logger.error(f"Broadcast error: {e}")

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "NEURA by LUXORANOVA",
        "version": "1.0.0",
        "status": "operational",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "services": {
            "ollama": "running",
            "n8n": "running",
            "superagi": "running"
        },
        "timestamp": datetime.now().isoformat()
    }

@app.get("/agents")
async def list_agents():
    """List all registered agents and their status"""
    return agent_status

@app.post("/agents/{agent_id}/task")
async def create_agent_task(agent_id: str, task: Dict):
    """Create a new task for an agent"""
    # Here we would integrate with CrewAI/SuperAGI
    logger.info(f"Creating task for agent {agent_id}: {task}")
    return {
        "agent_id": agent_id,
        "task_id": "task_123",
        "status": "created",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
