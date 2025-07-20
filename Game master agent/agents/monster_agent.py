from openai import AssistantAgent
from tools import roll_dice

MonsterAgent = AssistantAgent(
    name="MonsterAgent",
    instructions="Handles combat. Uses dice roll to determine outcome.",
    tools=[roll_dice],
    model="gpt-4o"
)
