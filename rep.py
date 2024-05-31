import os
import replicate

os.environ["REPLICATE_API_TOKEN"] = "r8_QwwqC438KmrHPAslIh68DgTaft5sS103QlMbV"

output = replicate.run(
    "bytedance/sdxl-lightning-4step:5f24084160c9089501c1b3545d9be3c27883ae2239b6f412990e82d4a6210f8f",
    input={  # Changed to use "input" as a keyword argument
        "width": 1024,
        "height": 1024,
        "prompt": "self-portrait of a woman, lightning in the background",
        "scheduler": "K_EULER",
        "num_outputs": 1,
        "guidance_scale": 0,
        "negative_prompt": "worst quality, low quality",
        "num_inference_steps": 4,
    },
)

print(output)
