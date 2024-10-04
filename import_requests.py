import requests
from bs4 import BeautifulSoup
import re

# Function to get all PDF links from a website
def get_pdf_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links = []

    # Find all anchor tags with href attribute
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Check if the link ends with .pdf
        if re.search(r'\.pdf$', href):
            pdf_links.append(href)

    return pdf_links

# Example usage
url = 'https://london.ca/government/property-taxes-finance/municipal-budget/2024-2027-business-plans'
pdf_links = get_pdf_links(url)
for link in pdf_links:
    print(link)
