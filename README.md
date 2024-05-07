# Llama3 GGUF llama_cpp
Using llama_cpp to load Llama3-8B-Chinese-Chat-GGUF-8bit model.

# Installation
Requirements:
- Python 3.8+
- C complier

## Install the package
```
pip install llama-cpp-python
```

## Usage
### Run
```
python app.py
```

### Use your own Llama GGUF model
```
# Load Llama3 model
model_path="./models/Llama3-8B-Chinese-Chat-q8_0-v2_1.gguf"
model = load_llama(model_path)
```
You can use other Llama gguf model by modifying the model_path which contain your downloaded Llama GGUF file.

### Change the max_tokens
```
# Generate response
print(generate_reponse(model=model, messages=messages, max_tokens=8192))
```
You can change the max_tokens values to suit your use case.
