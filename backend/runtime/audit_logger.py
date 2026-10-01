import json
import logging
from datetime import datetime, timezone


logger = logging.getLogger("evaluation.audit")


def log_event(event: str, **details: object) -> None:
    logger.info(json.dumps({
        "event": event,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "details": details,
    }, default=str))
