import sys
import click
from src.mood_logger import log_mood, latest_entries
from src.plot import show as plot_show

@click.group()
def cli():
    """Mood tracker commands."""
    pass

@cli.command()
@click.argument("rating", type=int)
@click.argument("note", type=str, required=False)
def log(rating, note):
    """Log your mood with RATING (1–10) and optional NOTE."""
    log_mood(rating, note)
    click.echo(f"Logged mood {rating}{f' – {note}' if note else ''}")

@cli.command()
@click.option("--n", default=5, help="How many entries to show.")
def latest(n):
    """Show the last N mood entries."""
    entries = latest_entries(n)
    for e in entries:
        click.echo(f"{e.date}: {e.rating} – {e.note or ''}")

@cli.command()
def plot():
    """Plot the last 30 mood ratings."""
    plot_show()

if __name__ == "__main__":
    cli()
