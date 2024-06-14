import re
text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Duis vehicula urna at sem egestas, et blandit elit sollicitudin. 
Sed et nisi sed augue consequat facilisis. 
Vestibulum tincidunt dolor at libero mollis, a varius dui consectetur. 
Email me at example@example.com or visit my website at https://www.example.com.
Call me at (123) 456-7890.
"""
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text)
print("Email addresses found:", emails)
url_pattern = r'https?://[A-Za-z0-9./]+'
urls = re.findall(url_pattern, text)
print("URLs found:", urls)
phone_pattern = r'\(\d{3}\) \d{3}-\d{4}'
phones = re.findall(phone_pattern, text)
print("Phone numbers found:", phones)
capitalized_words_pattern = r'\b[A-Z][a-z]*\b'
capitalized_words = re.findall(capitalized_words_pattern, text)
print("Capitalized words found:", capitalized_words)
search_pattern = r'dolor'
match = re.search(search_pattern, text)
if match:
    print(f"First occurrence of 'dolor' found at position: {match.start()}")
else:
    print("'dolor' not found in the text")
