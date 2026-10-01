from backend.skills.code_similarity.skill import similarity


class SimilarityAgent:
    def compare(self, source_a: str, source_b: str) -> float:
        return similarity(source_a, source_b)
