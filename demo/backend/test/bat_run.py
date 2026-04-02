import subprocess
import psutil

# 用于启动的脚本文件路径
script_path = r"E:\Nlp\Stable\stable-diffusion-webui\webui-user.bat"

# 检查进程是否已经在运行
def is_process_running(process_name):
    for process in psutil.process_iter():
        if process.name().lower() == process_name.lower():
            return True
    return False

# 如果进程已经在运行，则不做任何操作
if is_process_running("webui-user.bat"):
    print("脚本已经在运行，不做任何操作")
else:
    try:
        # 使用 subprocess 模块启动脚本
        subprocess.Popen(script_path, shell=True)
        print("脚本已成功启动")
    except Exception as e:
        print(f"启动脚本时出现错误: {e}")