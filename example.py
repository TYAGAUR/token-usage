from token_usage import calculate_token_usage

requests = [
    {"input_tokens": 12, "output_tokens": 18},
    {"input_tokens": 20, "output_tokens": 10},
]

summary = calculate_token_usage(requests)
print(summary)