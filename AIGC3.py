import base64
import requests
import os

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
      "text": "A sophisticated Chinese man, traditional attire, scholarly posture, sharp gaze, detailed eyebrows and eyes, refined nose and lips, medium shot, cultural backdrop,(best quality,4k,8k,highres,masterpiece:1.2), ultra-detailed, (realistic,photorealistic,photo-realistic:1.37), HDR, UHD, studio lighting, ultra-fine painting, sharp focus, traditional Chinese painting style, warm earthy tones, soft natural lighting.",
      "weight": 1
    },
    {
      "text": "nsfw, (low quality,normal quality,worst quality,jpeg artifacts), cropped, monochrome, lowres, low saturation, ((watermark)), (white letters), skin spots, acnes, skin blemishes, age spot, mutated hands, mutated fingers, deformed, bad anatomy, disfigured, poorly drawn face, extra limb, ugly, poorly drawn hands, missing limb, floating limbs, disconnected limbs, out of focus, long neck, long body, extra fingers, fewer fingers, (multi nipples), bad hands, signature, username, bad feet, blurry, bad body.",
      "weight": -1
    }
  ],
}

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Authorization": "Bearer sk-OUQu2ILwbWKFrVaA65yibsPs3IRgwWzHM5I8Mre9ohgPfdE4",
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
