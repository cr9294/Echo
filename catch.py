#抓取chatglm生成的文本prompt：
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
