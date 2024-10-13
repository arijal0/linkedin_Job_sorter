# resume_parsing.py
import PyPDF2
import docx

# Function to extract text from PDF resume
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)  # Use PdfReader instead of PdfFileReader
        text = ''
        for page in pdf_reader.pages:  # Iterate through pages using the new method
            text += page.extract_text()  # Use extract_text() method
    return text

# Function to extract text from Word resume
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return ' '.join([para.text for para in doc.paragraphs])

# Function to extract skills from the resume (based on keywords)
def extract_skills_from_resume(resume_text):
    skills_keywords = ['Python', 'Java', 'C++', 'C#', 'JavaScript', 'Ruby', 'HTML', 'CSS', 'SQL', 'NoSQL',
        'MongoDB', 'MySQL', 'PostgreSQL', 'AWS', 'GCP', 'Azure', 'Docker', 'Kubernetes', 
        'Machine Learning', 'Deep Learning', 'Data Science', 'Data Analysis', 'TensorFlow',
        'PyTorch', 'Django', 'Flask', 'React', 'Angular', 'Node.js', 'Spring Boot', 'Express.js',
        'Git', 'GitHub', 'Linux', 'Unix', 'Agile', 'Scrum', 'JIRA', 'Tableau', 'Power BI', 
        'Hadoop', 'Spark', 'Kafka', 'R', 'MATLAB', 'TypeScript', 'GraphQL', 'Rust', 'Go', 'Scala']
    extracted_skills = [skill for skill in skills_keywords if skill.lower() in resume_text.lower()]
    return extracted_skills
