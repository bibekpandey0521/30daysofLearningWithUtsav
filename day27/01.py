import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

BASE_URL = "https://books.toscrape.com/"
IMAGE_DIR = "images"

def sanitize_filename(title):
    return re.sub(r'[\\/*?:"<>|]', "_", title)

def download_image(img_url, filename):
    try:
        response = requests.get(img_url, stream=True, timeout=10)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
    except Exception as e:
        print(f"Failed to download {filename} - {e}")

def scrape_and_download_images():
    url = BASE_URL
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")[:10]

    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)

    for book in books:
        title = book.h3.a['title']
        relative_img = book.find("img")["src"]
        img_url = urljoin(BASE_URL, relative_img)

        filename = sanitize_filename(title) + ".jpeg"
        filepath = os.path.join(IMAGE_DIR, filename)

        print(f"Downloading: {title}")
        print(f"Image URL: {img_url}")
        print(f"Saved to: {filepath}\n")

        download_image(img_url, filepath)

    print("All 10 book covers downloaded to 'images/'")

if __name__ == "__main__":
    scrape_and_download_images()
