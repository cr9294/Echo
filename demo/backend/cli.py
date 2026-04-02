import json
import os
from openai import OpenAI
from colorama import init, Fore
from loguru import logger
import platform
from tool_register import get_tools, dispatch_tool

init(autoreset=True)
# 创建聊天客户端
client = OpenAI(
    base_url="http://127.0.0.1:8000/v1",
    api_key="xxx"
)

# 获取工具信息，包括工具名称、描述和参数信息。
functions = get_tools()


def run_conversation(query: str, stream=False, functions=None, max_retry=5):
    # 设置OpenAI参数
    params = dict(
        model="chatglm3",
        messages=[
            # 不加提示词的话，LLM最终输出结果可能与工具结果不同。可能是因为LLM对答案进行推理，“推翻”了工具的结果。
            # {   "role": "system",
            #     "content": "调用工具解决问题，如果没有合适的工具可以调用，那就不调用任何工具。最后的输出结果应该是工具的结果。"},

            # {   "role": "system",
            #     "content": "你是一个有用的人工智能助手,你可以调用工具解决问题，但最后的输出结果就是工具的结果,不要输出其它内容。"},

            {"role": "user", "content": query}],
        stream=stream)

    if functions:
        params["functions"] = functions

    # stream为False表示大模型会一次性回复完整答案
    response = client.chat.completions.create(**params)
    for _ in range(max_retry):
        if not stream:
            # logger.info(response.choices[0].message.function_call)
            # 判断是否有函数调用
            if response.choices[0].message.function_call:
                function_call = response.choices[0].message.function_call
                # function_call.model_dump() 用于生成模型的字典表示形式
                logger.info(f"Function Call Response: {function_call.model_dump()}")

                # 要传入调用函数的参数
                function_args = json.loads(function_call.arguments)
                tool_response = dispatch_tool(function_call.name, function_args)
                logger.info(f"Tool Call Response: {tool_response}")

                # 将本次回答的消息（助手回复）添加到对话历史记录中
                params["messages"].append(response.choices[0].message)
                params["messages"].append(
                    {
                        "role": "function",
                        "name": function_call.name,
                        "content": tool_response,  # 调用函数返回结果
                    }
                )
            else:
                reply = response.choices[0].message.content
                logger.info(f"Final Reply: \n{reply}")
                return

        else:
            output = ""
            for chunk in response:
                content = chunk.choices[0].delta.content or ""
                print(Fore.BLUE + content, end="", flush=True)
                output += content

                if chunk.choices[0].finish_reason == "stop":
                    return

                elif chunk.choices[0].finish_reason == "function_call":
                    print("\n")

                    function_call = chunk.choices[0].delta.function_call
                    logger.info(f"Function Call Response: {function_call.model_dump()}")

                    function_args = json.loads(function_call.arguments)
                    tool_response = dispatch_tool(function_call.name, function_args)
                    logger.info(f"Tool Call Response: {tool_response}")

                    params["messages"].append(
                        {
                            "role": "assistant",
                            "content": output
                        }
                    )
                    params["messages"].append(
                        {
                            "role": "function",
                            "name": function_call.name,
                            "content": tool_response,  # 调用函数返回结果
                        }
                    )

                    break
        response = client.chat.completions.create(**params)


if __name__ == "__main__":
    query = "9.0和6.0的和等于多少"
    run_conversation(query, functions=functions, stream=False)
