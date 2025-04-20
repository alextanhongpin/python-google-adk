

import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # State
        https://google.github.io/adk-docs/sessions/state/#how-state-is-updated-recommended-methods
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    from llm import agentmaker
    from google.adk.sessions import InMemorySessionService, Session
    from google.adk.runners import Runner
    from google.genai.types import Content, Part
    return Content, InMemorySessionService, Part, Runner, agentmaker


@app.cell
def _(agentmaker):
    # Define agent with output_key
    greeting_agent = agentmaker(
        name="Greeter",
        instruction="Generate a short, friendly greeting.",
        output_key="last_greeting",  # Save response to state['last_greeting']
    )
    return (greeting_agent,)


@app.cell
def _(InMemorySessionService, Runner, greeting_agent):
    # --- Setup Runner and Session ---
    app_name, user_id, session_id = "state_app", "user1", "session1"
    session_service = InMemorySessionService()
    runner = Runner(
        agent=greeting_agent, app_name=app_name, session_service=session_service
    )
    session = session_service.create_session(
        app_name=app_name, user_id=user_id, session_id=session_id
    )
    print(f"Initial state: {session.state}")
    return app_name, runner, session_id, session_service, user_id


@app.cell
def _(Content, Part, app_name, runner, session_id, session_service, user_id):
    # --- Run the Agent ---
    # Runner handles calling append_event, which uses the output_key
    # to automatically create the state_delta.
    user_message = Content(role="user", parts=[Part(text="hello")])
    for event in runner.run(
        user_id=user_id, session_id=session_id, new_message=user_message
    ):
        if event.is_final_response():
            print(f"Agent responded.")  # Response text is also in event.content

    # --- Check Updated State ---
    updated_session = session_service.get_session(
        app_name=app_name, user_id=user_id, session_id=session_id
    )
    print(f"State after agent run: {updated_session.state}")
    # Expected output might include: {'last_greeting': 'Hello there! How can I help you today?'}
    return (updated_session,)


@app.cell
def _(updated_session):
    updated_session.state
    return


if __name__ == "__main__":
    app.run()
