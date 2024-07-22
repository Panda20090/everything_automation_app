from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

def evaluate_model(model_dir, test_text):
    """
    Evaluate the trained model.

    Parameters:
        model_dir (str): Directory where the trained model is saved.
        test_text (str): Text to evaluate the model on.
    """
    tokenizer = GPT2Tokenizer.from_pretrained(model_dir)
    model = GPT2LMHeadModel.from_pretrained(model_dir)

    inputs = tokenizer(test_text, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    predictions = torch.argmax(logits, dim=-1)
    predicted_text = tokenizer.decode(predictions[0])

    print(f"Input text: {test_text}")
    print(f"Predicted text: {predicted_text}")

if __name__ == "__main__":
    model_dir = "Veronica"
    test_text = "This is a test sentence."
    evaluate_model(model_dir, test_text)
