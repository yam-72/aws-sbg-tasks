
import csv
from pathlib import Path

import numpy as np


DATA_FILE = Path(__file__).with_name("raw_data.csv")


def load_data(file_path):
    """Load student records from a CSV file."""
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def clean_data(raw_data):
    """Clean student records and remove duplicates."""
    cleaned_data = []
    seen = set()

    for row in raw_data:
        student = row["student"].strip().title()
        raw_score = row["score"].strip()

        if not student or not raw_score:
            continue

        try:
            score = float(raw_score)
        except ValueError:
            continue

        if not 0 <= score <= 100:
            continue

        record = (student, score)

        if record in seen:
            continue

        seen.add(record)
        cleaned_data.append({
            "student": student,
            "score": score
        })

    return cleaned_data


def analyze_scores(cleaned_data):
    """Calculate statistics using NumPy."""
    if not cleaned_data:
        print("No valid records to analyze.")
        return

    scores = np.array(
        [record["score"] for record in cleaned_data],
        dtype=float
    )

    print("\nData Analysis")
    print("-" * 30)
    print(f"Valid records: {len(cleaned_data)}")
    print(f"Average score: {np.mean(scores):.2f}")
    print(f"Median score: {np.median(scores):.2f}")
    print(f"Minimum score: {np.min(scores):.2f}")
    print(f"Maximum score: {np.max(scores):.2f}")
    print(f"Standard deviation: {np.std(scores):.2f}")


def main():
    """Run the complete data-processing workflow."""
    raw_data = load_data(DATA_FILE)

    print(f"Raw records: {len(raw_data)}")

    cleaned_data = clean_data(raw_data)

    print(f"Cleaned records: {len(cleaned_data)}")

    print("\nCleaned Dataset")
    print("-" * 30)

    for record in cleaned_data:
        print(record)

    analyze_scores(cleaned_data)


if __name__ == "__main__":
    main()
