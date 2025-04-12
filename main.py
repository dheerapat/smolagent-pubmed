import os
from smolagents import OpenAIServerModel, ToolCollection, GradioUI
from mcp import StdioServerParameters
from smolagents.agents import CodeAgent

server_parameters = StdioServerParameters(
    command="uvx",
    args=["--quiet", "pubmedmcp@latest"],
    env={"UV_PYTHON": "3.13", **os.environ},
)

model = OpenAIServerModel(
    model_id="meta-llama/llama-4-maverick",
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
        "efficacy of 81 mg aspirin vs 100 mg aspirin in cardiovascular disease",
    )
