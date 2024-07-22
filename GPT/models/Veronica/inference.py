from transformers import GPT2Tokenizer, GPT2LMHeadModel

def generate_text(model_dir, prompt):
    """
    Generate text using the trained model.

    Parameters:
        model_dir (str): Directory where the trained model is saved.
        prompt (str): Prompt text to generate from.
    """
    tokenizer = GPT2Tokenizer.from_pretrained(model_dir)
    model = GPT2LMHeadModel.from_pretrained(model_dir)

    inputs = tokenizer(prompt, return_tensors='pt')
    outputs = model.generate(inputs['input_ids'], max_length=50, num_return_sequences=1)

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Generated text: {generated_text}")

if __name__ == "__main__":
    model_dir = "Veronica"
    prompt = "Once upon a time"
    generate_text(model_dir, prompt)
