import json
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments

def train_model(data_file, model_dir):
    """
    Train a GPT model using the collected data.

    Parameters:
        data_file (str): Path to the JSON file containing the training data.
        model_dir (str): Directory to save the trained model.
    """
    with open(data_file, 'r') as file:
        data = json.load(file)

    texts = [item["content"] for item in data]

    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')

    inputs = tokenizer(texts, return_tensors='pt', max_length=512, truncation=True, padding=True)

    training_args = TrainingArguments(
        output_dir=model_dir,
        num_train_epochs=3,
        per_device_train_batch_size=2,
        save_steps=10_000,
        save_total_limit=2,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=inputs['input_ids']
    )

    trainer.train()
    model.save_pretrained(model_dir)
    tokenizer.save_pretrained(model_dir)
    print(f"Model trained and saved to {model_dir}")

if __name__ == "__main__":
    data_file = "training_data.json"
    model_dir = "Veronica"
    train_model(data_file, model_dir)
