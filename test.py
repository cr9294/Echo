from catch import separate_prompts
from fastapi import FastAPI, WebSocket, Response
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from sd import generate_images
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from chat import chat_with_model
from chat2 import llm

data = input("请输入文本：")
response = llm(data)
print(response)
good, bad = separate_prompts(response)
print("good:",good)
print("bad:",bad)
image_data = generate_images(good, bad)
print("image_data_done")
