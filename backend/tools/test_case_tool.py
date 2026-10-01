from backend.models.test_case import TestCase


_test_cases: dict[str, TestCase] = {}


def get_test_cases(question_id: str) -> list[TestCase]:
    return [case for case in _test_cases.values() if case.question_id == question_id]


def save_test_case(test_case: TestCase) -> TestCase:
    _test_cases[test_case.id] = test_case
    return test_case
