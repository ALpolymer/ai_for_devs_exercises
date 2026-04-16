import os
import json
from utils import ask



my_prompt = """I would like to classify the following sentence:

'Ο Γιάννης αγόρασε ένα κινητό και είναι πολύ ευχαριστημένος με την κάμερα αλλά όχι με την μπαταρία.'

The classification must be based on:
- The general sentiment of the sentence
- The positive and the negative aspects inside the sentence

The response MUST be structured in JSON format as follows:
{
  "sentiment": "...",
  "positive_aspects": ["..."],
  "negative_aspects": ["..."]
}

Return ONLY the JSON object. No explanation, no markdown, no extra text.
"""

response = ask(prompt=my_prompt, temperature=0)


try:
    result = json.loads(response)
    print("\n=== Parsed JSON ===")
    print(f"Sentiment       : {result['sentiment']}")
    print(f"Positive aspects: {result['positive_aspects']}")
    print(f"Negative aspects: {result['negative_aspects']}")
except json.JSONDecodeError:
    print(f"{response}")
    print("Not valid JSON")