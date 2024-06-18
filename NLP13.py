from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "Natural language processing (NLP) is a field of study in artificial intelligence.",
    "NLP techniques are used in various applications like machine translation and sentiment analysis.",
    "The development of NLP tools and libraries has made text analysis easier."
]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

tfidf_matrix_dense = tfidf_matrix.todense()

feature_names = vectorizer.get_feature_names_out()
for doc_idx, doc in enumerate(tfidf_matrix_dense):
    print(f"Document {doc_idx + 1} TF-IDF scores:")
    for word_idx, score in enumerate(doc.tolist()[0]):
        print(f"{feature_names[word_idx]}: {score:.4f}")
    print("\n")
