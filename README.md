# 🚀 CareerAlign AI — Outsmart the Bots. Align with Your Dream Job.

**The Smartest Way to Match Your Resume to Your Dream Job!**
---

## 🚀 Overview

**CareerAlign AI** is an AI-powered web app that helps you instantly see how well your resume fits a job description—plus, it shows skill gaps, recommends learning resources, suggests career paths, and even writes a tailored cover letter for you!

No more guessing if your resume is a match. Upload your resume, paste the job description, and let CareerAlign AI do the heavy lifting.

---

## ✨ Features

- **Resume & Job Description Analyzer:**  
  Upload your resume (PDF/DOCX) and paste any job description to get a detailed analysis.

- **Match Score:**  
  Instantly see how closely your resume matches the job requirements, calculated as a percentage.

- **Skill Mapping:**  
  - *Your Skills*: Skills detected in your resume.
  - *Matching Skills*: Skills that overlap with the job description.
  - *Missing Skills*: Skills required by the job but missing from your resume.

- **Learning Resources:**  
  Get curated links to learn any missing skills.

- **Career Suggestions:**  
  Discover potential job roles based on your skillset.

- **Job Description Summarizer:**  
  Summarize long job descriptions with one click using advanced AI.

- **PDF Report:**  
  Download a professional report summarizing your match analysis.

- **Cover Letter Generator:**  
  Instantly create a personalized cover letter tailored to the job and company.

- **Modern UI:**  
  Clean, collapsible sections for easy navigation, powered by Gradio.

---

## 🛠️ How It Works

1. **Upload Your Resume:**  
   Drop a PDF or DOCX file in the Resume Input section.

2. **Paste Job Description:**  
   Copy-paste the job description into the provided box.

3. **Analyze:**  
   Click "Analyze Resume" to see your match score, skill breakdown, and get a downloadable PDF report.

4. **Detailed Analysis:**  
   Expand the "View Detailed Analysis" section to see:
   - All detected skills
   - Matching and missing skills
   - Learning resources for each missing skill
   - Career suggestions based on your strengths

5. **Cover Letter:**  
   Enter the job title and company, then click "Generate Cover Letter" to get a ready-to-use cover letter.

6. **Summarize Job Description (Optional):**  
   Use the "Summarize Description" button to get a concise summary of lengthy job postings.

---

## 🧩 Under the Hood

- **Python & Gradio** for the interactive web interface
- **PyPDF2** and **python-docx** for resume parsing
- **FPDF** for PDF report generation
- **Hugging Face BART** for job description summarization
- **Custom Skill Database** for skill extraction and mapping
- **Role Suggestions** based on detected skills
- **Learning Resources** mapped to each technical skill

---

## 📦 Installation & Usage

1. **Create a virtual environment (recommended):**
python -m venv venv

2. **Activate the virtual environment:**
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```

3. **Install the required dependencies:**
```
pip install gradio PyPDF2 python-docx fpdf requests
```

5. **Set your Hugging Face API key:**

The job description summarization feature uses the Hugging Face BART model API.  
Before running the app, you need to set your Hugging Face API key as an environment variable:

- On Windows:
  ```
  set HF_API_KEY=your_huggingface_api_key
  ```
- On macOS/Linux:
  ```
  export HF_API_KEY=your_huggingface_api_key
  ```

Replace `-copy your hugging face key here-` with your actual Hugging Face API key.  
*(You can get a free API key by signing up at huggingface.co)*

**In your code:**  
Make sure the line in your code that sets the headers uses your environment variable:
import os
headers = {"Authorization": "Bearer -copy your hugging face key here-"}

text

5. **Run the app:**
python your_script_name.py

text
*(Replace `your_script_name.py` with the name of your Python file.)*

6. **Open the app in your browser:**  
After running, Gradio will provide a local URL—click or copy it into your browser to use JobFit Analyzer.

---

## 📄 Example Output

- **Match Score:** 78%
- **Matching Skills:** Python, SQL, Machine Learning
- **Missing Skills:** AWS, Docker
- **Learning Resources:**  
- AWS: [AWS Training](https://aws.amazon.com/training/)
- Docker: [Docker Getting Started](https://docs.docker.com/get-started/)
- **Career Suggestions:** Data Analyst, Backend Developer
- **Cover Letter:**  
*(Auto-generated, ready to copy or download)*

---

## 💡 Why Use CareerAlign AI?

- **Save Time:** Instantly know your fit for any job.
- **Get Actionable Feedback:** See exactly what you’re missing—and how to improve.
- **Boost Your Applications:** Use tailored cover letters and skill insights to stand out.
- **Plan Your Learning:** Direct links to upskill where it matters most.

---

## 🤝 Contributing

Pull requests are welcome! If you have ideas for new features, bug fixes, or UI improvements, open an issue or submit a PR.
