

import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Long Running Function Tool

        https://google.github.io/adk-docs/tools/function-tools/#2-long-running-function-tool
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    from google.adk.tools import LongRunningFunctionTool
    from llm import agentmaker, runner
    import time
    return LongRunningFunctionTool, agentmaker, runner, time


@app.cell
def _(LongRunningFunctionTool, agentmaker, runner, time):
    # 1. Define the generator function
    def process_large_file(file_path: str) -> dict:
        """
        Simulates processing a large file, yielding progress updates.

        Args:
          file_path: Path to the file being processed.

        Returns:
          A final status dictionary.
        """
        total_steps = 5

        # This dict will be sent in the first FunctionResponse
        yield {
            "status": "pending",
            "message": f"Starting processing for {file_path}...",
        }

        for i in range(total_steps):
            time.sleep(1)  # Simulate work for one step
            progress = (i + 1) / total_steps
            # Each yielded dict is sent in a subsequent FunctionResponse
            yield {
                "status": "pending",
                "progress": f"{int(progress * 100)}%",
                "estimated_completion_time": f"~{total_steps - (i + 1)} seconds remaining",
            }

        # This returned dict will be sent in the final FunctionResponse
        return {
            "status": "completed",
            "result": f"Successfully processed file: {file_path}",
        }


    # 2. Wrap the function with LongRunningFunctionTool
    long_running_tool = LongRunningFunctionTool(func=process_large_file)

    # 3. Use the tool in an Agent
    file_processor_agent = agentmaker(
        # Use a model compatible with function calling
        name="file_processor_agent",
        instruction="""You are an agent that processes large files. When the user provides a file path, use the 'process_large_file' tool. Keep the user informed about the progress based on the tool's updates (which arrive as function responses). Only provide the final result when the tool indicates completion in its final function response.""",
        tools=[long_running_tool],
    )
    runner(file_processor_agent)("Replace with a path to your file...")
    return


if __name__ == "__main__":
    app.run()
