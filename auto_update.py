from bs4 import BeautifulSoup
import http.client

conn = http.client.HTTPSConnection("cgyy.xmu.edu.cn")
payload = ''
headers = {}
conn.request("GET", "/room/1", payload, headers)
res = conn.getresponse()
data = res.read()

new_soup = BeautifulSoup(data)
if new_soup.find('ul', class_='slot-list') is None:
    print("302")
else:
    old_soup = BeautifulSoup(open("gymbooker.html"))

    old_soup.find('ul', class_='slot-list').clear()

    for i in new_soup.find('ul', class_='slot-list'):
        old_soup.find('ul', class_='slot-list').append(i)

    old_soup.find('ul', class_='slot-list').append(new_soup.find('div', class_="help-info"))


    with open('gymbooker.html', 'w', encoding='utf-8') as f:
        f.write(str(old_soup))  # write result
    print("successed")