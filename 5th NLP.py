from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["running", "programmer", "programs", "phones", "playing"]
stemmed_words = [stemmer.stem(word) for word in words]
print("Original Words:", words)
print("Stemmed Words:", stemmed_words)
