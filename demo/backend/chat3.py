#chatglm3, chatglm3-6b,能不能跑测试代码
from transformers import AutoTokenizer, AutoModel
# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("/home/lanqiao/data/pycharm/factory/chatglm3-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("/home/lanqiao/data/pycharm/factory/chatglm3-6b", trust_remote_code=True, device='cuda')
model = model.eval()
# Chat history initialization
history = []
def chat_with_model(input_text):
    global history
    # Chat with the model using the same fixed prompt
    response, history = model.chat(tokenizer, input_text, history=history)
    return response, history
# Example usage
response, history = chat_with_model("你好")
print(response)
response, history = chat_with_model("辽宁的省会是哪里？")
print(response)