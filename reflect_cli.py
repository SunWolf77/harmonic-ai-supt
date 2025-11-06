# reflect_cli.py – SUPT Harmonic Terminal Reflection Console

import requests
from rich import print
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel

API_URL = "http://localhost:8000/reflect"

print("\n[bold cyan]SUPT Harmonic Reflection Console[/bold cyan]")
print("Type your prompt. Press Ctrl+C to exit.\n")

while True:
    try:
        user_input = Prompt.ask("[bold yellow]Prompt[/bold yellow]")
        payload = {"prompt": user_input}
        res = requests.post(API_URL, json=payload)

        if res.status_code != 200:
            print(f"[red]Error: {res.status_code}[/red] – {res.text}")
            continue

        data = res.json()

        print("\n[bold green]Original[/bold green]:", data['original_prompt'])
        print("[bold magenta]Repaired[/bold magenta]:", data['repaired_prompt'])

        # Score Table
        table = Table(title="SUPT Harmonic Scores", show_lines=True)
        table.add_column("Field", style="cyan")
        table.add_column("Score", justify="right")
        for k, v in data['scores'].items():
            bar = "█" * int(v * 20)
            table.add_row(k, f"{v:.2f} {bar}")
        print(table)

        print(Panel(f"[italic white]{data['supthint']}[/italic white]", title="[bold blue]supthint()[/bold blue]", expand=False))

    except KeyboardInterrupt:
        print("\n[bold red]Goodbye.[/bold red]")
        break
    except Exception as e:
        print(f"[red]Exception:[/red] {e}")
