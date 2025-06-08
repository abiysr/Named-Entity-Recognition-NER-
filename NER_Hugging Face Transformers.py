# pip install transformers
# pip install torch  # Or: pip install tensorflow

from transformers import pipeline

ner_pipeline = pipeline(
    "ner", 
    model="dbmdz/bert-large-cased-finetuned-conll03-english", 
    aggregation_strategy="simple"
)

# Your text
text = "Apple, based in Cupertino, announced that Tim Cook will be presenting the new iPhone in September for $999."

# Get the results
results = ner_pipeline(text)

# Print the results
print("--- Entities Found ---")
for entity in results:
    print(f"Entity: {entity['word']}, Label: {entity['entity_group']}, Score: {entity['score']:.4f}")

# Output:

    # --- Entities Found ---
# Entity: Apple, Label: ORG, Score: 0.9991
# Entity: Cupertino, Label: LOC, Score: 0.9997
# Entity: Tim Cook, Label: PER, Score: 0.9998
