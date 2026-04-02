#Stable Diffusion WebUI API 的api文生成图片端口调用
# use webuiapi.py from webuiapi folder
import sys
sys.path.append('./webuiapi')

#引用api端口库，可以通过"pip install webuiapi"命令安装
# or install using pip install webuiapi
import webuiapi
# api = webuiapi.WebUIApi()

#定义api端口，host为本地地址，port为端口号，sampler为模型名称，steps为迭代次数
api = webuiapi.WebUIApi(host='127.0.0.1',
                        port=7860,
                        sampler='Euler a',
                        steps=20)
print(api)

#文生成图片端口测试
# txt2img
result1 = api.txt2img(prompt="cute squirrel",
                    negative_prompt="ugly, out of frame",
                    styles=["anime"],
                    cfg_scale=7,
#                      sampler_index='DDIM',
#                      steps=30,
                    )
result1.image.show()