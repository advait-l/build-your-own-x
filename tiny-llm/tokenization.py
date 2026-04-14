# Character-level tokenization
text = "Hello, world!"

# Split into individual characters
char_tokens = list(text)

print("Original text:", text)
print("Character tokens:", char_tokens)
print("Number of tokens:", len(char_tokens))

# Each character becomes a separate token
for i, char in enumerate(char_tokens):
    print(f"  Token {i}: '{char}'")

# Simple word-level tokenization
text = "Hello, world! How are you?"

# Split by spaces
word_tokens = text.split()

print("Original text:", text)
print("Word tokens:", word_tokens)
print("Number of tokens:", len(word_tokens))

print("\nTokens:")
for i, word in enumerate(word_tokens):
    print(f"  Token {i}: '{word}'")

print("\n⚠️ Notice: Punctuation is stuck to words!")
print("'Hello,' is treated as different from 'Hello'")
