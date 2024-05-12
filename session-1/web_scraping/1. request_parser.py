import requests
from bs4 import BeautifulSoup
url = "https://www.prothomalo.com/bangladesh/district/l9iivxgmt0"

response = requests.get(url)
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

print(soup.find('h1').text)
all_paragraphs = soup.find_all('p')

for paragraph in all_paragraphs:
    print(paragraph.text)


