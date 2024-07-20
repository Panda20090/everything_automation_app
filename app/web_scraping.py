import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url, target_element, target_class):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        elements = soup.find_all(target_element, class_=target_class)
        data = [element.get_text() for element in elements]
        df = pd.DataFrame(data, columns=['ScrapedData'])
        file_path = 'data/scraped_data.csv'
        df.to_csv(file_path, index=False)
        return file_path
    else:
        return None
