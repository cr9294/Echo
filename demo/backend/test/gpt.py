#文心一言端口测试

# -*- coding: utf-8 -*
import wenxin_api # 可以通过"pip install wenxin-api"命令安装
from wenxin_api.tasks.free_qa import FreeQA
wenxin_api.ak = "cTYcOLlpHTEInUSQTrXWGSwraG1Mc9Do" #输入您的API Key
wenxin_api.sk = "2i2yRh94wsq3UfbcOY9LoiwCuaGIaPGE" #输入您的Secret Key
# 问答
input_dict = {
    "text": "问题：交朋友的原则是什么？\n回答：",
    "seq_len": 512,
    "topp": 0.5,
    "penalty_score": 1.2,
    "min_dec_len": 2,
    "min_dec_penalty_text": "。?：！[<S>]",
    "is_unidirectional": 0,
    "task_prompt": "qa",
    "mask_type": "paragraph"
}
rst = FreeQA.create(**input_dict)
print(rst)