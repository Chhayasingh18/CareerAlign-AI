# CareerAlign AI

**Live demo:** https://huggingface.co/spaces/Chhaya3008/careeralign-ai

CareerAlign AI is a beginner-friendly Python web application that compares a resume with a job description and highlights relevant skills and possible skill gaps.

## Features

- Upload a resume in PDF or DOCX format.
- Paste a job description.
- Extract skills from the resume and job description using a predefined keyword list.
- Calculate an indicative keyword-match percentage.
- Display matching skills and skills to improve.
- Suggest career paths and learning resources based on detected skills.
- Download a PDF analysis report.
- Save recent analysis results in a local SQLite database and view recent history.
- Optional job-description summarisation using a Hugging Face API token.

## Tech stack

- **Language:** Python
- **UI:** Gradio
- **Database:** SQLite
- **Document parsing:** PyPDF2 and python-docx
- **PDF report:** FPDF2
- **Hosting:** Hugging Face Spaces (ZeroGPU)

## Run locally

Python 3.10+ is recommended.

```bash
pip install -r requirements.txt
python app.py
```

Open the local URL printed in the terminal, usually http://127.0.0.1:7860.

## Deployment

The application is deployed on Hugging Face Spaces:

https://huggingface.co/spaces/Chhaya3008/careeralign-ai

To create your own Space:
1. Create a new Space and select the Gradio SDK.
2. Choose an available free hardware option for your account.
3. Upload `app.py` and `requirements.txt` to the Space.
4. Hugging Face installs the dependencies and starts the app automatically.

## Database note

The app creates `careeralign.db` automatically using SQLite. This is a lightweight database suitable for a beginner project and local demonstrations. On free hosted Spaces, local storage may not be permanent across rebuilds or restarts; use a managed database if permanent cloud history is required.

## How the matching works

The current matching score is a simple keyword-based comparison using a predefined skills list. It is an indicative score for learning and demonstration purposes, not a trained machine-learning model, semantic AI evaluation, ATS certification, or a hiring prediction.

## Optional summarisation

The job-description summarisation feature requires an `HF_API_KEY` environment secret. Resume parsing, keyword matching, skill-gap results and PDF report generation do not require that API key.

## Repository

https://github.com/Chhayasingh18/CareerAlign-AI
