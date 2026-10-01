def list_mcp_tools() -> list[dict[str, str]]:
    return [
        {"name": "get_question", "description": "Retrieve a question by ID"},
        {"name": "get_test_cases", "description": "List test cases for a question"},
        {"name": "evaluate_submission", "description": "Run the evaluation workflow"},
    ]
