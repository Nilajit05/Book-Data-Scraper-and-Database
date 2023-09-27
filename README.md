# Book-Data-Scraper-and-Database

Project Name: Book-Data-Scraper-and-Database
# Description: 
This Python script performs web scraping to fetch book data from http://books.toscrape.com and stores it in a SQLite database. It uses the requests library for web requests, BeautifulSoup for parsing HTML, and sqlite3 for database operations.

# Features:
Scrapes book data from multiple pages.
Creates a SQLite database to store book information.
Handles potential errors during web scraping.
# How to Use:
Install the required dependencies:
pip install requests beautifulsoup4 sqlite3
# Clone this repository:
git clone <repository-url>
# Navigate to the project folder:
cd Book-Data-Scraper
# Run the Python script:
python book_scraper.py
# Database Structure:
books table: Stores book data with columns title, price, availability, and rating.
