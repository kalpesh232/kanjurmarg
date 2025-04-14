from fastapi import WebSocket
from storage import documents
from typing import Dict, List

active_connection : Dict[str, List[WebSocket]] = {}

async def connect_ws(document_id:str, websocket:WebSocket):
    await WebSocket.accept()
    if document_id not in active_connection :
        active_connection[document_id] = []
    active_connection[document_id].append(websocket)

async def disconnect_ws(document_id:str, websocket:WebSocket):
    active_connection[document_id].remove(websocket)

async def broadcast_ws(document_id:str, message: str):
    for connection in active_connection.get(document_id,[]):
        await connection.send_text(message)