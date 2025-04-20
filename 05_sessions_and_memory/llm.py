from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
import litellm

litellm._turn_on_debug()

llama_model = LiteLlm(model="openai/llama3.2")


APP_NAME = 'myapp'
USER_ID = "user1234"
SESSION_ID = "user1234"
MODEL_ID = llama_model


def agentmaker(**kwargs):
    agent = Agent(
        model=MODEL_ID, **kwargs,
    )
    return agent

def runner(agent):
    # Session and Runner
    session_service = InMemorySessionService()
    session = session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )
    runner = Runner(
        agent=agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    # Agent Interaction
    def call_agent(query):
        content = types.Content(role="user", parts=[types.Part(text=query)])
        events = runner.run(
            user_id=USER_ID, session_id=SESSION_ID, new_message=content
        )

        for event in events:
            if event.is_final_response():
                final_response = event.content.parts[0].text
                print("Agent Response: ", final_response)

    return call_agent
