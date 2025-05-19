from datetime import datetime
from matplotlib import pyplot as plt
from .mood_logger import load_entries


def show(*, file_path: str = "mood.csv") -> None:
    """Display a line chart of the last 30 mood entries."""
    entries = load_entries(file_path=file_path)[-30:]
    if not entries:
        return
    dates = [datetime.fromisoformat(e.date) for e in entries]
    ratings = [e.rating for e in entries]
    plt.plot(dates, ratings, marker="o")
    plt.xlabel("Date")
    plt.ylabel("Rating")
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.show()
