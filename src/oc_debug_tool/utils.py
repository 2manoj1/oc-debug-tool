import shutil
import typer

def check_oc_installed():
    if not shutil.which("oc"):
        typer.secho("❌ 'oc' CLI is not installed or not in PATH.", fg=typer.colors.RED, err=True)
        typer.secho("🔧 Please install the OpenShift CLI before using this tool.", fg=typer.colors.YELLOW)
        raise typer.Exit(code=1)