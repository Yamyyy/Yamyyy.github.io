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


    empty_div = new_soup.new_tag('div')
    empty_div.attrs['class'] = 'clearfix'
    empty_div.append(' ')
    empty_div2= new_soup.new_tag('div')
    empty_div2.append("123")
    empty_div.append(empty_div2)
    for i in new_soup.find('ul', class_='slot-list'):
        old_soup.find('ul', class_='slot-list').append(i)
        
        
        # old_soup.find('ul', class_='slot-list').append(new_soup.find('div', class_="clearfix"))
        old_soup.find('ul', class_='slot-list').append(empty_div)
        print(empty_div)

    old_soup.find('ul', class_='slot-list').append(new_soup.find('div', class_="help-info"))


    with open('gymbooker.html', 'w', encoding='utf-8') as f:
        f.write(str(old_soup))  # write result
    print("successed")