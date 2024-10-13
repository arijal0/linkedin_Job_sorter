# scraping.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

# Selenium setup for LinkedIn login

def linkedin_login(driver, email, password):
    driver.get("https://www.linkedin.com/login")
    
    # Correctly find elements using By.ID
    email_field = driver.find_element(By.ID, 'username')  # Correct ID for email/phone field
    password_field = driver.find_element(By.ID, 'password')  # Correct ID for password field

    email_field.send_keys(email)
    password_field.send_keys(password)
    password_field.submit()

# Function to scrape LinkedIn jobs
def scrape_linkedin_jobs(driver, keyword, location):
    search_url = f"https://www.linkedin.com/jobs/search?keywords={keyword}&location={location}"
    driver.get(search_url)
    time.sleep(3)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    job_titles = []
    companies = []
    locations = []
    job_descriptions = []
    
    jobs = soup.find_all('li', class_='result-card job-result-card')
    
    for job in jobs:
        title = job.find('h3', class_='result-card__title').text if job.find('h3', class_='result-card__title') else 'N/A'
        company = job.find('h4', class_='result-card__subtitle').text if job.find('h4', class_='result-card__subtitle') else 'N/A'
        location = job.find('span', class_='job-result-card__location').text if job.find('span', class_='job-result-card__location') else 'N/A'
        job_desc = job.find('p', class_='job-result-card__snippet').text if job.find('p', class_='job-result-card__snippet') else 'N/A'
        
        job_titles.append(title)
        companies.append(company)
        locations.append(location)
        job_descriptions.append(job_desc)
    
    df = pd.DataFrame({
        'Job Title': job_titles,
        'Company': companies,
        'Location': locations,
        'Job Description': job_descriptions
    })
    return df

# Initialize WebDriver
def get_driver():
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

