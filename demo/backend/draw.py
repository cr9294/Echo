import sys
import time
from PIL import Image
sys.path.append('./webuiapi')
import webuiapi

api = webuiapi.WebUIApi(host='127.0.0.1',
                        port=7860,
                        sampler='Euler a',
                        steps=20)
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