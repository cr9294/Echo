from catch import separate_prompts
from fastapi import FastAPI, WebSocket, Response
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from sd import generate_images
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from chat import chat_with_model
from chat2 import llm


app = FastAPI()
#http://127.0.0.1:8080/static/index.html
app.mount("/static", StaticFiles(directory="real"), name="static")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(data)
        await websocket.send_text(f"Message text was: {data}, please wait")
        try:
            #word = "Prompt: A historic scene of the founding ceremony of the People's Republic of China, the Tiananmen Square filled with a massive crowd, the red flags waving, soldiers marching in perfect formation, the silhouette of the Monument to the People's Heroes in the background, clear blue sky, traditional Chinese architecture, vibrant colors, socialist realism art style, (best quality,4k,8k,highres,masterpiece:1.2), ultra-detailed, (realistic,photorealistic,photo-realistic:1.37), HDR, UHD, studio lighting, vivid colors.Negative Prompt: nsfw, (low quality,normal quality,worst quality,jpeg artifacts), cropped, monochrome, lowres, low saturation, ((watermark)), (white letters), modern elements, western architecture, blurry, bad anatomy, disfigured, poorly drawn face, extra limb, ugly, poorly drawn hands, missing limb, floating limbs, disconnected limbs, out of focus. (For this particular theme, it's important to exclude any modern or western elements that do not fit the historical setting of the event.)"
            #response, history =chat_with_model(data)
            try:
                response = llm(data)
            except Exception as e:
                error_message = str(e)
                error_code = error_message[12:15]  # Extract error code
                if error_code == "400":
                    print("Error: 400")
                    await websocket.send_text(f"系统检测到输入或生成内容可能包含不安全或敏感内容，请您避免输入易产生敏感内容的提示语，感谢您的配合。")
                    continue
            good, bad = separate_prompts(response)
            image_data = generate_images(good, bad)
            print("image_data_done")
            #await websocket.send_text(f"{data}")
            if image_data:
                await websocket.send_bytes(image_data)
                print("send image")
            await websocket.send_text(f"AI绘图完成: {data}")
        except Exception as e:
            print(f"Error: {e}")
            await websocket.send_text(f"Error:{e}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app='main:app',
        #host="10.0.8.16",
        #host="111.230.70.21",
        host="127.0.0.1",
        #host="0.0.0.0",
        log_level="debug",
        port=8088,
        loop="asyncio",
        reload=True,
    )

