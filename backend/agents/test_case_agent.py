from backend.models.test_case import TestCase
from backend.tools.test_case_tool import save_test_case


class TestCaseAgent:
    def add_test_case(self, test_case: TestCase) -> TestCase:
        return save_test_case(test_case)
