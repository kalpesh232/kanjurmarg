from fastapi import HTTPException, WebSocket, FastAPI, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4
from models import Document
from storage import documents
from websocket_handler import connect_ws, disconnect_ws, broadcast_ws

app = FastAPI()

documents = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/documents")
def create_document():
    doc_id = str(uuid4())
    documents[doc_id] = ""
    return {"id" : doc_id}

@app.get("/documents/{doc_id}")
def get_document(doc_id:str):
    if doc_id not in documents:
        raise HTTPException(status_code=404, detail="Document Not Found")
    return {"id" : doc_id, "content" : documents[doc_id]}


@app.websocket("/ws/documents/{document_id}")
async def websocket_endpoint(websocket: WebSocket, document_id: str):
    # Accept the WebSocket connection
    await websocket.accept()

    try:
        # Initialize the document if it does not exist
        if document_id not in documents:
            documents[document_id] = ""

        # Loop to keep receiving messages
        while True:
            # Receive a message (document content in this case)
            data = await websocket.receive_text()

            # Store or update the document in the in-memory store
            documents[document_id] = data  # Update document content

            # Send the updated content back to the client
            await websocket.send_text(documents[document_id])  # Send back the actual document content
    
    except WebSocketDisconnect:
        # Handle WebSocket disconnect
        print(f"Client disconnected from document {document_id}")