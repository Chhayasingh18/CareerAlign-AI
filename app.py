import gradio as gr
from PyPDF2 import PdfReader
from docx import Document
from fpdf import FPDF
import requests
from collections import Counter
import re

SKILLS_DB = [
    "Python", "Java", "C++", "JavaScript", "SQL", "R", "MATLAB",
    "Machine Learning", "Data Analysis", "Pandas", "NumPy", "TensorFlow", "PyTorch",
    "AWS", "Azure", "Google Cloud", "Docker", "Kubernetes",
    "HTML", "CSS", "React", "Django", "Flask",
    "Git", "GitHub", "JIRA", "Excel", "PowerPoint"
]

RESOURCES = {
    "Python": "https://www.learnpython.org/",
    "Java": "https://www.learnjavaonline.org/",
    "C++": "https://www.learncpp.com/",
    "JavaScript": "https://javascript.info/",
    "SQL": "https://www.w3schools.com/sql/",
    "R": "https://cran.r-project.org/manuals.html",
    "MATLAB": "https://matlabacademy.mathworks.com/",
    "Machine Learning": "https://www.coursera.org/learn/machine-learning",
    "Data Analysis": "https://www.datacamp.com/courses/data-analysis-in-python",
    "Pandas": "https://pandas.pydata.org/docs/getting_started/index.html",
    "NumPy": "https://numpy.org/devdocs/user/quickstart.html",
    "TensorFlow": "https://www.tensorflow.org/tutorials",
    "PyTorch": "https://pytorch.org/tutorials/",
    "AWS": "https://aws.amazon.com/training/",
    "Azure": "https://learn.microsoft.com/en-us/training/azure/",
    "Google Cloud": "https://cloud.google.com/training",
    "Docker": "https://docs.docker.com/get-started/",
    "Kubernetes": "https://kubernetes.io/docs/tutorials/",
    "HTML": "https://developer.mozilla.org/en-US/docs/Web/HTML",
    "CSS": "https://developer.mozilla.org/en-US/docs/Web/CSS",
    "React": "https://reactjs.org/tutorial/tutorial.html",
    "Django": "https://docs.djangoproject.com/en/stable/intro/tutorial01/",
    "Flask": "https://flask.palletsprojects.com/en/2.0.x/tutorial/",
    "Git": "https://git-scm.com/doc",
    "GitHub": "https://docs.github.com/en/get-started",
    "JIRA": "https://www.atlassian.com/software/jira/guides",
    "Excel": "https://support.microsoft.com/en-us/excel",
    "PowerPoint": "https://support.microsoft.com/en-us/powerpoint"
}

def extract_text(file):
    text = ""
    if not file:
        return ""
    filepath = file.name
    if filepath.endswith('.pdf'):
        reader = PdfReader(filepath)
        for page in reader.pages:
            txt = page.extract_text()
            if txt:
                text += txt + "\n"
    elif filepath.endswith('.docx'):
        doc = Document(filepath)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text.lower()

def suggest_roles(skill):
    roles_map = {
        "Python": ["Backend Developer", "Data Analyst"],
        "Machine Learning": ["ML Engineer", "Data Scientist"],
        "AWS": ["Cloud Engineer", "DevOps Engineer"],
        "Docker": ["DevOps Engineer"],
        "Flask": ["Backend Developer", "Web Developer"],
        "SQL": ["Database Admin", "Data Analyst"],
        "Kubernetes": ["Cloud Architect"],
        "Git": ["Software Engineer"]
    }
    return roles_map.get(skill, [])

def generate_pdf(your_skills, matching_skills, missing_skills, learning_resources, career_suggestions, match_score):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "AI Resume & Job Match Report", 0, 1, 'C')
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"Match Score: {match_score}%", 0, 1, 'C')
    pdf.ln(5)
    def write_section(title, content_list):
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, title, ln=1)
        pdf.set_font("Arial", size=11)
        if content_list:
            for item in content_list:
                pdf.multi_cell(0, 8, "- " + str(item))
        else:
            pdf.cell(0, 8, "None", ln=1)
        pdf.ln(5)
    write_section("Your Skills:", your_skills)
    write_section("Matching Skills:", matching_skills)
    write_section("Missing Skills:", missing_skills)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Learning Resources:", ln=1)
    pdf.set_font("Arial", size=11)
    if learning_resources:
        for skill, link in learning_resources.items():
            pdf.multi_cell(0, 8, f"{skill}: {link}")
    else:
        pdf.cell(0, 8, "None", ln=1)
    pdf.ln(5)
    write_section("Career Suggestions:", career_suggestions)
    path = "resume_job_match_report.pdf"
    pdf.output(path)
    return path

def summarize_job_description(job_desc):
    if not job_desc.strip():
        return job_desc
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": "Bearer -copy your hugging face key here-"}
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": job_desc})
        if response.status_code == 200:
            return response.json()[0]['summary_text']
        return job_desc
    except:
        return job_desc

def calculate_match_score(matching_skills, missing_skills):
    total_relevant = len(matching_skills) + len(missing_skills)
    if total_relevant == 0:
        return 0
    return int((len(matching_skills) / total_relevant) * 100)

def extract_keywords(text, n=10):
    words = re.findall(r'\b\w{4,}\b', text.lower())
    common_words = set(['with', 'this', 'that', 'have', 'will', 'your', 'team', 'work'])
    filtered = [word for word in words if word not in common_words and not word.isdigit()]
    return [word for word, count in Counter(filtered).most_common(n)]

def generate_cover_letter(job_title, company, matching_skills):
    if not job_title:
        job_title = "the position"
    if not company:
        company = "your company"
    skills_list = ", ".join(matching_skills[:5]) if matching_skills else "relevant skills"
    return f"""
Dear Hiring Manager,

I'm excited to apply for the {job_title} position at {company}. 
With my experience in {skills_list}, I believe I'd be a great fit for this role.

[Your personal introduction here]

Looking forward to the opportunity to discuss how my skills align with your needs.

Best regards,
[Your Name]
"""

def analyze_resume(resume_file, job_desc):
    if not resume_file or not job_desc.strip():
        return [], [], [], {}, [], None, 0, []
    resume_text = extract_text(resume_file)
    job_text = job_desc.lower()
    your_skills = [skill for skill in SKILLS_DB if skill.lower() in resume_text]
    matching_skills = [skill for skill in your_skills if skill.lower() in job_text]
    missing_skills = [skill for skill in SKILLS_DB if skill.lower() in job_text and skill not in your_skills]
    learning_resources = {skill: RESOURCES.get(skill, "No resource found.") for skill in missing_skills}
    career_suggestions = sorted(set(role for skill in your_skills for role in suggest_roles(skill)))
    match_score = calculate_match_score(matching_skills, missing_skills)
    job_keywords = extract_keywords(job_text)
    pdf_path = generate_pdf(your_skills, matching_skills, missing_skills, learning_resources, career_suggestions, match_score)
    return (your_skills, matching_skills, missing_skills, learning_resources, 
            career_suggestions, pdf_path, match_score, job_keywords)

def format_skills(skills):
    if not skills:
        return "<p>No skills found.</p>"
    return "<ul>" + "".join(f"<li>{skill}</li>" for skill in skills) + "</ul>"

def format_resources(resources):
    if not resources:
        return "<p>No learning resources available.</p>"
    return "<ul>" + "".join(f'<li><strong>{skill}:</strong> <a href="{link}" target="_blank">{link}</a></li>' 
                           for skill, link in resources.items()) + "</ul>"

def format_careers(careers):
    if not careers:
        return "<p>No career suggestions.</p>"
    return "<ul>" + "".join(f"<li>{career}</li>" for career in careers) + "</ul>"

def format_keywords(keywords):
    if not keywords:
        return "<p>No keywords extracted.</p>"
    return "<div class='keywords'>" + " ".join(f"<span class='keyword'>{kw}</span>" for kw in keywords) + "</div>"
