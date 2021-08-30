import requests
import lxml
import bs4

result = requests.get('https://en.wikipedia.org/wiki/Tim_Cook')
print(type(result))

soup = bs4.BeautifulSoup(result.text, "lxml")


# print(soup.select('.infobox-image .image img'))
img_src = soup.select('.infobox-image .image img')[0]['src']
img_link = requests.get('https:' + img_src)
print(img_link)

f = open('/home/roman/Temp/temp.jpg', 'wb')
f.write(img_link.content)
f.close()