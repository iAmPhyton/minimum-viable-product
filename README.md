This toolbox consists of two projects - one for fetching job descriptions using various job websites' APIs and another for analyzing job descriptions using spaCy for key skills and qualifications.

UsingApiKeys.py: Job Descriptions Fetcher

This script fetches job descriptions from various job websites using their respective APIs.

Getting Started

Prerequisites

- Python 3. x
- Install required packages:
  pip install requests bs4
  
Usage:
Input the URLs of job websites with APIs included in the script:
 
linkedin_job_url = 'input URL of job websites with APIs included'
wellfound_job_url = 'input URL of job websites with APIs included'
theladders_job_url = 'input URL of job websites with APIs included'
Replace the example API keys with your actual API keys:

linkedin_api_key = 'your_linkedin_api_key'
theladders_api_key = 'your_theladders_api_key'
wellfound_api_key = 'your_wellfound_api_key'
Run the script:
python job_descriptions_fetcher.py
Example Output:
LinkedIn Job Description:
[LinkedIn job description here]

WellFound Job Description:
[WellFound job description here]

TheLadders Job Description:
[TheLadders job description here]
Notes:
Make sure to handle your API keys securely.
Replace the example URLs with the specific job websites' API endpoints.
completeCode.py: Job Descriptions Analyzer
This script extracts job descriptions from various job websites and analyzes them using spaCy for key skills and qualifications.

Getting Started
Prerequisites
Python 3. x

Install required packages:
pip install requests bs4 pandas spacy
Download the spaCy English model:
python -m spacy download en_core_web_sm

Usage:
Modify the job_description_urls list with the URLs of the job descriptions you want to analyze:

Python
job_description_urls = [
    'https://www.linkedin.com/jobs/',
    'https://www.wellfound.com/jobs',
    'https://www.theladders.com/recommended'
]
Running the script:
python job_descriptions_analyzer.py
Example Output
{'Job Description': '[Job description text here]', 'Key Skills': ['skill1', 'skill2'], 'Qualifications': ['qualification1', 'qualification2']}
{'Job Description': '[Job description text here]', 'Key Skills': ['skill3', 'skill4'], 'Qualifications': ['qualification3', 'qualification4']}
...
Contributions are welcome! Please follow the contribution guidelines.

License
This project is licensed under the MIT License.
