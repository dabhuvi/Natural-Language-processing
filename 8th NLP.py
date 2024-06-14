from collections import Counter

def most_frequent_tag(word, tagged_text):
  """
  Returns the most frequent POS tag for a given word in the training data.

  Args:
      word: The word for which to find the most frequent tag.
      tagged_text: A list of tuples containing (word, tag) pairs.

  Returns:
      The most frequent POS tag for the given word, or None if unseen.
  """
  word_tags = Counter(tag for word, tag in tagged_text if word == word.lower())
  return word_tags.most_common(1)[0][0] if word_tags else None

def stochastic_pos_tag(text, tagged_text):
  """
  Performs POS tagging on a text using a most-frequent-tag approach.

  Args:
      text: The text to be tagged.
      tagged_text: A list of tuples containing (word, tag) pairs (training data).

  Returns:
      A list of POS tags for each word in the text.
  """
  words = text.lower().split()
  tags = []
  for word in words:
    most_frequent_tag_ = most_frequent_tag(word, tagged_text)
    tags.append(most_frequent_tag_ if most_frequent_tag_ else "UNKNOWN")
  return tags
tagged_text = [("Time", "NN"), ("flies", "VBZ"), ("like", "IN"), ...]  # Sample training data
text_to_tag = "This is a test sentence."

predicted_tags = stochastic_pos_tag(text_to_tag, tagged_text)
print("Original Text:", text_to_tag)
print("Predicted Tags:", predicted_tags)
