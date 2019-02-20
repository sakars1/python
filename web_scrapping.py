import urllib3

from bs4 import BeautifulSoup

http = urllib3.PoolManager()
link='https://paailajob.com'
page=http.request('GET',link)
soup=BeautifulSoup(page.data)
head=soup.find('div',attrs={'class':"job-n-c"})
head=head.text.strip()
print(head)