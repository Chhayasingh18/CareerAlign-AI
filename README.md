# 🚀 CareerAlign AI 

**Empowering Creators and Professionals to Build Smarter Career Content with AI**


---

## 🚀 Overview

CareerAlign AI is designed for the creator economy: freelancers, content creators, students, and professionals seeking opportunities in today's AI-driven world. This hackathon submission uses advanced AI (Gradio, Hugging Face, OpenAI) to help users instantly match their resume to job descriptions, uncover skill gaps, access upskilling resources, and generate personalized cover letters—all with the ease and creativity that the AI Demos hackathon celebrates.

---

## ✨ Features

- **Resume & Job Description Analyzer:**  
  Upload your resume (PDF/DOCX) and a job posting to get a detailed AI-powered analysis.

- **Match Score Calculator:**  
  Instantly see how well your resume fits the chosen role (percentage match).

- **Skill Mapping for Creators:**  
  - Detect your current skills from resume  
  - Spot skills needed for the role  
  - View missing skills and resource suggestions to upskill

- **Smart Learning Resource Finder:**  
  AI-curated links to YouTube, docs, and online courses for every missing skill.

- **Career Path Suggestions:**  
  Discover alternative creative/professional roles aligned with your existing strengths.

- **Job Description Summarization:**  
  Advanced AI summarizes lengthy job posts for quick review—no more reading walls of text.

- **Professional PDF Report:**  
  Download a neat summary of your match analysis and recommendations.

- **Cover Letter Generator:**  
  Instantly generate a personalized cover letter for any company and role.

---

## 🛠️ How to Use

1. Upload your resume (PDF/DOCX)
2. Paste the job description
3. Click "Analyze Resume"  
   - View match score, skill analysis, and PDF summary  
   - Expand "Detailed Analysis" for upskilling links and career suggestions
4. Generate your custom cover letter
5. Summarize long job descriptions at the click of a button

---

## 🏗️ Technology Stack

- Python (Gradio, PyPDF2, python-docx, fpdf, requests)
- Hugging Face BART (Job summarization)
- OpenAI, spaCy (Skill extraction, AI features)
- Custom career suggestion logic

---

## 📦 Installation

   python -m venv venv

Activate venv (Windows)
venv\Scripts\activate

Or, macOS/Linux:
source venv/bin/activate

pip install gradio PyPDF2 python-docx fpdf requests


Set your Hugging Face API key:  
- Windows: `set HF_API_KEY=your_huggingface_api_key`
- macOS/Linux: `export HF_API_KEY=your_huggingface_api_key`

Run:  
python your_script_name.py


Open your browser at the Gradio link.

---

## 📄 Example Output

- **Resume-Role Match Score:** 82%
  > Indicates how well your resume aligns with the targeted creative or tech job.

- **Matching Skills:** Python, Prompt Engineering, Video Editing, Canva  
  > Skills found in both the resume and job description, making the candidate a strong fit for content-centric roles.

- **Missing Skills:** Social Media Management, Newsletter Automation  
  > Skills required for the position but not present—along with curated learning resources for each.

- **Recommended Learning Resources:**  
  - Social Media Management: [HubSpot Social Media Management Guide](https://www.hubspot.com/social-media-management)  
  - Newsletter Automation: [MailerLite Newsletter Automation Guide](https://www.mailerlite.com/blog/newsletter-automation-guide)

- **Career Suggestions:**  
  - Content Creator  
  - Video Producer  
  - Social Media Analyst  
  > Suggested based on the user’s detected skillset and creative strengths.

- **AI-Generated Cover Letter:**  
  *(A custom cover letter matching the candidate’s resume to the position, written in seconds and ready to copy or download.)*

- **Job Description Summary:**  
  > An instant, concise overview of a lengthy creative role, making it easier for creators to identify core requirements and opportunities.

---

CareerAlign AI’s output helps you create and optimize job application content with actionable, AI-driven insights—ideal for creators, marketers, and professionals in today’s digital workspace.

- Brings AI directly to the world of content creators and job seekers.
- Transforms traditional career content—resumes, cover letters—into creative, intelligent outputs.
- Makes upskilling, career discovery, and job applications engaging and efficient for everyone in the creator economy.

---

## 🤝 Contributing

Open for pull requests and feature suggestions—let’s expand the creative impact of CareerAlign AI!

---

**Demo Video:**  
https://drive.google.com/file/d/1gXlVoPsiF_CX3YcxN4b3yytxtn-gmcGN/view?usp=sharing

---


