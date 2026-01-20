import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/"

def get_books():
    try:
        response = requests.get(URL)
        response.raise_for_status()  # перевірка помилок HTTP

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            availability = book.find("p", class_="instock availability").text.strip()

            print("Назва:", title)
            print("Ціна:", price)
            print("Наявність:", availability)
            print("-" * 40)

    except requests.exceptions.RequestException as e:
        print("Помилка при з'єднанні з сайтом:", e)


get_books()
