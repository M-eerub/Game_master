from tools import roll_dice, generate_event
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def display_intro():
    console.print(Panel.fit("🎮 [bold magenta]Welcome to the Fantasy Adventure Game![/bold magenta]"))
    console.print("[cyan]You are a brave hero entering a magical realm... ✨[/cyan]\n")

def narrator_turn():
    event = generate_event()
    console.print(f"📖 [yellow]{event}[/yellow]")

def monster_turn():
    console.print("👹 [bold red]A monster appears! Prepare for battle![/bold red]")
    result = roll_dice(20)
    console.print(f"🎲 You rolled a [bold cyan]{result}[/bold cyan]!")
    if result >= 12:
        console.print("[green]You struck the monster down with a mighty blow! 🗡️[/green]")
    else:
        console.print("[red]The monster wounded you! 🩸 Retreat and heal.[/red]")

def item_turn():
    items = ["Healing Potion 🧪", "Golden Sword ⚔️", "Magic Ring 💍", "Mystery Box 🎁"]
    from random import choice
    found = choice(items)
    console.print(f"🎁 [bold green]You found: {found}[/bold green]")

def play_game():
    display_intro()
    while True:
        narrator_turn()
        action = Prompt.ask("\nWhat do you want to do?", choices=["fight", "explore", "rest", "quit"], default="explore")

        if action == "fight":
            monster_turn()
        elif action == "explore":
            item_turn()
        elif action == "rest":
            console.print("[blue]You take a short rest and recover your strength. 🛌[/blue]")
        elif action == "quit":
            console.print("[bold magenta]Thank you for playing, adventurer! 🌟[/bold magenta]")
            break

if __name__ == "__main__":
    play_game()
