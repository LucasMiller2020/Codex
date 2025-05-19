from datetime import date
import click
from src.mood_logger import MoodEntry, save_entry, load_entries

@click.group()
def cli():
    """Mood tracker commands."""
    pass

@cli.command()
@click.argument("rating", type=int)
@click.argument("note", type=str, required=False)
def log(rating, note):
    """Log your mood with RATING (1–10) and optional NOTE."""
    entry = MoodEntry(date.today().isoformat(), rating, note)
    save_entry(entry)
    click.echo("Logged!")

@cli.command()
def latest():
    """Show the most recent mood entry."""
    entries = load_entries()
    if not entries:
        click.echo("No entries found.")
        return
    e = entries[-1]
    click.echo(f"{e.date}: {e.rating}{f' – {e.note}' if e.note else ''}")

if __name__ == "__main__":
    cli()
