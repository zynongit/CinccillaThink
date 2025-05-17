from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Carregar modelo e tokenizador
model_name = "gpt2"  # Você pode usar "gpt2-medium", "gpt2-large" para versões maiores
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Função para gerar texto
def generate_text(prompt, max_length=50):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, do_sample=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Exemplo de uso
if __name__ == "__main__":
    prompt = "A inteligência artificial é"
    generated = generate_text(prompt)
    print(generated)
