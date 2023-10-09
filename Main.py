from collections import Counter
import re

# Function to clean and split text into words for analysis
def clean_and_split_text(text):
    # Remove special characters
    cleaned_text = re.sub(r'[^\w\s]', '', text)

    # Convert to lowercase and split into words
    words = cleaned_text.lower().split()

    return words

# Clean and split the text into words
words = clean_and_split_text(docx_text)

# Count the frequency of each word
word_count = Counter(words)

# Display the most common words to help identify main themes or topics
common_words = word_count.most_common(20)
common_words
