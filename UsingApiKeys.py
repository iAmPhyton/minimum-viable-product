import requests
import json
from bs4 import BeautifulSoup

def fetch_linkedin_job_descriptions(api_key, job_url):
    # Assuming you have a valid LinkedIn API key
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(job_url, headers=headers)

    if response.status_code == 200:
        job_data = response.json()
        return job_data.get('description', '')
    else:
        print(f"Error fetching job description from LinkedIn: {response.status_code}")
        return None

def fetch_wellfound_job_descriptions(job_url):
    # Assuming WellFound provides a public API
    response = requests.get(job_url)

    if response.status_code == 200:
        job_data = response.json()
        return job_data.get('description', '')
    else:
        print(f"Error fetching job description from WellFound: {response.status_code}")
        return None

def fetch_theladders_job_descriptions(job_url):
    # Assuming TheLadders provides a public API
    response = requests.get(job_url)

    if response.status_code == 200:
        job_data = response.json()
        return job_data.get('description', '')
    else:
        print(f"Error fetching job description from TheLadders: {response.status_code}")
        return None

# Example URLs for job descriptions
linkedin_job_url = 'input URL of job websites with APIs included'
wellfound_job_url = 'input URL of job websites with APIs included'
theladders_job_url = 'input URL of job websites with APIs included'

# Example API key for job websites (replace with your actual various API keys)
linkedin_api_key = 'your_linkedin_api_key'
theladders_api_key = 'your_theladders_api_key'
wellfound_api_key = 'your_wellfound_api_key'

# Fetch job descriptions using APIs
linkedin_job_description = fetch_linkedin_job_descriptions(linkedin_api_key, linkedin_job_url)
wellfound_job_description = fetch_wellfound_job_descriptions(wellfound_api_key,wellfound_job_url)
theladders_job_description = fetch_theladders_job_descriptions(theladders_api_key,theladders_job_url)

# Output the fetched job descriptions
print("LinkedIn Job Description:")
print(linkedin_job_description)

print("\nWellFound Job Description:")
print(wellfound_job_description)

print("\nTheLadders Job Description:")
print(theladders_job_description) 