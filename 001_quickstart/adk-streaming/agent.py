from google.adk.agents import Agent
from google.adk.tools import google_search


root_agent = Agent(
    name="basic_search_agent",
    # The Large Language Model (LLM) that agent will use.
    model="gemini-2.0-flash-exp",
    description="Agent to answer questions using Google Search.",
    # Instructions to set the agent's behavior.
    instruction="You are an expert researcher. You always stick to the facts.",
    # Add google_search tool to perform grounding with Google search.
    tools=[google_search],
)
