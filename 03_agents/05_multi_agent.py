import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Multi-Agent Systems in ADK

        https://google.github.io/adk-docs/agents/multi-agents/
        """
    )
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""## parent_agent""")
    return


@app.cell
def _():
    from google.adk.agents import LlmAgent, BaseAgent

    # Define individual agents.
    greeter = LlmAgent(name="greeter", model="gemini-2.0-flash")
    task_doer = BaseAgent(name="TaskExecutor")

    # Create parent agent and assign children via sub_agents.
    coordinator = LlmAgent(
        name="Coordinator",
        model="gemini-2.0-flash",
        description="I coordinate greetings and tasks.",
        sub_agents=[greeter, task_doer],
    )

    assert greeter.parent_agent == coordinator
    assert task_doer.parent_agent == coordinator
    return


if __name__ == "__main__":
    app.run()
