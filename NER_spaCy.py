# Install spaCy
# pip install spacy

# Download the small English model
# python -m spacy download en_core_web_sm
# en_core_web_sm: Small English model. Fast and good for getting started.
# en_core_web_md: Medium English model. More accurate.
# en_core_web_lg: Large English model. Most accurate, but larger and slower.

import spacy

# Load the pre-trained English model
# The 'sm' stands for small model. For higher accuracy, you can use 'md' (medium) or 'lg' (large).
nlp = spacy.load("en_core_web_sm")

# Your text
text = "Apple, based in Cupertino, announced that Tim Cook will be presenting the new iPhone in September for $999."

# Process the text with the spaCy model
doc = nlp(text)

# Iterate over the detected entities and print them
print("--- Entities Found ---")
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}, Description: {spacy.explain(ent.label_)}")

    # Output of the Code:
    # --- Entities Found ---
# Entity: Apple, Label: ORG, Description: Companies, agencies, institutions, etc.
# Entity: Cupertino, Label: GPE, Description: Countries, cities, states
# Entity: Tim Cook, Label: PERSON, Description: People, including fictional
# Entity: September, Label: DATE, Description: Absolute or relative dates or periods
# Entity: $999, Label: MONEY, Description: Monetary values, including unit