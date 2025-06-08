# pip install nltk

# Run this in a Python interpreter to download the necessary data
# >>> import nltk
# >>> nltk.download('popular')

import nltk

# Sample text
text = "Apple, based in Cupertino, announced that Tim Cook will be presenting the new iPhone in September for $999."

# 1. Tokenize the sentence into words
tokens = nltk.word_tokenize(text)

# 2. Tag the words with their Part of Speech (POS)
tagged_tokens = nltk.pos_tag(tokens)

# 3. Perform Named Entity Recognition (Chunking)
# The binary=False argument means it will label entities with more specific types (GPE, PERSON, etc.)
# If binary=True, it would just label them as 'NE' (Named Entity).
entities = nltk.ne_chunk(tagged_tokens, binary=False)

# Now, iterate through the tree to find the entities
print("--- Entities Found ---")
for chunk in entities:
    # An entity is a 'Tree' object in NLTK
    if hasattr(chunk, 'label'):
        entity_name = ' '.join(c[0] for c in chunk)
        entity_label = chunk.label()
        print(f"Entity: {entity_name}, Label: {entity_label}")

        # Output:

       # --- Entities Found ---
# Entity: Apple, Label: PERSON
# Entity: Cupertino, Label: GPE
# Entity: Tim Cook, Label: PERSON
# Entity: iPhone, Label: GPE