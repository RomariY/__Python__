import requests
import lxml
import bs4

page = 1
page_still_valid = True
authors = set()
quotes = set()

while page_still_valid:
    print(page)
    result_page = requests.get('https://quotes.toscrape.com/page/' + str(page) + '/')
    soup = bs4.BeautifulSoup(result_page.text, 'lxml')
    validation = soup.select('.row .col-md-8')
    for txt in validation:
        if 'No quotes found!' in txt.text:
            page_still_valid = False
            break

    for name in soup.select('.author'):
        authors.add(name.text)


    
    for quot in soup.select('.text'):
        quotes.add(quot.text)

    page += 1
    

for a in authors:
    print(a)


# for tag in soup.select('.tags-bx .tag-item'):
#     print(tag.text)

