

import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Google Search

        https://google.github.io/adk-docs/tools/built-in-tools/#google-search
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    from google.adk.tools import google_search
    from llm import agentmaker, runner

    root_agent = agentmaker(
        name="basic_search_agent",
        description="Agent to answer questions using Google Search.",
        instruction="I can answer your questions by searching the internet. Just ask me anything!",
        # google_search is a pre-built tool which allows the agent to perform Google searches.
        tools=[google_search],
    )

    # Session and Runner

    runner(root_agent)("What is the latest AI news?")
    return


if __name__ == "__main__":
    app.run()
