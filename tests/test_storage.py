from datetime import date
from src import mood_logger


def test_save_and_load_round_trip(tmp_path, monkeypatch):
    data_file = tmp_path / "moods.json"
    monkeypatch.setattr(mood_logger, "DATA_FILE", data_file)

    entry = mood_logger.MoodEntry(date.today().isoformat(), 8, "feeling good")
    mood_logger.save_entry(entry)

    assert data_file.exists()

    loaded = mood_logger.load_entries()
    assert loaded == [entry]
