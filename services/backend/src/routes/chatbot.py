from typing import List
from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from fastapi.responses import HTMLResponse
from starlette.responses import JSONResponse

from ..schemas.chatbot import ChatDTO
from ..contents.chatbot.chat_test import chat_test

router = APIRouter()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://flussberg.shop/chatbot/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@router.get("/")
async def get():
    return HTMLResponse(html)


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    print("### 웹소켓 연결 ###")
    try:
        while True:
            print("### 1 ###")
            data = await websocket.receive_text()
            print("### 2 ###")
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            print("### 3 ###")
            response = chat_test(data)
            print("### 4 ###")
            await manager.broadcast(f"Chatbot says: {response}")
            print("### 5 ###")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")


@router.post("/test")
async def chatbot_test(dto: ChatDTO):
    message = dto.dict()["message"]
    print(f"##### message : {message} ##### ")
    print(f"##### message type : {type(message)} ##### ")
    response = chat_test(message)
    print(f"##### response : {response} ##### ")
    dict = {"response": response}
    return JSONResponse(content=dict, status_code=200)

@router.post("/korean")
async def chatbot_test(dto: ChatDTO):
    message = dto.dict()["message"]
    print(f"##### message : {message} ##### ")
    print(f"##### message type : {type(message)} ##### ")
    response = message
    print(f"##### response : {response} ##### ")
    dict = {"response": response}
    return JSONResponse(content=dict, status_code=200)
