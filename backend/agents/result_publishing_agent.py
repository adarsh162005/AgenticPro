from backend.models.result import Result
from backend.tools.result_tool import publish_result


class ResultPublishingAgent:
    def publish(self, result: Result) -> Result:
        return publish_result(result)
