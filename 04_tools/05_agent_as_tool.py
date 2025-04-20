

import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Agent-as-a-Tool

        https://google.github.io/adk-docs/tools/function-tools/#3-agent-as-a-tool
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    from google.adk.tools.agent_tool import AgentTool
    from llm import agentmaker, runner


    summary_agent = agentmaker(
        name="summary_agent",
        instruction="""You are an expert summarizer. Please read the following text and provide a concise summary.""",
        description="Agent to summarize text",
    )

    root_agent = agentmaker(
        name="root_agent",
        instruction="""You are a helpful assistant. When the user provides a text, use the 'summarize' tool to generate a summary. Always forward the user's message exactly as received to the 'summarize' tool, without modifying or summarizing it yourself. Present the response from the tool to the user.""",
        tools=[AgentTool(agent=summary_agent)],
    )

    long_text = """Quantum computing represents a fundamentally different approach to computation, 
    leveraging the bizarre principles of quantum mechanics to process information. Unlike classical computers 
    that rely on bits representing either 0 or 1, quantum computers use qubits which can exist in a state of superposition - effectively 
    being 0, 1, or a combination of both simultaneously. Furthermore, qubits can become entangled, 
    meaning their fates are intertwined regardless of distance, allowing for complex correlations. This parallelism and 
    interconnectedness grant quantum computers the potential to solve specific types of incredibly complex problems - such 
    as drug discovery, materials science, complex system optimization, and breaking certain types of cryptography - far 
    faster than even the most powerful classical supercomputers could ever achieve, although the technology is still largely in its developmental stages."""

    runner(root_agent)(long_text)
    return


if __name__ == "__main__":
    app.run()
