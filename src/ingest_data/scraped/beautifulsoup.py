import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for successful request

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

    return None

def get_website_data(url):
        
        soup = scrape_website(url)
        # Extract title, description, images, and links
        title = soup.title.string if soup.title else "N/A"
        description = soup.find('meta', attrs={'name': 'description'})
        description = description['content'] if description else "N/A"
        images = [img['src'] for img in soup.find_all('img') if img.get('src')]
        links = [a['href'] for a in soup.find_all('a') if a.get('href')]

        # Create a Pandas DataFrame
        data = {
            'URL': [url],
            'Title': [title],
            'Description': [description],
            'Images': [images],
            'Links': [links]
        }
        df = pd.DataFrame(data)

        return df



# # Example usage:
# url_to_scrape = 'https://example.com'
# result_df = get_website_data(url_to_scrape)

# # Display the resulting DataFrame
# print(result_df)