# delegation-tracker

A simple Python tool to track delegation records from a CSV file.

## Features

- Reads delegation records from CSV
- Calculates total delegated amount
- Summarizes totals by validator
- Shows recent records
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

Run:
python3 src/tracker.py

## Roadmap

- Add sorting by date
- Add CSV path argument
- Add exportable summary output
