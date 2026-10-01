from fastapi import FastAPI
from backend.mcp.tools import list_mcp_tools
from backend.mcp.resources import list_resources


mcp_app = FastAPI(title="Programming Lab MCP")


@mcp_app.get("/tools")
def tools() -> list[dict[str, str]]:
    return list_mcp_tools()


@mcp_app.get("/resources")
def resources() -> list[dict[str, str]]:
    return list_resources()
