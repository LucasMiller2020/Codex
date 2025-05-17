import csv
from src.mood_logger import log_mood, latest_entries, MoodEntry

def test_log_mood_creates_file_and_writes_row(tmp_path):
    file = tmp_path / "mood.csv"
    # Log one mood entry
    log_mood(7, note="test-note", file_path=str(file))

    # File should now exist
    assert file.exists()

    # Check header + data row
    with file.open(newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    assert rows[0] == ["date", "rating", "note"]
    # rating and note should match what we logged
    assert rows[1][1] == "7"
    assert rows[1][2] == "test-note"

def test_latest_entries_returns_correct_dataclasses(tmp_path):
    file = tmp_path / "mood.csv"
    # No file yet → empty list
    assert latest_entries(n=3, file_path=str(file)) == []

    # Write several entries
    for rating in [1, 5, 3, 9]:
        log_mood(rating, file_path=str(file))

    # Ask for last 2 entries
    entries = latest_entries(n=2, file_path=str(file))
    assert len(entries) == 2
    # They should be MoodEntry instances with correct ratings
    assert all(isinstance(e, MoodEntry) for e in entries)
    assert [e.rating for e in entries] == [3, 9]
