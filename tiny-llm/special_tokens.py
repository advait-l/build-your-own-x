# Demonstrating special tokens with tiny GPT vocabulary
vocab = [
    "the",
    "cat",
    "dog",
    "sat",
    "ran",
    "on",
    "mat",
    "house",
    "a",
    "big",
    "small",
    "quickly",
    "slowly",
    "and",
    "is",
    "red",
    "blue",
    "to",
    "PAD",
    "END",
]

print(f"Vocabulary size: {len(vocab)} tokens")
print(f"Regular words: {len(vocab) - 2}")
print(f"Special tokens: 2 (PAD, END)")
print()

# Example 1: Complete sentence with END marker
text_tokens = ["the", "cat", "sat", "END"]
print("Example 1: Complete sentence with END marker")
print(f"  Tokens: {text_tokens}")
print(f"  Length: {len(text_tokens)}")
print()

# Example 2: Padding shorter sequences
sequences = [
    ["the", "cat", "END"],  # 3 tokens
    ["a", "dog", "ran", "quickly", "END"],  # 5 tokens
]

max_len = max(len(seq) for seq in sequences)
print(f"Example 2: Padding to match length {max_len}")

for i, seq in enumerate(sequences):
    # Add padding tokens to reach max_len
    padded = seq + ["PAD"] * (max_len - len(seq))
    print(f"  Sequence {i + 1}: {seq}")
    print(f"  Padded:     {padded}")
    print()


# Example 3: Token IDs
def tokens_to_ids(tokens):
    return [vocab.index(t) for t in tokens]


example = ["the", "cat", "sat", "END"]
token_ids = tokens_to_ids(example)

print("Example 3: Converting to token IDs")
print(f"  Tokens: {example}")
print(f"  IDs:    {token_ids}")
print()
for token, idx in zip(example, token_ids):
    print(f"    '{token}' → {idx}")
