# Arabic Text Analyzer

A simple Python CLI tool that reads Arabic text from a CSV file, cleans the text, and generates a JSON report containing the total word count and the 20 most frequent words.

## Features

- Read Arabic text from a CSV file.
- Remove emojis, punctuation, and Arabic diacritics.
- Normalize Arabic Alef characters and remove Tatweel.
- Count the total number of words.
- Find the 20 most frequent words.
- Export the results to a JSON file.
- Handle missing CSV files and missing text columns.

## Requirements

- Python 3
- emoji library

## Installation

1. Clone or download the project.
2. Open the project folder in a terminal.
3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

5. Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python main.py
```

The program reads `ar_text_data.csv` and generates `report.json`.

The CSV file must contain a column named `text`.

## Output

The generated JSON report contains:

- `total_words`: Total number of words after cleaning.
- `top_20_words`: The 20 most frequent words and their frequencies.

## Project Files

- `main.py` — Main Python program.
- `ar_text_data.csv` — Input CSV dataset.
- `requirements.txt` — Required external libraries.
- `report.json` — Generated analysis report.

## Error Handling

The program displays an error message if the CSV file does not exist or if the required `text` column is missing.