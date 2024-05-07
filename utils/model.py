from llama_cpp import Llama

# Load Llama3
def load_llama(model_path):
    model = Llama(
        model_path=model_path,
        verbose=False,
        n_gpu_layers=-1
    )
    return model

# Generate response function
def generate_reponse(model, messages, max_tokens):
    output = model.create_chat_completion(
        messages,
        stop=["<|eot_id|>", "<|end_of_text|>"],
        max_tokens=max_tokens,
    )["choices"][0]["message"]["content"]
    return output