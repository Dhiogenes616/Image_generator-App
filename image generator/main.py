import os
import openai

openai.api_key ="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"

user_prompt = "rato segurando uma faca"

response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)