import urllib3

from bs4 import BeautifulSoup

http = urllib3.PoolManager()
user = input("Enter github username: ")
link = "https://github.com/"+user+"?tab=repositories"
page=http.request('GET',link)
soup=BeautifulSoup(page.data,'html.parser')
head=soup.find('div',attrs={'id': 'user-repositories-list'})
# head=head.text.strip()
print(head.prettify())