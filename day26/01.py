import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
import time

BASE_URL = "https://books.toscrape.com/"
START_PAGE = "catalogue/page-1.html"
OUTPUT_PAGE = "books_data.json"
TARGET_COUNT = 70


def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Failed to fetch URL: {url}\nError: {e}")
        return [], None

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    # Loop through all book entries on the page
    for article in soup.select("article.product_pod"):
        title_tag = article.select_one("h3 > a")
        if not title_tag:
            continue

        title = title_tag.get("title")
        price_tag = article.select_one("p.price_color")
        price = price_tag.text.strip() if price_tag else "N/A"

        books.append({
            "title": title,
            "price": price
        })

    # Find link to next page (if any)
    next_link = soup.select_one("li.next > a")
    next_url = urljoin(url, next_link["href"]) if next_link else None

    return books, next_url


def main():
    collected = []
    current_url = urljoin(BASE_URL, START_PAGE)

    while len(collected) < TARGET_COUNT and current_url:
        print(f"\n📘 Scraping: {current_url}")
        books, next_url = scrape_page(current_url)
        if not books:
            print("⚠️ No books found on this page. Stopping.")
            break

        collected.extend(books)
        print(f"✅ Collected so far: {len(collected)} books")

        current_url = next_url
        time.sleep(1)  # Be polite to the server

    # Trim to target count
    collected = collected[:TARGET_COUNT]

    print(f"\n✅ Total scraped: {len(collected)} books")

    # Save results to JSON
    with open(OUTPUT_PAGE, "w", encoding="utf-8") as f:
        json.dump(collected, f, indent=2, ensure_ascii=False)

    print(f"💾 Data saved to {OUTPUT_PAGE}")


if __name__ == "__main__":
    main()
