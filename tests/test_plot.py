import os
import matplotlib.pyplot as plt
from src.plot import show
from src.mood_logger import log_mood
import pytest

@pytest.mark.skipif(os.getenv("CI") == "true", reason="Skip on CI")
def test_show_calls_pyplot_show(tmp_path, monkeypatch):
    file = tmp_path / "mood.csv"
    for rating in range(3):
        log_mood(rating + 1, file_path=str(file))

    called = []

    def fake_show():
        called.append(True)

    monkeypatch.setattr(plt, "show", fake_show)
    show(file_path=str(file))
    assert called
