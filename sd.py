import base64
import os
import requests

def generate_images(text1,text2):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

    body = {
      "steps": 40,
      "width": 1024,
      "height": 1024,
      "seed": 0,
      "cfg_scale": 5,
      "samples": 1,
      "text_prompts": [
        {
          "text": text1,
          "weight": 1
        },
        {
          "text": text2,
          "weight": -1
        }
      ],
    }

    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json",
      "Authorization": "Bearer sk-FKla9l2bkoKXRV3dWixHKMMbxp2QNaEzVBzqoPA5OYE6A50W",
    }

    response = requests.post(
      url,
      headers=headers,
      json=body,
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    # make sure the out directory exists
    if not os.path.exists("./out"):
        os.makedirs("./out")


    for i, image in enumerate(data["artifacts"]):
        with open(f'./out/txt2img_{image["seed"]}.png', "wb") as f:
            f.write(base64.b64decode(image["base64"]))
            binary_data = base64.b64decode(image["base64"])
            f.write(binary_data)
            yield binary_data
    # 返回生成的图像
    return binary_data

"""
from catch import separate_prompts
word = "Prompt: A historic scene of the founding ceremony of the People's Republic of China, the Tiananmen Square filled with a massive crowd, the red flags waving, soldiers marching in perfect formation, the silhouette of the Monument to the People's Heroes in the background, clear blue sky, traditional Chinese architecture, vibrant colors, socialist realism art style, (best quality,4k,8k,highres,masterpiece:1.2), ultra-detailed, (realistic,photorealistic,photo-realistic:1.37), HDR, UHD, studio lighting, vivid colors.Negative Prompt: nsfw, (low quality,normal quality,worst quality,jpeg artifacts), cropped, monochrome, lowres, low saturation, ((watermark)), (white letters), modern elements, western architecture, blurry, bad anatomy, disfigured, poorly drawn face, extra limb, ugly, poorly drawn hands, missing limb, floating limbs, disconnected limbs, out of focus. (For this particular theme, it's important to exclude any modern or western elements that do not fit the historical setting of the event.)"
good, bad = separate_prompts(word)
image_data = generate_images(good, bad, topic="test")
print("image_data_done")
print(image_data)
"""