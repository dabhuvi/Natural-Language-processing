import nltk
from collections import defaultdict, Counter
import random
text = "I am Sam. Sam I am. I do not like green eggs and ham."
tokens = nltk.word_tokenize(text.lower())
tokens
