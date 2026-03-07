# delegation-tracker

A simple Python tool to track delegation records from a CSV file.

## Features

- Reads delegation records from CSV
- Calculates total delegated amount
- Summarizes totals by validator
- Sorts records by date
- Shows recent records
- Handles missing CSV input gracefully
- Supports custom CSV path input
- Easy to run in WSL or Ubuntu

## Structure

- src/ -> Python source files
- data/ -> sample CSV data
- docs/ -> usage notes
- examples/ -> sample output

## Main Script

### tracker.py
Reads a CSV file with delegation records and prints a summary.

## Usage

Run with default sample data:
python3 src/tracker.py

Run with a custom CSV path:
python3 src/tracker.py data/delegations.csv

## Roadmap

- Add exportable summary output
- Add validator filtering
- Add summary by date range
