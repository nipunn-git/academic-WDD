import sys
from transformers import pipeline

p = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
prompt = " ".join(sys.argv[1:]) or "hello"
out = p([{"role": "user", "content": prompt}], max_new_tokens=300)
print(out[0]["generated_text"][-1]["content"])


# python ask.py