# Arabic Text Analyzer

A Python-based tool that reads Arabic text from a CSV file, cleans the text, and generates a JSON report containing the total word count and the 20 most frequent words.

The project supports both a Command Line Interface (CLI) and a REST API built with FastAPI.

## Features

- Read Arabic text from a CSV file.
- Remove emojis, punctuation, and Arabic diacritics.
- Normalize Arabic Alef characters and remove Tatweel.
- Count the total number of words.
- Find the 20 most frequent words.
- Export the results to a JSON file.
- Upload CSV files through a REST API.
- Return analysis results as a JSON response.
- Validate uploaded files and handle invalid requests.
- Automatically manage temporary uploaded files.
- Test API endpoints using Swagger UI.

## Technologies

- Python
- FastAPI
- Uvicorn
- Emoji
- Swagger UI

## Requirements

- Python 3
- emoji
- fastapi
- uvicorn
- python-multipart

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

## CLI Usage

Run the program:

```bash
python main.py
```

The program reads `ar_text_data.csv` and generates `report.json`.

The CSV file must contain a column named `text`.

## API Usage

Start the FastAPI server:

```bash
uvicorn api:app --reload
```

The server will be available at:

http://127.0.0.1:8000

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Check if the API is running |
| POST | /analyze | Upload and analyze a CSV file |

## Testing with Swagger UI

1. Start the FastAPI server.
2. Open http://127.0.0.1:8000/docs
3. Select the POST /analyze endpoint.
4. Click Try it out.
5. Upload a CSV file.
6. Click Execute.
7. View the JSON response.

## Output

The generated JSON report contains:

- `total_words`: Total number of words after cleaning.
- `top_20_words`: The 20 most frequent words and their frequencies.

Example response (shortened):

```json
{
    "total_words": 456,
    "top_20_words": [
        ["في", 14],
        ["من", 11]
    ]
}
```

## Error Handling

The API validates uploaded files before processing them.

| Status Code | Description |
|-------------|-------------|
| 200 | Successful analysis |
| 400 | Invalid file extension |
| 400 | Empty uploaded file |
| 400 | Missing required text column |
| 422 | Missing required file upload |

## Project Files

- `main.py` — Core text cleaning and analysis functions, and CLI execution.
- `api.py` — FastAPI server, API endpoints, and file validation.
- `ar_text_data.csv` — Input CSV dataset.
- `requirements.txt` — Required external libraries.
- `report.json` — Generated CLI analysis report.
- `README.md` — Project documentation.
- `.gitignore` — Files excluded from version control.

## Automated API Testing

The project includes automated API tests using Pytest
and FastAPI TestClient.

### Test Cases

- Home endpoint validation.
- Valid CSV file upload and analysis.
- Invalid file extension handling.
- Empty file handling.
- Missing text column handling.
- Arabic text cleaning and word count accuracy.

### Running Tests

To run all automated tests:

```bash
python -m pytest -v
```

### Test Results

- Total Tests: 6
- Passed: 6
- Failed: 0
- Success Rate: 100%
- Execution Time: 0.86 seconds