# AI Token Usage Calculator

This tiny Python project adds up the tokens used by a list of AI requests and
works out the average tokens used for each request.

## What are tokens?

An AI model breaks text into small pieces called **tokens**. A token can be a
whole short word, part of a longer word, or punctuation. The model uses tokens
both to read your message and to write its answer:

- **Input tokens** are the tokens sent to the AI.
- **Output tokens** are the tokens the AI sends back.

## How to use it

Each request is a Python dictionary with `input_tokens` and `output_tokens`.
Pass a list of those dictionaries to `calculate_token_usage`:

```python
from token_usage import calculate_token_usage

requests = [
    {"input_tokens": 12, "output_tokens": 18},
    {"input_tokens": 20, "output_tokens": 10},
]

summary = calculate_token_usage(requests)
print(summary)
```

The result is:

```text
{'request_count': 2, 'total_input_tokens': 32, 'total_output_tokens': 28, 'total_tokens': 60, 'average_input_tokens': 16.0, 'average_output_tokens': 14.0, 'average_tokens_per_request': 30.0}
```

## How the code works

1. It starts both totals at zero.
2. It checks each request and adds its input and output tokens to the totals.
3. It adds the input and output totals to get all tokens used.
4. It divides each total by the number of requests to get the averages.
5. If the list is empty, the totals and averages are zero instead of causing a
   divide-by-zero error.

Token counts must be non-negative whole numbers. The function raises an error
if a request is missing a count or contains an invalid count.

## Try it

You need Python 3.10 or newer. Save the example above in a file such as
`example.py`, then run:

```text
python example.py
```
