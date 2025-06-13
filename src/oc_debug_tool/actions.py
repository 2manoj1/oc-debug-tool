import subprocess
from rich.console import Console
from rich.syntax import Syntax

console = Console()

def run_debug(params):
    kind = params["kind"]
    name = params["name"]
    ns = params["namespace"]
    action = params["action"]

    cmd = ["oc", action, f"{kind}/{name}", "-n", ns] if action != "logs" else ["oc", "logs", f"{kind}/{name}", "-n", ns]
    console.print(f"[bold yellow]Running: {' '.join(cmd)}[/bold yellow]")

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode:
        console.print(f"[red]Error:[/red] {result.stderr}")
    else:
        console.print(Syntax(result.stdout, "yaml" if action == "describe" else "bash"))
