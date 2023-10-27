# Sample text data
text_data = """It is a good practice to code everyday , this will help you with problem solving understand the concept of the 
topic and try to work on it
"""
# Define a list of stop words (common words to be removed)
stop_words = ["a", "an", "the", "is", "of", "and", "with", "in", "to", "this"]

# Step 1: Case-Folding (Converting text to lowercase)
text_data = text_data.lower()

# Step 2: Tokenization (Splitting text into words)
words = text_data.split()

# Step 3: Stop Word Removal
filtered_words = [word for word in words if word not in stop_words]

# Reconstruct the preprocessed text
preprocessed_text = " ".join(filtered_words)

# Display the preprocessed text
print("GIVEN TEXT:\n", text_data)
tokens=nltk.word_tokenize(text_data)
print("token:\n",tokens)
print("\nRESULT after case folding and stop watch removal:\n", preprocessed_text)
