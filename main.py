import os
from smolagents import OpenAIServerModel, ToolCollection, GradioUI
from mcp import StdioServerParameters
from smolagents.agents import CodeAgent

server_parameters = StdioServerParameters(
    command="uvx",
    args=["--quiet", "pubmedmcp@0.1.3"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

model = OpenAIServerModel(
    model_id="meta-llama/llama-3.3-70b-instruct",
    api_base="https://openrouter.ai/api/v1",
    api_key=os.environ["API_KEY"],
)

with ToolCollection.from_mcp(server_parameters) as tool_collection:
    agent = CodeAgent(
        tools=[*tool_collection.tools],
        model=model,
        additional_authorized_imports=["time", "numpy", "pandas"],
    )
    # ui = GradioUI(agent=agent)
    # ui.launch()
    agent.run(
        "summarized how obstructive sleep apnea affect cognitive function. citation properly in final answer"
    )
