import streamlit as st
import sys
import time
from PIL import Image
sys.path.append('./webuiapi')
import webuiapi

st.title("Generate Images with API")

# Initialize API
api = webuiapi.WebUIApi(host='127.0.0.1',
                        port=7860,
                        sampler='Euler a',
                        steps=20)

def run_api(prompt, negative_prompt):
    try:
        result = api.txt2img(prompt=prompt,
                             negative_prompt=negative_prompt,
                             styles=["anime"],
                             cfg_scale=7)
        st.image(result.image, caption=f"Generated Image for '{prompt}'", use_column_width=True)
        return True
    except Exception as e:
        st.error(f"Error: {e}")
        return False

# Main Streamlit UI
def main():
    prompt = st.text_input("Enter prompt:")
    negative_prompt = st.text_input("Enter negative prompt:")
    if st.button("Generate Image"):
        if prompt and negative_prompt:
            if not run_api(prompt, negative_prompt):
                st.warning("Failed to generate image. Please try again.")

if __name__ == "__main__":
    main()
