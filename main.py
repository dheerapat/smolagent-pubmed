import os
from smolagents import ToolCallingAgent, OpenAIServerModel, ToolCollection, GradioUI
from mcp import StdioServerParameters
from smolagents.agents import CodeAgent

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
    agent = CodeAgent(tools=[*tool_collection.tools], model=model, additional_authorized_imports=["time", "numpy", "pandas"])
    ui = GradioUI(agent=agent)
    ui.launch()
    # agent.run("research a clinical study for me about medical intervention that can help lower weight in diabetes patient, summarized each intervention and citation properly")
