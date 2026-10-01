import re


def similarity(left: str, right: str) -> float:
    left_tokens = set(re.findall(r"[A-Za-z_][A-Za-z_0-9]*|\d+|[^\s]", left))
    right_tokens = set(re.findall(r"[A-Za-z_][A-Za-z_0-9]*|\d+|[^\s]", right))
    union = left_tokens | right_tokens
    return len(left_tokens & right_tokens) / len(union) if union else 1.0
