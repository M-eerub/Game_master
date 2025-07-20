from openai import AssistantAgent
from tools import generate_event

NarratorAgent = AssistantAgent(
    name="NarratorAgent",
    instructions="Narrates the story and offers player choices.",
    tools=[generate_event],
    model="gpt-4o"
)
