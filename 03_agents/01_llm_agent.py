import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # LLM Agent

        https://google.github.io/adk-docs/agents/llm-agents/
        """
    )
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    from google.adk.agents import LlmAgent
    from google.genai import types

    # Define a tool function
    def get_capital_city(country: str) -> str:
        """Retrieves the capital city for a given country."""
        # Replace with actual logic (e.g., API call, database lookup)
        capitals = {"france": "Paris", "japan": "Tokyo", "canada": "Ottawa"}
        return capitals.get(
            country.lower(), f"Sorry, I don't know the capital of {country}."
        )

    # Defining a simple agent
    capital_agent = LlmAgent(
        # Basic identity.
        model="gemini-2.0-flash",
        name="capital_agent",
        description="Answers user questions about the capital city of the given country",
        # Guiding the agent.
        instruction="""You are an agent that provides the capital city of a country.
    When a user asks for the capital of a country:
    1. Identify the country name from the user's query.
    2. Use the `get_capital_city` tool to find the capital.
    3. Respond clearly to the user, stating the capital city.
    Example Query: "What's the capital of France?"
    Example Response: "The capital of France is Paris."
    """,
        # Equiping the agent.
        tools=[get_capital_city],
        # Fine-tuning LLM Generation.
        generate_content_config=types.GenerateContentConfig(
            temperature=0.2,  # More deterministic output
            max_output_tokens=250,
        ),
    )
    return (LlmAgent,)


@app.cell
def _(mo):
    mo.md(r"""## Structuring Data (`input_schema`, `output_schema`, `output_key`)""")
    return


@app.cell
def _(LlmAgent):
    from pydantic import BaseModel, Field

    class CapitalOutput(BaseModel):
        capital: str = Field(description="The capital of the country")

    structured_capital_agent = LlmAgent(
        # ... name, model, description
        instruction="""You are a Capital Information Agent. Given a country, respond ONLY with a JSON object containing the capital. Format: {"capital": "capital_name"}""",
        output_schema=CapitalOutput,  # Enforce JSON output
        output_key="found_capital",  # Store result in state['found_capital']
        # Cannot use tools=[get_capital_city] effectively here
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Managing Context (`include_contents`)""")
    return


@app.cell
def _(LlmAgent):
    stateless_agent = LlmAgent(
        name="stateless_agent",
        # ... other params
        include_contents="none",
    )
    return


if __name__ == "__main__":
    app.run()
