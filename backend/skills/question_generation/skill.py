def generate_question(topic: str, difficulty: str = "beginner") -> dict[str, str]:
    topic = topic.strip()
    if not topic:
        raise ValueError("A topic is required")
    return {
        "title": f"{difficulty.title()} exercise: {topic}",
        "prompt": f"Write a program that demonstrates {topic}.",
        "difficulty": difficulty,
    }
