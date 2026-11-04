def calculate_token_usage(requests: list[dict[str, int]]) -> dict[str, int | float]:
    """Calculate total and average token usage for a list of AI requests.

    Each request must contain non-negative integer ``input_tokens`` and
    ``output_tokens`` values.
    """
    total_input_tokens = 0
    total_output_tokens = 0

    for request_number, request in enumerate(requests, start=1):
        for field in ("input_tokens", "output_tokens"):
            if field not in request:
                raise ValueError(
                    f"Request {request_number} is missing the '{field}' value."
                )

            token_count = request[field]
            if isinstance(token_count, bool) or not isinstance(token_count, int):
                raise TypeError(
                    f"Request {request_number} '{field}' must be an integer."
                )
            if token_count < 0:
                raise ValueError(
                    f"Request {request_number} '{field}' cannot be negative."
                )

        total_input_tokens += request["input_tokens"]
        total_output_tokens += request["output_tokens"]

    request_count = len(requests)
    total_tokens = total_input_tokens + total_output_tokens

    return {
        "request_count": request_count,
        "total_input_tokens": total_input_tokens,
        "total_output_tokens": total_output_tokens,
        "total_tokens": total_tokens,
        "average_input_tokens": (
            total_input_tokens / request_count if request_count else 0
        ),
        "average_output_tokens": (
            total_output_tokens / request_count if request_count else 0
        ),
        "average_tokens_per_request": (
            total_tokens / request_count if request_count else 0
        ),
    }
