from typing import Any


def retrieve(records: list[dict[str, Any]], query: str, text_key: str = "text", limit: int = 5) -> list[dict[str, Any]]:
    terms = set(query.casefold().split())
    ranked = []
    for record in records:
        text = str(record.get(text_key, "")).casefold()
        score = sum(term in text for term in terms)
        if score:
            ranked.append((score, record))
    ranked.sort(key=lambda item: item[0], reverse=True)
    return [record for _, record in ranked[:limit]]
