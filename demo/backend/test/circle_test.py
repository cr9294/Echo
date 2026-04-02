import sys
import time
from PIL import Image
sys.path.append('./webuiapi')
import webuiapi

api = webuiapi.WebUIApi(host='127.0.0.1',
                        port=7860,
                        sampler='Euler a',
                        steps=20)

def run_api():
    try:
        result = api.txt2img(prompt="cute squirrel",
                             negative_prompt="ugly, out of frame",
                             styles=["anime"],
                             cfg_scale=7)
        result.image.save("generated_image_api.png")  # 保存生成的图片
        result.image.show()
        return True  # 如果执行成功，返回 True
    except Exception as e:
        print(f"Error: {e}")
        return False  # 如果执行失败，返回 False

while not run_api():  # 当 run_api() 返回 False 时循环执行
    time.sleep(1)  # 每次执行失败后等待一秒再尝试
print("API 执行成功")


def run_circle(prompt, negative_prompt):
    try:
        result = api.txt2img(prompt=prompt,
                             negative_prompt=negative_prompt,
                             styles=["anime"],
                             cfg_scale=7)
        result.image.save(f"generated_image_{prompt}.png")  # 保存生成的图片，文件名包含 prompt
        result.image.show()
        return True  # 如果执行成功，返回 True
    except Exception as e:
        print(f"Error: {e}")
        return False  # 如果执行失败，返回 False

while True:
    prompt = input("请输入 prompt：")
    stop = input("是否停止循环？（输入 'yes' 以停止循环）：")
    if stop == "yes":
        print("停止循环")
        break
    negative_prompt = input("请输入 negative_prompt：")
    if not run_circle(prompt=prompt, negative_prompt=negative_prompt):
        time.sleep(1)  # 每次执行失败后等待一秒再尝试



