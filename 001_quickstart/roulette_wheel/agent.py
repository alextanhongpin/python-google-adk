import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


def roulette_wheel(square: int) -> str:
    """Checks if the square is a winner
    Args:
        square (int): The square selected by suser

    Returns:
        str: Returns 'winner' if the square is 18, otherwise 'loser'.
    """
    return "winner" if square == 18 else "loser"


# TODO: native openai https://github.com/google/adk-python/issues/27
os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_BASE_URL")

model = os.getenv("CHAT_MODEL", "llama3.2")
root_agent = Agent(
    name="roulette_wheel_agent",
    model=LiteLlm(model="openai/" + model),  # Standard LiteLLM format for Ollama
    description=("Agent to check if the user is a winner in roulette."),
    instruction=(
        "Use the roulette_wheel function to check if the user is a winner based on the number they provide."
    ),
    tools=[roulette_wheel],  # List of tools the agent can use
)
