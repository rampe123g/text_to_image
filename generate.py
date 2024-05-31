# import os
# import replicate
# import streamlit as st
# import time
# import base64
# from io import BytesIO
# from PIL import Image
# import requests


# # Set your Replicate API token
# os.environ["REPLICATE_API_TOKEN"] = "r8_9ToJKw2xITt0RbfKWyUf24aSZW91icU2jNcmw"

# st.title("AI Image Generator")

# # Input field for user to provide prompt
# prompt = st.text_input("Enter a prompt for the image")


# def create_download_link(image_url):
#     if image_url:
#         response = requests.get(image_url)
#         image = Image.open(BytesIO(response.content))
#         buffered = BytesIO()
#         image.save(buffered, format="PNG")
#         img_str = base64.b64encode(buffered.getvalue()).decode()
#         href = f"data:file/png;base64,{img_str}"
#         st.markdown(
#             f'<a href="{href}" download="generated_image.png">Download generated image</a>',
#             unsafe_allow_html=True,
#         )


# if st.button("Generate Image"):
#     with st.spinner("Generating Image..."):
#         start_time = time.time()

#         # Run the Replicate model
#         output = replicate.run(
#             "bytedance/sdxl-lightning-4step:5f24084160c9089501c1b3545d9be3c27883ae2239b6f412990e82d4a6210f8f",
#             input={
#                 "width": 1024,  # Default width
#                 "height": 1024,  # Default height
#                 "prompt": prompt,
#                 "scheduler": "K_EULER",  # Default scheduler
#                 "num_outputs": 1,
#                 "guidance_scale": 3.18,  # Default guidance scale
#                 "negative_prompt": "worst quality, low quality",  # Default negative prompt
#                 "num_inference_steps": 4,  # Default number of inference steps
#             },
#         )

#         end_time = time.time()
#         elapsed_time = end_time - start_time

#         # Display the generated image
#         image_url = output[0]
#         st.image(image_url)
#         st.write(f"Image generated in {elapsed_time:.2f} seconds")

#         # Create the download link
#         create_download_link(image_url)


import os
import replicate
import streamlit as st
import time
import base64
from io import BytesIO
from PIL import Image
import requests

# Set your Replicate API token
os.environ["REPLICATE_API_TOKEN"] = "r8_9ToJKw2xITt0RbfKWyUf24aSZW91icU2jNcmw"

st.title("AI Image Generator")

# Input field for user to provide prompt
prompt = st.text_input("Enter a prompt for the image")


def create_download_link(image_url, prompt):
    if image_url:
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        safe_prompt = "".join(
            [c if c.isalnum() else "_" for c in prompt]
        )  # Replace non-alphanumeric characters
        href = f"data:file/png;base64,{img_str}"
        st.markdown(
            f'<a href="{href}" download="{safe_prompt}.png">Download generated image</a>',
            unsafe_allow_html=True,
        )


if st.button("Generate Image"):
    with st.spinner("Generating Image..."):
        start_time = time.time()

        # Run the Replicate model
        output = replicate.run(
            "bytedance/sdxl-lightning-4step:5f24084160c9089501c1b3545d9be3c27883ae2239b6f412990e82d4a6210f8f",
            input={
                "width": 1024,  # Default width
                "height": 1024,  # Default height
                "prompt": prompt,
                "scheduler": "K_EULER",  # Default scheduler
                "num_outputs": 1,
                "guidance_scale": 3.18,  # Default guidance scale
                "negative_prompt": "worst quality, low quality",  # Default negative prompt
                "num_inference_steps": 4,  # Default number of inference steps
            },
        )

        end_time = time.time()
        elapsed_time = end_time - start_time

        # Display the generated image
        image_url = output[0]
        st.image(image_url)
        st.write(f"Image generated in {elapsed_time:.2f} seconds")

        # Create the download link with the prompt as the filename
        create_download_link(image_url, prompt)
