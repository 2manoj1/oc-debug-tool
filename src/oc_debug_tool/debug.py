import typer
from rich.console import Console
from oc_debug_tool.prompts import collect_inputs
from oc_debug_tool.actions import run_debug
from oc_debug_tool.login import is_logged_in
from oc_debug_tool.utils import check_oc_installed

console = Console()

def start():
    check_oc_installed()
    if not is_logged_in():
        console.print("[bold red]❌ Not logged in. Please run `oc-debug login` first.[/bold red]")
        raise typer.Exit(1)

    console.print("[bold cyan]Welcome to OpenShift Debug CLI![/bold cyan]")
    params = collect_inputs()
    run_debug(params)
