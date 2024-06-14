import nltk

text = "Time flies like an arrow, but fruit flies like a banana."

tokens = nltk.word_tokenize(text)

tagged_tokens = nltk.pos_tag(tokens)

print("Original Text:", text)
print("POS Tags:", tagged_tokens)
