from dataclasses import dataclass, asdict
from datetime import date
import csv
import json
from pathlib import Path
from typing import List, Optional

@dataclass
class MoodEntry:
    """Represents one logged mood entry."""
    date: str
    rating: int
    note: Optional[str] = None

# Default JSON data file stored at the repository root
DATA_FILE = Path(__file__).resolve().parent.parent / "moods.json"

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


def load_entries() -> List[MoodEntry]:
    """Load all mood entries from the JSON ``DATA_FILE``."""
    path = Path(DATA_FILE)
    if not path.exists():
        return []
    with path.open() as f:
        data = json.load(f)
    return [MoodEntry(**item) for item in data]


def save_entry(entry: MoodEntry) -> None:
    """Append ``entry`` to ``DATA_FILE``."""
    path = Path(DATA_FILE)
    entries = load_entries()
    entries.append(entry)
    with path.open("w") as f:
        json.dump([asdict(e) for e in entries], f)
