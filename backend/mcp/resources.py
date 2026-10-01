def list_resources() -> list[dict[str, str]]:
    return [
        {"uri": "lab://health", "name": "Service health"},
        {"uri": "lab://evaluation-policy", "name": "Evaluation policy"},
    ]
