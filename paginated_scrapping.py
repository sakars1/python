import requests
from bs4 import BeautifulSoup

page_url = 'https://www.whitehouse.gov/briefings-statements/'
access = requests.get(page_url)

article_num = 1

while True:

    source = access.content

    soup = BeautifulSoup(source, 'html.parser')

    urls = []
    for h2_tag in soup.find_all('h2'):
        a_tag = h2_tag.find('a')
        urls.append(a_tag.attrs['href'])

    next_page = soup.find('a', {'class': 'pagination__next'})
    if next_page:
        page_url = next_page.get('href')

        # Print the URLS

        for n_url in urls:
            print(article_num, n_url, '\n')
            article_num += 1
    else:
        break  # exit `while True`

