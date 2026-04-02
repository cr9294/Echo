#chatglm3, chatglm3-6b,能不能跑测试代码
from transformers import AutoTokenizer, AutoModel
# Chat history initialization
history = [
    {
        "role": "user",
        "content": "请问我需要做什么？"
    },
    {
        "role": "assistant",
        "content": "你需要根据给定的主题想象一幅完整的画面，并转化成详细的、高质量的prompt，以帮助Stable Diffusion生成图像。"
    },
    {
        "role": "user",
        "content": "我需要了解更多关于Stable Diffusion prompt的内容。"
    },
    {
        "role": "assistant",
        "content": "Stable Diffusion prompt是一种用于描述图像的文本格式，通过指定图像主体、材质、细节、质量等要素，帮助模型生成图像。"
    },
    {
        "role": "user",
        "content": "我需要了解prompt的结构和要求。"
    },
    {
        "role": "assistant",
        "content": "prompt由\"Prompt:\"和\"Negative Prompt:\"两部分组成，分别描述图像内容和要避免的内容。每部分由英文逗号分隔的tag构成，按重要性排序。"
    },
    {
        "role": "user",
        "content": "请问有什么限制吗？"
    },
    {
        "role": "assistant",
        "content": "限制：tag 内容用英语单词或短语来描述，并不局限于我给你的单词。注意只能包含关键词或词组。注意不要输出句子，不要有任何解释。tag数量限制40个以内，单词数量限制在60个以内。tag不要带引号(\"。\").使用英文半角\",\"做分隔符。tag 按重要性从高到低的顺序排列。我给你的主题可能是用中文描述，你给出的prompt和negative prompt只能用英文给。"
    },
    {
        "role": "user",
        "content": "能否提供一些关于prompt格式和要求的示例？"
    },
    {
        "role": "assistant",
        "content": "Prompt: A historic scene of the founding ceremony of the People's Republic of China, the Tiananmen Square filled with a massive crowd, the red flags waving, soldiers marching in perfect formation, the silhouette of the Monument to the People's Heroes in the background, clear blue sky, traditional Chinese architecture, vibrant colors, socialist realism art style, (best quality,4k,8k,highres,masterpiece:1.2), ultra-detailed, (realistic,photorealistic,photo-realistic:1.37), HDR, UHD, studio lighting, vivid colors.Negative Prompt: nsfw, (low quality,normal quality,worst quality,jpeg artifacts), cropped, monochrome, lowres, low saturation, ((watermark)), (white letters), modern elements, western architecture, blurry, bad anatomy, disfigured, poorly drawn face, extra limb, ugly, poorly drawn hands, missing limb, floating limbs, disconnected limbs, out of focus. (For this particular theme, it's important to exclude any modern or western elements that do not fit the historical setting of the event.)"
    },
    {
        "role": "user",
        "content": "下面所有回答都是英文回答吗？"
    },
    {
        "role": "assistant",
        "content": "是的，所有回答都需要用英文回答。"
    },
]

def chat_with_model(input_text):
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("/home/lanqiao/data/pycharm/factory/chatglm3-6b", trust_remote_code=True)
    model = AutoModel.from_pretrained("/home/lanqiao/data/pycharm/factory/chatglm3-6b", trust_remote_code=True,
                                      device='cuda')
    model = model.eval()
    global history
    # Chat with the model using the same fixed prompt
    response, history = model.chat(tokenizer, input_text, history=history)
    return response, history

"""
# Example usage
response, history = chat_with_model("开国大典")
print(response)
response, history = chat_with_model("凯撒大帝被刺")
print(response)
"""
