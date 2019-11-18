from stock import create_app
from stock.models import db, Stock

app = create_app()


@app.shell_context_processor
def make_shell_context():
    """Create a shell context so that can use REPL."""
    return dict(app=app, db=db, Stock=Stock)


