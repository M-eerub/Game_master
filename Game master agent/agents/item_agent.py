from openai import AssistantAgent

ItemAgent = AssistantAgent(
    name="ItemAgent",
    instructions="Manages inventory, rewards, and items found.",
    model="gpt-4o"
)
