

import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Session

        https://google.github.io/adk-docs/sessions/session/
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    from google.adk.sessions import InMemorySessionService, Session

    # Create a simple session to examine its properties
    temp_service = InMemorySessionService()
    example_session: Session = temp_service.create_session(
        app_name="my_app",
        user_id="example_user",
        state={"initial_key": "initial_value"},  # State can be initialized
    )

    print(f"--- Examining Session Properties ---")
    print(f"ID (`id`):                {example_session.id}")
    print(f"Application Name (`app_name`): {example_session.app_name}")
    print(f"User ID (`user_id`):         {example_session.user_id}")
    print(
        f"State (`state`):           {example_session.state}"
    )  # Note: Only shows initial state here
    print(
        f"Events (`events`):         {example_session.events}"
    )  # Initially empty
    print(
        f"Last Update (`last_update_time`): {example_session.last_update_time:.2f}"
    )
    print(f"---------------------------------")

    # Clean up (optional for this example)
    temp_service.delete_session(
        app_name=example_session.app_name,
        user_id=example_session.user_id,
        session_id=example_session.id,
    )
    return (Session,)


@app.cell
def _(Session):
    # Requires: pip install google-adk[database]
    from google.adk.sessions import DatabaseSessionService

    # Example using a local SQLite file:
    db_url = "sqlite:///./my_agent_data.db"
    session_service = DatabaseSessionService(db_url=db_url)
    db_session: Session = session_service.create_session(
        app_name="my_app",
        user_id="example_user",
        state={"initial_key": "initial_value"},  # State can be initialized
    )
    return


@app.cell
def _():
    import sqlalchemy

    DATABASE_URL = "sqlite:///my_agent_data.db"
    engine = sqlalchemy.create_engine(DATABASE_URL)
    return (engine,)


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT name FROM sqlite_master WHERE type='table';
        """,
        engine=engine
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        select * from sessions;
        """,
        engine=engine
    )
    return


if __name__ == "__main__":
    app.run()
