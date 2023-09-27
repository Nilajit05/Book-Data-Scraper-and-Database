import requests
from bs4 import BeautifulSoup
import sqlite3

# Create a SQLite database
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Create a table to store book data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        title TEXT,
        price TEXT,
        availability TEXT,
        rating TEXT
    )
''')

conn.commit()

# Base URL for book pages
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

# Loop through all 50 pages of books
for page_number in range(1, 51):
    url = base_url.format(page_number)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        for book in books:
            title = book.h3.a.attrs['title']
            price = book.select('div p.price_color')[0].get_text()
            availability = book.select('div p.availability')[0].get_text().strip()
            rating = book.p.attrs['class'][1]

            # Insert the data into the database
            cursor.execute("INSERT INTO books (title, price, availability, rating) VALUES (?, ?, ?, ?)",
                           (title, price, availability, rating))

        conn.commit()
    else:
        print(f"Failed to fetch data from page {page_number}")

conn.close()

print("Scraping and data insertion complete.")
