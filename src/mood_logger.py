from dataclasses import dataclass
from datetime import date
import csv
from pathlib import Path
from typing import List, Optional

@dataclass
class MoodEntry:
    """Represents one logged mood entry."""
    date: str
    rating: int
    note: Optional[str] = None

def log_mood(
    rating: int,
    note: Optional[str] = None,
    *,
    file_path: str = "mood.csv"
) -> None:
    """
    Append a mood entry to a CSV file.
    
    Creates the file with headers if it doesn't exist.
    """
    path = Path(file_path)
    write_header = not path.exists()
    with path.open("a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if write_header:
            writer.writerow(["date", "rating", "note"])
        writer.writerow([date.today().isoformat(), rating, note or ""])

def latest_entries(
    n: int = 5,
    *,
    file_path: str = "mood.csv"
) -> List[MoodEntry]:
    """
    Return the last `n` mood entries from the CSV file.
    
    If the file doesn't exist, returns an empty list.
    """
    path = Path(file_path)
    if not path.exists():
        return []
    with path.open(newline="") as csvfile:
        rows = list(csv.DictReader(csvfile))
    entries = [
        MoodEntry(row["date"], int(row["rating"]), row.get("note") or None)
        for row in rows
    ]
    return entries[-n:]

def load_entries(*, file_path: str = "mood.csv") -> List[MoodEntry]:
    """Return all mood entries from the CSV file."""
    path = Path(file_path)
    if not path.exists():
        return []
    with path.open(newline="") as csvfile:
        rows = list(csv.DictReader(csvfile))
    return [
        MoodEntry(row["date"], int(row["rating"]), row.get("note") or None)
        for row in rows
    ]
