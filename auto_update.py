from bs4 import BeautifulSoup
import requests

url = "https://cgyy.xmu.edu.cn/room/1"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

new_soup = BeautifulSoup(response.text)
if new_soup.find('ul', class_='slot-list') is None:
    print("302")
else:
    old_soup = BeautifulSoup(open("./gymbooker.html"))

    old_soup.find('ul', class_='slot-list').clear()

    for i in new_soup.find('ul', class_='slot-list'):
        old_soup.find('ul', class_='slot-list').append(i)

    old_soup.find('ul', class_='slot-list').append(new_soup.find('div', class_="help-info"))


    with open('gymbooker.html', 'w', encoding='utf-8') as f:
        f.write(str(old_soup))  # write result
    print("successed")