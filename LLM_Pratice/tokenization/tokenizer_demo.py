from transformers import AutoTokenizer


# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    "bert-base-uncased"
)


# Input text
text = """
Machine learning is a branch of artificial intelligence
that allows computers to learn from data.
"""


# Tokenize text
tokens = tokenizer.tokenize(text)


# Convert tokens into token IDs
token_ids = tokenizer.convert_tokens_to_ids(tokens)


# Count tokens
token_count = len(token_ids)


print("\nOriginal Text:")
print(text)

print("\nTokens:")
print(tokens)

print("\nToken IDs:")
print(token_ids)

print("\nTotal Token Count:")
print(token_count)