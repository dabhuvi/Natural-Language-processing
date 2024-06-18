from transformers import MarianMTModel, MarianTokenizer
model_name = "Helsinki-NLP/opus-mt-en-de"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
def translate(text, model, tokenizer):
    inputs = tokenizer.encode(text, return_tensors="pt", truncation=True)
    translated_tokens = model.generate(inputs, max_length=512, num_beams=5, early_stopping=True)
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text
sentences = [
    "Hello, how are you?",
    "I love programming.",
    "What is your name?",
    "The weather is nice today."
]
for sentence in sentences:
    translated_sentence = translate(sentence, model, tokenizer)
    print(f"English: {sentence}")
    print(f"German: {translated_sentence}\n")
