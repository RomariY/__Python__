import requests
import bs4
import lxml

def title_grab():
    pass



two_star_titles = []
for num in range(1, 51):

    result_page = requests.get('https://books.toscrape.com/catalogue/category/books_1/page-' + str(num) + '.html')
    page_format = bs4.BeautifulSoup(result_page.text, "lxml")
    m = False
    books = page_format.select('.row > li > .product_pod')
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            title = book.select('a')[1]['title']
            two_star_titles.append(title)

for title in two_star_titles:
    print(title)