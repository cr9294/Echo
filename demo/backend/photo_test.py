import sys
#定位draw.py的位置
from fastapi import FastAPI, WebSocket, Response
import time
import sys
import time
from PIL import Image
sys.path.append('./webuiapi')
import webuiapi
import io

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
        result.image.save(f"generated_image_{prompt[:4]}.png")  # 保存生成的图片，文件名包含 prompt
        result.image.show()
        image_io = io.BytesIO()
        result.image.save(image_io, format='PNG')
        image_io.seek(0)
        return image_io.getvalue()  # 返回生成的图片数据
    except Exception as e:
        print(f"Error: {e}")
        return None  # 如果执行失败，返回 False

# 大模型处理部分
from zhipuai import ZhipuAI

# Initialize the client with your API key
client = ZhipuAI(api_key="52e1eea980cc94323947ca884ebf70df.hDy4Xh87ghlBpkQD") # Replace with your actual API Key


def llm(word):
# Define the topic for the completion
    try:
        topic = str(word)
        response = client.chat.completions.create(
            model="glm-4",
            messages=[
                {
                    "role": "assistant",
                    "content": (
                    "Prompt技巧：Stable Diffusion prompt 助理你来充当一位有艺术气息的Stable Diffusion prompt 助理。"
                    "任务我用自然语言告诉你要生成的prompt的主题，你的任务是根据这个主题想象一幅完整的画面，然后转化成一份详细的、高质量的prompt，让Stable Diffusion可以生成高质量的图像。"
                    "背景介绍Stable Diffusion是一款利用深度学习的文生图模型，支持通过使用 prompt 来产生新的图像，描述要包含或省略的元素。"
                    "prompt 概念完整的prompt包含“Prompt:”和\"Negative Prompt:\"两部分。prompt 用来描述图像，由普通常见的单词构成，使用英文半角\",\"做为分隔符。negative prompt用来描述你不想在生成的图像中出现的内容。以\",\"分隔的每个单词或词组称为 tag。所以prompt和negative prompt是由系列由\",\"分隔的tag组成的。"
                    "调整关键字强度的等效方法是使用 () 和 []。 (keyword) 将tag的强度增加 1.1 倍，与 (keyword:1.1) 相同，最多可加三层。 [keyword] 将强度降低 0.9 倍，与 [keyword:0.9] 相同。"
                    "Prompt 格式要求下面我将说明 prompt 的生成步骤，这里的 prompt 可用于描述人物、风景、物体或抽象数字艺术图画。你可以根据需要添加合理的、但不少于5处的画面细节。"
                    "prompt 要求你输出的 Stable Diffusion prompt 以“Prompt:”开头。prompt 内容包含画面主体、材质、附加细节、图像质量、艺术风格、色彩色调、灯光等部分，但你输出的 prompt 不能分段，例如类似\"medium:\"这样的分段描述是不需要的，也不能包含\":\"和\".\"。"
                    "画面主体：不简短的英文描述画面主体, 如 A girl in a garden，主体细节概括（主体可以是人、事、物、景）画面核心内容。这部分根据我每次给你的主题来生成。你可以添加更多主题相关的合理的细节。"
                    "对于人物主题，你必须描述人物的眼睛、鼻子、嘴唇，例如'beautiful detailed eyes,beautiful detailed lips,extremely detailed eyes and face,long eyelashes'，以免Stable Diffusion随机生成变形的面部五官，这点非常重要。"
                    "你还可以描述人物的外表、情绪、衣服、姿势、视角、动作、背景等。人物属性中，1girl表示一个女孩，2girls表示两个女孩。"
                    "材质：用来制作艺术品的材料。 例如：插图、油画、3D 渲染和摄影。 Medium 有很强的效果，因为一个关键字就可以极大地改变风格。"
                    "附加细节：画面场景细节，或人物细节，描述画面细节内容，让图像看起来更充实和合理。这部分是可选的，要注意画面的整体和谐，不能与主题冲突。"
                    "图像质量：这部分内容开头永远要加上“(best quality,4k,8k,highres,masterpiece:1.2),ultra-detailed,(realistic,photorealistic,photo-realistic:1.37)”， 这是高质量的标志。"
                    "其它常用的提高质量的tag还有，你可以根据主题的需求添加：HDR,UHD,studio lighting,ultra-fine painting,sharp focus,physically-based rendering,extreme detail description,professional,vivid colors,bokeh。"
                    "艺术风格：这部分描述图像的风格。加入恰当的艺术风格，能提升生成的图像效果。常用的艺术风格例如：portraits,landscape,horror,anime,sci-fi,photography,concept artists等。"
                    "色彩色调：颜色，通过添加颜色来控制画面的整体颜色。"
                    "灯光：整体画面的光线效果。"
                    "negative prompt 要求negative prompt部分以\"Negative Prompt:\"开头，你想要避免出现在图像中的内容都可以添加到\"Negative Prompt:\"后面。"
                    "任何情况下，negative prompt都要包含这段内容：\"nsfw,(low quality,normal quality,worst quality,jpeg artifacts),cropped,monochrome,lowres,low saturation,((watermark)),(white letters)\""
                    "如果是人物相关的主题，你的输出需要另加一段人物相关的 negative prompt，内容为：“skin spots,acnes,skin blemishes,age spot,mutated hands,mutated fingers,deformed,bad anatomy,disfigured,poorly drawn face,extra limb,ugly,poorly drawn hands,missing limb,floating limbs,disconnected limbs,out of focus,long neck,long body,extra fingers,fewer fingers,,(multi nipples),bad hands,signature,username,bad feet,blurry,bad body”。"
                    "限制：tag 内容用英语单词或短语来描述，并不局限于我给你的单词。注意只能包含关键词或词组。注意不要输出句子，不要有任何解释。tag数量限制40个以内，单词数量限制在60个以内。tag不要带引号(\"。\").使用英文半角\",\"做分隔符。tag 按重要性从高到低的顺序排列。我给你的主题可能是用中文描述，你给出的prompt和negative prompt只能用英文给。"
                    )
                },
                {"role": "user", "content": topic}
            ],
        )
        # Print the AI's response
        print(response.choices[0].message)
        # Extract the message content from the CompletionMessage object
        message_content = response.choices[0].message.content
        file_name = f"{topic}.txt"
        # Save the message content to a text file
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(message_content)
            print("响应已保存到本地文件。")
    except Exception as e:
        print(f"Error: {e}")
        return None
    # 返回AI的回复
    return message_content



def separate_prompts(content):
    try:
        prompt_start = content.find("Prompt:") + len("Prompt:")
        prompt_end = content.find("Negative Prompt:")
        prompt = content[prompt_start:prompt_end].strip()

        negative_prompt_start = content.find("Negative Prompt:") + len("Negative Prompt:")
        negative_prompt_end = content.find("(For this particular theme)")
        negative_prompt = content[negative_prompt_start:negative_prompt_end].strip()

        return prompt, negative_prompt
    except Exception as e:
        print(f"Error in separate_prompts: {e}")
        return None, None

#word = "Prompt: A historic scene of the founding ceremony of the People's Republic of China, the Tiananmen Square filled with a massive crowd, the red flags waving, soldiers marching in perfect formation, the silhouette of the Monument to the People's Heroes in the background, clear blue sky, traditional Chinese architecture, vibrant colors, socialist realism art style, (best quality,4k,8k,highres,masterpiece:1.2), ultra-detailed, (realistic,photorealistic,photo-realistic:1.37), HDR, UHD, studio lighting, vivid colors.Negative Prompt: nsfw, (low quality,normal quality,worst quality,jpeg artifacts), cropped, monochrome, lowres, low saturation, ((watermark)), (white letters), modern elements, western architecture, blurry, bad anatomy, disfigured, poorly drawn face, extra limb, ugly, poorly drawn hands, missing limb, floating limbs, disconnected limbs, out of focus. (For this particular theme, it's important to exclude any modern or western elements that do not fit the historical setting of the event.)"


app = FastAPI()
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(data)
        try:
            content = llm(data)
            if content is None:
                continue
            prompt_create, negative_prompt_create = separate_prompts(content)
            if prompt_create is None or negative_prompt_create is None:
                continue
            image_data = run_circle(prompt=prompt_create, negative_prompt=negative_prompt_create)
            print("done")
            await websocket.send_text(f"{data}")
            if image_data:
                await websocket.send_bytes(image_data)
                print("send image")
        except Exception as e:
            print(f"Error: {e}")
            await websocket.send_text(f"Error: {e}")
