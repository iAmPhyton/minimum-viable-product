import requests
from bs4 import BeautifulSoup
import pandas as pd
import spacy

# Sample job description URLs from job websites
job_description_urls = [
    'https://www.linkedin.com/jobs/',
    'https://www.wellfound.com/jobs',
    'https://www.theladders.com/recommended'
] 

def fetch_job_descriptions(job_urls):
    job_descriptions = []

    for url in job_urls:
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract job description from the HTML (adjust based on actual HTML structure)
        job_description_element = soup.find('div', class_='job-description')
        if job_description_element:
            job_description = job_description_element.get_text(strip=True)
            job_descriptions.append(job_description)

    return job_descriptions

def analyze_job_descriptions(job_descriptions):
    nlp = spacy.load("en_core_web_sm")

    analyzed_jobs = []

    for job_description in job_descriptions:
        doc = nlp(job_description)

        # Extract entities (e.g., skills, qualifications) using spaCy
        key_skills = [ent.text for ent in doc.ents if ent.label_ == "KEY_SKILL"]
        qualifications = [ent.text for ent in doc.ents if ent.label_ == "QUALIFICATION"]

        # Store analyzed job details in a dictionary
        analyzed_job = {
            'Job Description': job_description,
            'Key Skills': key_skills,
            'Qualifications': qualifications
        }
        analyzed_jobs.append(analyzed_job)

    return analyzed_jobs

# Sample function to update spaCy's named entity recognition (NER) for custom labels
def update_spacy_ner(nlp):
    ner = nlp.get_pipe("ner")
    ner.add_label("KEY_SKILL")
    ner.add_label("QUALIFICATION")

# Sample code to update spaCy NER labels
update_spacy_ner(spacy.load("en_core_web_sm"))

# Fetch job descriptions from the provided dummy job websites
job_descriptions = fetch_job_descriptions(job_description_urls)

# Analyze job descriptions using spaCy
analyzed_jobs = analyze_job_descriptions(job_descriptions)

# Output the analyzed job details
for job in analyzed_jobs:
    print(job) 