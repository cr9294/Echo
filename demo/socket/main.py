from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles  # 添加这一行
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="real"), name="static")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app='main:app',
        host="10.191.31.211",
        log_level="debug",
        port=8000,
        loop="asyncio",
        # workers=4,
    )
