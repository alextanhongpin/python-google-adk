import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a given city.


    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error message.
    """
    if city.lower() != "new york":
        return {
            "status": "error",
            "error_message": f"Weather report for {city} is not available.",
        }

    return {
        "status": "success",
        "report": "The weather in New York is sunny with a temperature of 25 degrees Celsius (41 degrees Fahrenheit).",
    }


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.
    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error message.
    """
    if city.lower() != "new york":
        return {
            "status": "error",
            "error_message": (f"Sorry, I don't have timezone information for {city}."),
        }

    tz = ZoneInfo("America/New_York")
    now = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

    return {
        "status": "success",
        "report": f"The current time in {city} is {now}."
    }



root_agent = Agent(
    name="weather_time_agent",
    # model=LiteLlm(model="ollama/gemma3:4b"),  # Standard LiteLLM format for Ollama
    model=LiteLlm(model="ollama/llama3.2"),  # Standard LiteLLM format for Ollama
    description=("Agent to answer questions about the time and weather in a city."),
    instruction=("I can answer questions about the time and weather in a city."),
    tools=[get_weather, get_current_time],
)
