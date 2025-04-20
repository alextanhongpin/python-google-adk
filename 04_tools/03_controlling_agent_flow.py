

import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Controlling Agent Flow


        https://google.github.io/adk-docs/tools/#controlling-agent-flow
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    from google.adk.tools import FunctionTool, ToolContext
    from llm import agentmaker, runner
    return FunctionTool, ToolContext, agentmaker, runner


@app.cell
def _(FunctionTool, ToolContext, agentmaker, runner):
    def check_and_transfer(query: str, tool_context: ToolContext) -> str:
        """Checks if the query requires escalation and transfers to another agent if needed."""
        print("Query:", query)

        if "urgent" in query.lower():
            print("Tool: Detected urgency, transferring to the support agent.")
            tool_context.actions.transfer_to_agent = "support_agent"
            return "Transferring to the support agent..."
        else:
            return f"Processed query: '{query}'. No further action needed."


    escalation_tool = FunctionTool(func=check_and_transfer)

    main_agent = agentmaker(
        name="main_agent",
        instruction="""You are the first point of contact for customer support of an analytics tool. Answer general queries. If the user indicates urgency, use the 'check_and_transfer' tool. Preserve the user's query when passing to the tool.""",
        tools=[escalation_tool],
    )

    support_agent = agentmaker(
        name="support_agent",
        instruction="""You are the dedicated support agent. Mentioned you are a support handler and please help the user with their urgent issue.""",
    )

    main_agent.sub_agents = [support_agent]

    runner(main_agent)("this is super urgent! i cant login at all")
    return


if __name__ == "__main__":
    app.run()
