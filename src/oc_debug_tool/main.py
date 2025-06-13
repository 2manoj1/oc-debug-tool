import typer
from oc_debug_tool import login
from oc_debug_tool import debug
from oc_debug_tool.utils import check_oc_installed

app = typer.Typer()
app.command("login")(login.login)
app.command("debug")(debug.start)

if __name__ == "__main__":
    check_oc_installed()
    app()