import os
import typer
from rich.console import Console
import subprocess
from oc_debug_tool.utils import check_oc_installed

console = Console()

def is_logged_in():
    try:
        subprocess.run(["oc", "whoami"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def login(
    token: str = typer.Option(None, help="OpenShift token", envvar="OC_TOKEN"),
    server: str = typer.Option(None, help="OpenShift server URL", envvar="OC_SERVER")
):
    check_oc_installed()
    if not token or not server:
        console.print("[bold red]❌ Token and server must be provided via options or environment variables[/bold red]")
        raise typer.Exit(1)

    console.print(f"[bold green]🔐 Logging in to OpenShift...[/bold green]")
    try:
        subprocess.run(
            ["oc", "login", f"--token={token}", f"--server={server}"],
            check=True,
            capture_output=True,
            text=True
        )
        console.print("[bold green]✅ Login successful![/bold green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Login failed:[/bold red] {e.stderr}")
        raise typer.Exit(1)
