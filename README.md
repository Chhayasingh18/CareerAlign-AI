# CareerAlign AI

A beginner-friendly Python project that compares a resume with a job description.

## Features
- Upload PDF or DOCX resumes and extract text.
- Compare resume skills with a pasted job description using a predefined keyword catalogue.
- Show an indicative keyword-match score, matching skills, missing skills and learning links.
- Download a PDF analysis report.
- Save the 20 most recent analyses in a small SQLite database.
- Optional job-description summarisation using a Hugging Face API token.

## Tech stack
Python, Gradio, SQLite, PyPDF2, python-docx and FPDF2.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Open the local URL printed in the terminal (usually http://127.0.0.1:7860).

## Deploy free on Hugging Face Spaces
1. Create a free account at https://huggingface.co/.
2. Choose **New Space** and give it a name such as `careeralign-ai`.
3. Select **Gradio** as the Space SDK and **CPU Basic** as the hardware.
4. Create the Space, then open its **Files** tab.
5. Upload `app.py` and `requirements.txt` from this repository.
6. The Space will install dependencies and build automatically. Open the running app when the build finishes.

## Database note
SQLite creates `careeralign.db` automatically. It is suitable for local use and a beginner demo. Free hosted Space storage may be reset when the Space is rebuilt or restarted, so this version does not promise permanent hosted history. A hosted database such as Supabase can be connected later if permanent history is needed.

## Important
The matching score is a simple keyword heuristic, not a trained AI model or a hiring prediction. The optional summary needs an `HF_API_KEY` secret; all other features work without it.

Repository: https://github.com/Chhayasingh18/CareerAlign-AI
