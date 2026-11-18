# CareerAlign AI

A small resume and job-description comparison application built with Python and Gradio.

## What it currently does

- Accepts PDF and DOCX resumes.
- Extracts text from the uploaded file.
- Checks the resume and job description against a predefined skills catalogue.
- Shows detected, matching, and missing skills.
- Calculates a simple keyword-match percentage.
- Suggests learning links and a small set of rule-based career options.
- Creates a downloadable PDF analysis report.
- Includes an optional job-description summarisation button. To use it, configure an `HF_API_KEY` environment variable for the Hugging Face inference service. The rest of the matching workflow works without an API key.

## How matching works

The current matching logic is dictionary/keyword based. It looks for entries from `SKILLS_DB` in the extracted resume text and job-description text. It is a lightweight heuristic, not a trained semantic matching model, and the percentage should be treated as an indicative keyword score rather than a hiring prediction.

The cover-letter helper is currently a template function and is not presented as an AI-generated personalised letter in the user interface.

## Tech stack

- Python
- Gradio
- PyPDF2
- python-docx
- FPDF2
- Requests (optional Hugging Face summarisation call)

## Run locally

1. Install Python 3.10 or newer.
2. Clone this repository.
3. Install packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   python app.py
   ```

5. Open the local Gradio URL printed in the terminal.

Optional: set `HF_API_KEY` in your environment to enable job-description summarisation. Never commit an API token to GitHub.

## Free deployment on Render

1. Push this repository to GitHub.
2. In Render, choose **New + → Web Service** and connect this repository.
3. Use the repository root as the Root Directory.
4. Select **Python** as the runtime.
5. Set Build Command to `pip install -r requirements.txt`.
6. Set Start Command to `python app.py`.
7. Select the **Free** instance type and deploy.
8. Copy the public `onrender.com` URL after the first successful deployment.

The Render free service may sleep after 15 minutes without incoming traffic, and the first request after sleeping can take around a minute to wake up. Treat this as a portfolio/demo deployment, not a production service.

## Repository

https://github.com/Chhayasingh18/CareerAlign-AI
