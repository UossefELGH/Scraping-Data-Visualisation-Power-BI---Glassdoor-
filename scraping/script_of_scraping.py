from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import random
import logging

# Configure logging for error tracking
logging.basicConfig(filename='scraping_errors.log', level=logging.ERROR)

# Replace with the correct path to your ChromeDriver
service = Service(r"C:\Users\DELL\Desktop\chromedriver-win64\chromedriver.exe")

# Configure Chrome options
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--headless")  # Uncomment to run headless

# Define base URL and parameters for job search
base_url = "https://www.glassdoor.com/Job/france-{}-jobs-SRCH_IL.0,6_IN86_KO7,32.htm"
job_types = {
    "ingénieur-en-informatique": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-en-intelligence-artificielle": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-devops": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-cybersécurité": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "data-engineer": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "cloud-computing-engineer": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "data-scientist": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-énérgies-renouvelables": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-électrotechnique": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-génie-civil": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-robotique": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-mécanique": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-industriel": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-automobile": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-télécommunications": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-électronique": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-financier": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-électronique": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-financier": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-aéronautique": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-data-scientist": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-logiciel": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-full-stack": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-réseaux-sécurité": {"CDI": "5QWDV", "CDD": "T9BXE"},
    "ingénieur-civil": {"CDI": "5QWDV", "CDD": "T9BXE"}
}
from_age = 30

# Generate the list of URLs
def generate_urls(base_url, job_types, from_age):
    urls = []
    for job_title, types in job_types.items():
        for contract_type, job_code in types.items():
            url = f"{base_url.format(job_title)}?jobTypeIndeed={job_code}&fromAge={from_age}"
            urls.append(url)
    return urls

urls = generate_urls(base_url, job_types, from_age)

# File name to store the data
file_name = 'glassdoor_jobs_dataset.csv'

# Function to initialize and return the browser driver
def init_browser():
    return webdriver.Chrome(service=service, options=options)

# Function to detect contract type from URL
def detect_contract_type(url):
    if "5QWDV" in url:
        return "CDI"
    elif "T9BXE" in url:
        return "CDD"
    else:
        return "Non spécifié"  # Default if contract type not found


# Function to scrape a single URL, auto-detecting contract type
def scrape_data_from_url(driver, url):
    driver.get(url)
    time.sleep(random.uniform(5, 10))  # Pause to simulate human-like delay
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Automatically detect the contract type from the URL
    contract_type = detect_contract_type(url)
    
def scrape_data_from_url(driver, url):
    driver.get(url)
    time.sleep(random.uniform(5, 10))  # Pause pour éviter d'être détecté
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Détecter automatiquement le type de contrat
    contract_type = detect_contract_type(url)
    
    job_listings = []
    for job_card in soup.find_all('div', class_='JobCard_jobCardContainer__arQlW'):
        title = job_card.find('a', class_='JobCard_jobTitle__GLyJ1').get_text(strip=True) if job_card.find('a', class_='JobCard_jobTitle__GLyJ1') else "Non spécifié"
        company = job_card.find('span', class_='EmployerProfile_profileContainer__63w3R.EmployerProfile_compact__28h9t').get_text(strip=True) if job_card.find('span', class_='EmployerProfile_profileContainer__63w3R.EmployerProfile_compact__28h9t') else "Non spécifié"
        location = job_card.find('div', class_='JobCard_location__Ds1fM').get_text(strip=True) if job_card.find('div', class_='JobCard_location__Ds1fM') else "Non spécifié"
        salary = job_card.find('div', class_='JobCard_salaryEstimate__QpbTW').get_text(strip=True) if job_card.find('div', class_='JobCard_salaryEstimate__QpbTW') else "Non spécifié"
        
        # Ajouter la classification
        department = classify_job(title)

        job_listings.append({
            'Titre': title,
            'Entreprise': company,
            'Localisation': location,
            'Salaire': salary,
            'Contrat': contract_type,
            'Département': department,  # Nouveau champ
        })
    
    return job_listings


# Main scraping function to iterate through URLs with browser reopen after each URL
def main_scrape(urls):
    all_job_listings = []
    
    for url in urls:
        try:
            # Initialize the browser for each URL
            driver = init_browser()
            print(f"Scraping URL: {url}")

            # Scrape data from the current URL
            job_data = scrape_data_from_url(driver, url)
            all_job_listings.extend(job_data)  # Add data from current URL
            print(f"Data scraped for this URL")
            
            # Close the browser after scraping each page
            driver.quit()
            
            # Pause between requests to avoid detection
            time.sleep(random.uniform(5, 15))
        
        except Exception as e:
            # Log the error and ensure the browser is closed
            logging.error(f"Failed to scrape {url}: {e}")
            driver.quit()  # Close the browser in case of an error
            time.sleep(random.uniform(5, 10))  # Pause after an error to avoid issues
    
    return all_job_listings

# Save data to CSV
def save_to_csv(data, file_name):
    df = pd.DataFrame(data)
    if os.path.exists(file_name):
        df.to_csv(file_name, mode='a', header=False, index=False, encoding='utf-8')
        print(f"Data appended to {file_name}")
    else:
        df.to_csv(file_name, index=False, encoding='utf-8')
        print(f"All Data saved to new file {file_name}")

# Run the main scraping and save data
if __name__ == "__main__":
    all_job_listings = main_scrape(urls)
    save_to_csv(all_job_listings, file_name)
