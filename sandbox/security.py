SUPPORTED_LANGUAGES = {"python", "cpp", "java"}


def validate_language(language: str) -> str:
    normalized = language.strip().lower()
    if normalized not in SUPPORTED_LANGUAGES:
        raise ValueError(f"Unsupported language: {language}")
    return normalized
