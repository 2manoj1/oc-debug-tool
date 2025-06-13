from typing import Dict
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text

console = Console()

def collect_inputs() -> Dict:
    console.print(Text("🔍 [bold cyan]OpenShift Debug CLI[/bold cyan]", justify="center"))
    console.print("\n[bold yellow]Answer the following to begin debugging:[/bold yellow]\n")

    kind = Prompt.ask("🧩 What do you want to debug?", choices=["pod", "deployment", "service"], default="pod")
    namespace = Prompt.ask("📦 Namespace", default="default")
    name = Prompt.ask("🔍 Resource name")
    action = Prompt.ask("📋 What info do you need?", choices=["describe", "logs", "events", "exec"], default="describe")

    console.print("\n[bold green]✅ Inputs collected![/bold green]")
    console.print(f"""
    [bold blue]Kind[/bold blue]: {kind}
    [bold blue]Namespace[/bold blue]: {namespace}
    [bold blue]Name[/bold blue]: {name}
    [bold blue]Action[/bold blue]: {action}
    """)

    return {"kind": kind, "namespace": namespace, "name": name, "action": action}
