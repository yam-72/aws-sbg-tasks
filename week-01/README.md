# Week 01: Student Performance Data Processor

## Overview

This project is a small Python data-processing application that loads student records from a CSV file, cleans the data using Python functions, and calculates descriptive statistics using NumPy.

## Objectives

- Read data from a CSV file.
- Clean and validate records using reusable functions.
- Remove duplicate records.
- Process numerical data with NumPy.
- Practice Python virtual environments and dependency management.
- Run the application locally and in Google Colab.

## Project Files

- `student_performance_processor.py` — Standalone Python application.
- `student_performance_processor.ipynb` — Google Colab notebook containing explanations, code, and outputs.
- `raw_data.csv` — Sample dataset containing student names and scores.

## Data-Cleaning Rules

1. Remove leading and trailing whitespace from student names.
2. Standardize student-name capitalization.
3. Skip records with missing names or scores.
4. Skip non-numeric scores and scores outside the 0–100 range.
5. Remove duplicate records based on the normalized student name and score.
6. Preserve valid scores, including zero.

## How to Run

From the repository root, activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the dependencies if necessary:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
python week-01/student_performance_processor.py
```

## Expected Results

The sample dataset contains seven raw records. After cleaning, five valid records remain.

- Average score: 65.20
- Median score: 78.00
- Minimum score: 0.00
- Maximum score: 91.00
- Population standard deviation: approximately 33.22

## Learning Outcomes

This assignment demonstrates CSV file handling, Python functions, string processing, data validation, duplicate removal, NumPy arrays, descriptive statistics, and the use of a virtual environment.
