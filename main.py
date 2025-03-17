import os
from smolagents import ToolCallingAgent, OpenAIServerModel, ToolCollection
from mcp import StdioServerParameters

server_parameters = StdioServerParameters(
    command="uvx",
    args=["--quiet", "pubmedmcp@0.1.3"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

model = OpenAIServerModel(
    model_id="anthropic/claude-3.7-sonnet",
    api_base="https://openrouter.ai/api/v1",
    api_key=os.environ["API_KEY"]
)

with ToolCollection.from_mcp(server_parameters) as tool_collection:
    agent = ToolCallingAgent(tools=[*tool_collection.tools], model=model)
    agent.run("Please find a remedy for hangover.")
