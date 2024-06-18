import spacy

nlp = spacy.load("en_core_web_sm")

sentences = [
    "John and Mary went to the store.",
    "The big brown dog chased the small black cat."
]

for sentence in sentences:
    doc = nlp(sentence)

    print(f"Sentence: {sentence}")
    for token in doc:
        print(f"{token.text} ({token.pos_})")

    for token in doc:
        print(f"{token.text} ({token.dep_}) -> {token.head.text} ({token.head.dep_})")
    print("\n")  
