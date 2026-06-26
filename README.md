# NJZ EVM Fraud Detection

This repository contains a Flask-based survey app that collects voter details and opinions about state and national election fraud and candidate preferences.

## Contents

### 1. Political Survey (`app.py`)
A web app that collects voter details and preferences for:
- state chief minister candidates and party preferences
- national prime minister candidates and party preferences
- leader qualities for both state and national candidates
- EVM manipulation opinions for state and national elections

## Files
- `python_mini_project.py` - Main survey program
- `miniproject3.py` - Cafe chatbot with optional voice support
- `README.md` - Project documentation

## Contents

### 1. Political Survey (`app.py`)
A web app that collects voter details and preferences for:
- state chief minister candidates and party preferences
- national prime minister candidates and party preferences
- leader qualities for both state and national candidates
- EVM manipulation opinions for state and national elections

### 2. Cafe Chatbot (`miniproject3.py`)
A console-based cafe assistant that can:
- display the menu
- accept orders using `order <item> <qty>`
- calculate bills with discount and loyalty points
- answer price queries
- optionally use voice input/output when `speech_recognition` and `pyttsx3` are installed

## Getting Started

### Run locally
```bash
cd "c:\Users\KOLKAR NISHA\Desktop"
pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000/` in your browser.

### Run the cafe chatbot
```bash
cd "c:\Users\KOLKAR NISHA\Desktop"
python miniproject3.py
```

### Voice mode (optional)
Install the additional packages:
```bash
pip install SpeechRecognition pyttsx3
```
Then run `python miniproject3.py` and type `voice` to speak commands.

### Fee Management Checker (`fee_balance_check.py`)
This script checks student fee balances, validates payment dates, and can send reminder emails.

- Run locally:
  ```bash
  python fee_balance_check.py
  ```
- Default student records are loaded from `students.json` in the same folder.
- To use a different student data file, set the `STUDENT_DATA_FILE` environment variable.
- Email sending is disabled by default. Set `EMAIL_SENDING_ENABLED=true` to send real emails.
- Environment variables:
  - `EMAIL_SENDER`
  - `EMAIL_PASSWORD`
  - `SMTP_SERVER` (default: `smtp.gmail.com`)
  - `SMTP_PORT` (default: `465`)
  - `STUDENT_DATA_FILE`

Example for PowerShell:
```powershell
$env:EMAIL_SENDING_ENABLED = "true"
$env:EMAIL_SENDER = "solutions@algonex.co.in"
$env:EMAIL_PASSWORD = "your-app-password"
python fee_balance_check.py
```

Example for Bash / terminals:
```bash
export EMAIL_SENDING_ENABLED=true
export EMAIL_SENDER="solutions@algonex.co.in"
export EMAIL_PASSWORD="your-app-password"
python fee_balance_check.py
```

The default `students.json` contains the sample student records used by the script.

### Deploy to Heroku / Railway
1. Create an account on Heroku or Railway.
2. Push this repository to GitHub.
3. Connect the GitHub repo to your Heroku/Railway project.
4. Use the default `web: gunicorn app:app` command from `Procfile`.
5. Set the build runtime in `runtime.txt`.

### Notes
- The web app stores submissions in `survey.db`.
- State input is normalized for case and spacing, and suggestions are given for misspellings.
- You can later wrap this web app as a mobile app or a PWA for Play Store submission.
