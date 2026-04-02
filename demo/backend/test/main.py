# main.py
import main as st
import time
from PIL import Image
from circle_test import run_circle

def main():
    st.title("Circle Generator")

    # 创建文本输入框
    prompt = st.text_input("Enter prompt:")
    negative_prompt = st.text_input("Enter negative prompt:")

    # 创建提交按钮
    if st.button("Generate"):
        # 调用 run_circle 函数
        if run_circle(prompt=prompt, negative_prompt=negative_prompt):
            # 如果执行成功，显示生成的图片
            generated_image_path = f"generated_image_{prompt}.png"
            generated_image = Image.open(generated_image_path)
            st.image(generated_image, caption='Generated Image', use_column_width=True)
        else:
            st.write("Failed to generate image.")

if __name__ == "__main__":
    main()
