import ollama

prompt = "Write an email apologizing to Sarah for the tragic gardening mishap. Explain how it happened.<|assistant|>"

response = ollama.generate(
    model='phi3:mini',
    prompt=prompt,
    raw=True,
    options={
        'num_predict': 20,   # аналог max_new_tokens=20
    }
)

print(response['response'])
