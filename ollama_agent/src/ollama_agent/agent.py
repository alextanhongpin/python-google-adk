from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm


def make_agent(model="ollama_chat/llama3.2", **kwargs):
    args = dict(
        model=LiteLlm(model=model),  # LiteLLM model string format
        name="root_agent",
        description="Answer the user's query",
        instruction="You are a helpful assistant",
    )

    # --- Example Agent using Ollama's llama3.2 ---
    return LlmAgent(**(args | kwargs))
