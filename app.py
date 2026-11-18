import gradio as gr
from PyPDF2 import PdfReader
from docx import Document
from fpdf import FPDF
import requests
from collections import Counter
import re
import os
import sqlite3
from datetime import datetime

SKILLS_DB = [
    # Core Programming & AI Skills
    "Python", "Java", "C++", "JavaScript", "SQL", "R", "MATLAB",
    "Machine Learning", "Deep Learning", "Data Analysis", "Pandas", "NumPy",
    "TensorFlow", "PyTorch", "scikit-learn", "Statistics", "Data Visualization",
    # Cloud & DevOps
    "AWS", "Azure", "Google Cloud", "Docker", "Kubernetes", "API Development",
    # Web/App Development
    "HTML", "CSS", "Sass", "React", "Angular", "Vue", "Next.js", "Django", "Flask",
    "Firebase", "WordPress",
    # Collaboration & Workflow
    "Git", "GitHub", "JIRA", "Slack", "Trello", "Notion", "Asana",
    # Productivity & Office
    "Excel", "Google Sheets", "PowerPoint", "Microsoft Word",
    # Content Creation Tools
    "Canva", "Figma", "Photoshop", "Illustrator", "Premiere Pro", "Final Cut Pro",
    "DaVinci Resolve", "Audacity", "OBS Studio", "Screen Recording", "Video Editing",
    "Image Editing", "Audio Editing", "Animation", "Motion Graphics",
    # AI & Generative Media
    "Prompt Engineering", "Natural Language Processing", "ChatGPT", "Llama",
    "Generative AI", "LangChain", "Stable Diffusion", "Midjourney", "D-ID",
    "Speech-to-Text", "Text-to-Speech", "Face Animation", "Voice Cloning", "OpenCV",
    "Text Summarization", "Topic Modeling", "Automated Captioning",
    # Content, Marketing, Publishing
    "Content Automation", "Content Repurposing", "Newsletter Automation",
    "Blog Writing", "SEO", "Digital Marketing", "Branding", "Copywriting",
    "Social Media Management", "YouTube Studio", "Podcast Editing", "Online Courses",
    "Analytics", "Google Analytics", "Monetization", "Affiliate Marketing",
    "Email Marketing", "E-commerce Platforms",
    # Other creative skills
    "Storytelling", "Scriptwriting", "Photo Retouching", "Video Thumbnails",
    "Livestreaming", "Online Collaboration", "Campaign Optimization",
    # Java Full-Stack and Computer Science skills
    "Object-Oriented Programming", "OOP", "Data Structures", "Algorithms",
    "Java Collections", "Collections Framework", "Exception Handling",
    "Multithreading", "JDBC", "Spring Framework", "Spring Boot", "Spring MVC",
    "Spring Web", "Spring Data JPA", "Hibernate", "Maven", "Gradle", "REST APIs",
    "MySQL", "PostgreSQL", "Oracle Database", "MongoDB", "DBMS", "SQL Joins",
    "Subqueries", "Database Normalization", "Database Indexing", "JSON",
    "React.js", "HTML5", "CSS3", "JavaScript ES6", "Postman", "JUnit", "Mockito",
    "JDK", "JRE", "JVM", "Inheritance", "Polymorphism", "Encapsulation", "Abstraction",
    "Interfaces", "ArrayList", "HashMap", "String Handling", "Array Manipulation",
    "Recursion", "Searching", "Sorting", "Time Complexity", "Space Complexity",
    "LinkedList", "Stacks", "Queues", "Spring Security",
    "SQL Constraints", "Primary Keys", "Foreign Keys", "ACID Properties", "Transactions",
    "Stored Procedures", "Views", "Indexes", "Aggregate Functions", "GROUP BY", "ORDER BY",
    "DDL", "DML", "TCL", "ER Diagrams", "Database Normalisation"\r
]



RESOURCES = {
    # Core Programming & AI
    "Python": "https://www.learnpython.org/",
    "Java": "https://www.learnjavaonline.org/",
    "C++": "https://www.learncpp.com/",
    "JavaScript": "https://javascript.info/",
    "SQL": "https://www.w3schools.com/sql/",
    "R": "https://cran.r-project.org/manuals.html",
    "MATLAB": "https://matlabacademy.mathworks.com/",
    "Machine Learning": "https://www.coursera.org/learn/machine-learning",
    "Deep Learning": "https://www.deeplearning.ai/short-courses/",
    "Data Analysis": "https://www.datacamp.com/courses/data-analysis-in-python",
    "Statistics": "https://www.khanacademy.org/math/statistics-probability",
    "Data Visualization": "https://www.tableau.com/learn/training",
    "Pandas": "https://pandas.pydata.org/docs/getting_started/index.html",
    "NumPy": "https://numpy.org/devdocs/user/quickstart.html",
    "TensorFlow": "https://www.tensorflow.org/tutorials",
    "PyTorch": "https://pytorch.org/tutorials/",
    "scikit-learn": "https://scikit-learn.org/stable/tutorial/index.html",
    # Java Full-Stack and Computer Science resources
    "Object-Oriented Programming": "https://dev.java/learn/classes-objects/",
    "OOP": "https://dev.java/learn/classes-objects/",
    "Data Structures": "https://www.geeksforgeeks.org/data-structures/",
    "Algorithms": "https://www.geeksforgeeks.org/fundamentals-of-algorithms/",
    "Java Collections": "https://dev.java/learn/api/collections-framework/",
    "Collections Framework": "https://dev.java/learn/api/collections-framework/",
    "Exception Handling": "https://docs.oracle.com/javase/tutorial/essential/exceptions/",
    "Multithreading": "https://dev.java/learn/concurrency/",
    "JDBC": "https://docs.oracle.com/javase/tutorial/jdbc/",
    "Spring Framework": "https://docs.spring.io/spring-framework/reference/",
    "Spring Boot": "https://spring.io/guides",
    "Spring MVC": "https://docs.spring.io/spring-framework/reference/web/webmvc.html",
    "Spring Web": "https://docs.spring.io/spring-framework/reference/web.html",
    "Spring Data JPA": "https://docs.spring.io/spring-data/jpa/reference/",
    "Hibernate": "https://hibernate.org/orm/documentation/",
    "Maven": "https://maven.apache.org/guides/getting-started/",
    "Gradle": "https://docs.gradle.org/current/userguide/userguide.html",
    "REST APIs": "https://restfulapi.net/",
    "MySQL": "https://dev.mysql.com/doc/",
    "PostgreSQL": "https://www.postgresql.org/docs/",
    "Oracle Database": "https://docs.oracle.com/en/database/",
    "MongoDB": "https://www.mongodb.com/docs/",
    "DBMS": "https://www.geeksforgeeks.org/dbms/",
    "SQL Joins": "https://www.w3schools.com/sql/sql_join.asp",
    "Subqueries": "https://www.w3schools.com/sql/sql_subqueries.asp",
    "Database Normalization": "https://www.geeksforgeeks.org/database-normalization-normal-forms/",
    "Database Indexing": "https://dev.mysql.com/doc/refman/8.4/en/mysql-indexes.html",
    "JDK": "https://dev.java/learn/",
    "JRE": "https://dev.java/learn/",
    "JVM": "https://dev.java/learn/",
    "Inheritance": "https://dev.java/learn/classes-objects/",
    "Polymorphism": "https://dev.java/learn/classes-objects/",
    "Encapsulation": "https://dev.java/learn/classes-objects/",
    "Abstraction": "https://dev.java/learn/classes-objects/",
    "Interfaces": "https://dev.java/learn/",
    "ArrayList": "https://dev.java/learn/api/collections-framework/",
    "HashMap": "https://dev.java/learn/api/collections-framework/",
    "String Handling": "https://dev.java/learn/",
    "Array Manipulation": "https://www.geeksforgeeks.org/array-data-structure/",
    "Recursion": "https://www.geeksforgeeks.org/recursion/",
    "Searching": "https://www.geeksforgeeks.org/searching-algorithms/",
    "Sorting": "https://www.geeksforgeeks.org/sorting-algorithms/",
    "Time Complexity": "https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/",
    "Space Complexity": "https://www.geeksforgeeks.org/g-fact-86/",
    "LinkedList": "https://dev.java/learn/api/collections-framework/",
    "Stacks": "https://www.geeksforgeeks.org/stack-data-structure/",
    "Queues": "https://www.geeksforgeeks.org/queue-data-structure/",
    "Spring Security": "https://docs.spring.io/spring-security/reference/",
    "SQL Constraints": "https://dev.mysql.com/doc/refman/8.4/en/constraint.html",
    "Primary Keys": "https://dev.mysql.com/doc/refman/8.4/en/constraint-primary-key.html",
    "Foreign Keys": "https://dev.mysql.com/doc/refman/8.4/en/create-table-foreign-keys.html",
    "ACID Properties": "https://dev.mysql.com/doc/refman/8.4/en/mysql-acid.html",
    "Transactions": "https://dev.mysql.com/doc/refman/8.4/en/commit.html",
    "Stored Procedures": "https://dev.mysql.com/doc/refman/8.4/en/create-procedure.html",
    "Views": "https://dev.mysql.com/doc/refman/8.4/en/views.html",
    "Indexes": "https://dev.mysql.com/doc/refman/8.4/en/mysql-indexes.html",
    "Aggregate Functions": "https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html",
    "GROUP BY": "https://dev.mysql.com/doc/refman/8.4/en/group-by-handling.html",
    "ORDER BY": "https://dev.mysql.com/doc/refman/8.4/en/order-by-optimization.html",
    "DDL": "https://dev.mysql.com/doc/refman/8.4/en/sql-data-definition-statements.html",
    "DML": "https://dev.mysql.com/doc/refman/8.4/en/sql-data-manipulation-statements.html",
    "TCL": "https://dev.mysql.com/doc/refman/8.4/en/sql-transactional-statements.html",
    "ER Diagrams": "https://www.geeksforgeeks.org/dbms/introduction-of-er-model/",
    "Database Normalisation": "https://www.geeksforgeeks.org/dbms/database-normalization/",
    "JSON": "https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON",
    "React.js": "https://react.dev/learn",
    "HTML5": "https://developer.mozilla.org/en-US/docs/Web/HTML",
    "CSS3": "https://developer.mozilla.org/en-US/docs/Web/CSS",
    "JavaScript ES6": "https://javascript.info/",
    "Postman": "https://learning.postman.com/docs/getting-started/",
    "JUnit": "https://junit.org/junit5/docs/current/user-guide/",
    "Mockito": "https://site.mockito.org/",
    # Cloud & DevOps
    "AWS": "https://aws.amazon.com/training/",
    "Azure": "https://learn.microsoft.com/en-us/training/azure/",
    "Google Cloud": "https://cloud.google.com/training",
    "Docker": "https://docs.docker.com/get-started/",
    "Kubernetes": "https://kubernetes.io/docs/tutorials/",
    "API Development": "https://www.postman.com/resources/courses/",
    # Web/App
    "HTML": "https://developer.mozilla.org/en-US/docs/Web/HTML",
    "CSS": "https://developer.mozilla.org/en-US/docs/Web/CSS",
    "Sass": "https://sass-lang.com/guide",
    "React": "https://reactjs.org/tutorial/tutorial.html",
    "Angular": "https://angular.io/start",
    "Vue": "https://vuejs.org/guide/quick-start.html",
    "Next.js": "https://nextjs.org/learn/basics/create-nextjs-app",
    "Django": "https://docs.djangoproject.com/en/stable/intro/tutorial01/",
    "Flask": "https://flask.palletsprojects.com/en/2.0.x/tutorial/",
    "Firebase": "https://firebase.google.com/docs",
    "WordPress": "https://learn.wordpress.org/",
    # Collaboration
    "Git": "https://git-scm.com/doc",
    "GitHub": "https://docs.github.com/en/get-started",
    "JIRA": "https://www.atlassian.com/software/jira/guides",
    "Slack": "https://slack.com/resources",
    "Trello": "https://trello.com/guide",
    "Notion": "https://www.notion.so/help/guides/notion-basics",
    "Asana": "https://academy.asana.com/",
    # Productivity & Office
    "Excel": "https://support.microsoft.com/en-us/excel",
    "Google Sheets": "https://support.google.com/docs/answer/14078417",
    "PowerPoint": "https://support.microsoft.com/en-us/powerpoint",
    "Microsoft Word": "https://support.microsoft.com/en-us/word",
    # Content Creation Tools
    "Canva": "https://www.canva.com/learn/getting-started-with-canva/",
    "Figma": "https://www.figma.com/resources/learn-design/",
    "Photoshop": "https://helpx.adobe.com/photoshop/tutorials.html",
    "Illustrator": "https://helpx.adobe.com/illustrator/tutorials.html",
    "Premiere Pro": "https://helpx.adobe.com/premiere-pro/tutorials.html",
    "Final Cut Pro": "https://support.apple.com/final-cut-pro",
    "DaVinci Resolve": "https://www.blackmagicdesign.com/products/davinciresolve/training",
    "OBS Studio": "https://obsproject.com/wiki/",
    "Audacity": "https://www.audacityteam.org/help/documentation/",
    # AI & Generative
    "Prompt Engineering": "https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/",
    "Natural Language Processing": "https://www.coursera.org/specializations/natural-language-processing",
    "ChatGPT": "https://platform.openai.com/docs/guides/gpt",
    "Llama": "https://llama.meta.com/get-started/",
    "Generative AI": "https://developers.google.com/machine-learning/genai",
    "LangChain": "https://langchain.com/docs/",
    "Stable Diffusion": "https://docs.stablediffusionweb.com/",
    "Midjourney": "https://docs.midjourney.com/",
    "D-ID": "https://docs.d-id.com/docs",
    "Speech-to-Text": "https://cloud.google.com/speech-to-text/docs",
    "Text-to-Speech": "https://cloud.google.com/text-to-speech/docs",
    "Face Animation": "https://d-id.com/resources/",
    "Voice Cloning": "https://www.descript.com/overdub",
    "OpenCV": "https://opencv.org/courses/",
    "Text Summarization": "https://huggingface.co/tasks/summarization",
    "Topic Modeling": "https://towardsdatascience.com/topic-modeling-with-python-5eedb6e2a55",
    "Automated Captioning": "https://www.rev.com/blog/automated-captioning",
    # Content, Marketing, Publishing
    "Content Automation": "https://zapier.com/blog/automate-content-creation/",
    "Content Repurposing": "https://www.contenthacker.com/content-repurposing/",
    "Newsletter Automation": "https://www.mailerlite.com/blog/newsletter-automation-guide",
    "Blog Writing": "https://www.wix.com/blog/post/how-to-write-a-blog-post",
    "SEO": "https://moz.com/beginners-guide-to-seo",
    "Digital Marketing": "https://www.coursera.org/specializations/digital-marketing",
    "Branding": "https://www.coursera.org/learn/branding-the-creative/",
    "Copywriting": "https://www.copyblogger.com/copywriting-101/",
    "Social Media Management": "https://www.hubspot.com/social-media-management",
    "YouTube Studio": "https://support.google.com/youtube/answer/9314474",
    "Podcast Editing": "https://www.buzzsprout.com/blog/podcast-editing-software-tools",
    "Online Courses": "https://www.udemy.com/courses/teacher/",
    "Analytics": "https://support.google.com/analytics/answer/1008015",
    "Google Analytics": "https://analytics.google.com/analytics/academy/",
    "Monetization": "https://www.youtube.com/creators/monetize",
    "Affiliate Marketing": "https://www.hubspot.com/affiliate-marketing",
    "Email Marketing": "https://mailchimp.com/email-marketing/",
    "E-commerce Platforms": "https://www.shopify.com/learn",
    # Creative
    "Storytelling": "https://openai.com/research/storytelling",
    "Scriptwriting": "https://www.scriptreaderpro.com/complete-guide-to-scriptwriting/",
    "Photo Retouching": "https://www.adobe.com/creativecloud/photography/discover/photo-retouching.html",
    "Video Thumbnails": "https://www.youtube.com/official/blog/en-GB/products/yt-creator/video-thumbnails/",
    "Livestreaming": "https://creators.youtube.com/learn/live-streaming/",
    "Online Collaboration": "https://www.notion.so/help/guides/collaborate",
    "Campaign Optimization": "https://support.google.com/google-ads/answer/6167122"
}



def extract_text(file):
    text = ""
    if not file:
        return ""
    filepath = file if isinstance(file, str) else file.name
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
    """Optional BART summarisation; requires HF_API_KEY in the host environment."""
    if not job_desc or not job_desc.strip():
        return ""
    api_key = os.environ.get("HF_API_KEY")
    if not api_key:
        return "Summarisation is not configured. Add an HF_API_KEY environment variable to enable it."
    api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.post(api_url, headers=headers, json={"inputs": job_desc}, timeout=45)
        response.raise_for_status()
        payload = response.json()
        if isinstance(payload, list) and payload and "summary_text" in payload[0]:
            return payload[0]["summary_text"]
        return "The summarisation service did not return a summary. Please try again later."
    except requests.RequestException as exc:
        return f"Summarisation is temporarily unavailable: {exc.__class__.__name__}."
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

def contains_skill(text, skill):
    """Match a skill as a phrase/term, avoiding common substring false positives."""
    pattern = r"(?<![a-z0-9])" + re.escape(skill.lower()) + r"(?![a-z0-9])"
    return re.search(pattern, text.lower()) is not None




def init_db():
    """Create a small SQLite database for recent resume analyses."""
    with sqlite3.connect("careeralign.db") as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS analysis_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            match_score INTEGER NOT NULL,
            matched_skills TEXT,
            missing_skills TEXT,
            job_keywords TEXT
        )""")


def save_analysis(match_score, matching_skills, missing_skills, job_keywords):
    with sqlite3.connect("careeralign.db") as conn:
        conn.execute(
            "INSERT INTO analysis_history (created_at, match_score, matched_skills, missing_skills, job_keywords) VALUES (?, ?, ?, ?, ?)",
            (datetime.now().strftime("%Y-%m-%d %H:%M"), match_score,
             ", ".join(matching_skills), ", ".join(missing_skills), ", ".join(job_keywords))
        )


def load_history():
    init_db()
    with sqlite3.connect("careeralign.db") as conn:
        rows = conn.execute(
            "SELECT created_at, match_score, matched_skills, missing_skills FROM analysis_history ORDER BY id DESC LIMIT 20"
        ).fetchall()
    return rows or [("No analyses yet", "", "Upload a resume and analyse a job description", "")]

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

# Gradio web interface
CUSTOM_CSS = """
.gradio-container {max-width: 1120px !important; margin: auto !important;}
#hero {padding: 28px; border-radius: 18px; background: linear-gradient(120deg,#172554,#4338ca); color: white; margin-bottom: 18px;}
#hero h1 {font-size: 2.1rem; margin-bottom: 6px; color: white;}
#hero p {color: #e0e7ff; margin: 0;}
.panel {border: 1px solid var(--border-color-primary); border-radius: 14px; padding: 14px;}
footer {display:none !important;}
"""

init_db()
with gr.Blocks(title="CareerAlign AI | Resume Analyzer", theme=gr.themes.Soft(primary_hue="indigo", neutral_hue="slate"), css=CUSTOM_CSS) as demo:
    gr.HTML("""<div id='hero'><h1>CareerAlign AI</h1><p>A simple resume and job description analyzer · Find skill gaps and plan your next step</p></div>""")
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 01 · Add your details")
            resume_input = gr.File(label="Upload your resume", file_types=[".pdf", ".docx"], type="filepath")
            job_input = gr.Textbox(label="Job description", placeholder="Paste the job description here...", lines=12)
            analyze_button = gr.Button("Analyse my resume", variant="primary", size="lg")
            gr.Markdown("*Supports PDF and DOCX files. Your score is an indicative keyword match, not a hiring prediction.*")
        with gr.Column(scale=1):
            gr.Markdown("### 02 · Your analysis")
            score_output = gr.Number(label="Keyword match score (%)", precision=0)
            with gr.Row():
                detected_output = gr.JSON(label="Skills in your resume")
                matched_output = gr.JSON(label="Matching skills")
            with gr.Row():
                missing_output = gr.JSON(label="Skills to improve")
                careers_output = gr.JSON(label="Suggested career paths")
            resources_output = gr.JSON(label="Learning resources")
            keywords_output = gr.JSON(label="Job description keywords")
            report_output = gr.File(label="Download your PDF report")
    analyze_button.click(fn=analyze_resume, inputs=[resume_input, job_input], outputs=[detected_output, matched_output, missing_output, resources_output, careers_output, report_output, score_output, keywords_output])
    gr.Markdown("---")
    with gr.Accordion("Recent analysis history", open=False):
        history_output = gr.Dataframe(headers=["Date", "Match %", "Matched skills", "Missing skills"], value=load_history, interactive=False, wrap=True)
        refresh_button = gr.Button("Refresh history")
        refresh_button.click(fn=load_history, outputs=history_output)
    with gr.Accordion("Optional: summarise a job description", open=False):
        gr.Markdown("Requires an HF_API_KEY secret. Resume analysis works without an API key.")
        summary_input = gr.Textbox(label="Job description", lines=5)
        summary_button = gr.Button("Summarise")
        summary_output = gr.Textbox(label="Summary", lines=5)
        summary_button.click(fn=summarize_job_description, inputs=summary_input, outputs=summary_output)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", "7860")), share=False, show_error=True)
