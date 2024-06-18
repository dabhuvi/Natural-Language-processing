import spacy

nlp = spacy.load("en_core_web_sm")

sentence = "Barack Obama was the 44th President of the United States, and he was born in Honolulu, Hawaii."

doc = nlp(sentence)
for entity in doc.ents:
    print(f"{entity.text} ({entity.label_})")
