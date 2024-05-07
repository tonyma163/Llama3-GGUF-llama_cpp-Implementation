# import
from utils.model import load_llama, generate_reponse

# Load Llama3 model
model_path="./models/Llama3-8B-Chinese-Chat-q8_0-v2_1.gguf"
model = load_llama(model_path)

# Prompting
system_prompt = "You are a helpful assistant."
query_prompt = "写一首诗吧"

messages = [
    {
        "role": "system",
        "content": system_prompt,
    },
    {
        "role": "user",
        "content": query_prompt
    },
]

# Generate response
print(generate_reponse(model=model, messages=messages, max_tokens=8192))