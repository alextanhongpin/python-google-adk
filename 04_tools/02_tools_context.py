

import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Tools Context

        https://google.github.io/adk-docs/tools/#tool-context
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    from google.adk.tools import ToolContext, FunctionTool
    from llm import agentmaker, runner


    def update_user_preference(
        preference: str, value: str, tool_context: ToolContext
    ):
        """Updates a user-specific preference."""
        user_prefs_key = "user:preferences"
        # Get current preferences or initialize if none exist
        preferences = tool_context.state.get(user_prefs_key, {})
        preferences[preference] = value
        # Write the updated dictionary back to the state
        tool_context.state[user_prefs_key] = preferences
        print(f"Tool: Updated user preference '{preference}' to '{value}'")
        return {"status": "success", "updated_preference": preference}


    pref_tool = FunctionTool(func=update_user_preference)

    agent = agentmaker(
        name="AssistantAgent",
        description="Update preference for the user",
        instruction="""When requested by the user, call the `update_user_preference` tool to set the user's preferences""",
        tools=[pref_tool],
    )


    print("Executing...")
    runner(agent)("set my theme preference to dark theme")
    # In an Agent:
    # my_agent = Agent(..., tools=[pref_tool])

    # When the LLM calls update_user_preference(preference='theme', value='dark', ...):
    # The tool_context.state will be updated, and the change will be part of the
    # resulting tool response event's actions.state_delta.
    return


if __name__ == "__main__":
    app.run()
