# Wikipedia Article Scraper
import requests
from bs4 import BeautifulSoup

# Step 1: Get Wikipedia Article HTML
def get_wikipedia_page(topic):
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.118 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.text, "html.parser")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}. Check the topic and try again.")
        return None

# Step 2: Extract Article Title
def get_article_title(soup):
    return soup.find('h1').text

# Step 3: Extract Article Summary (first non-empty paragraph)
def get_article_summary(soup):
    paragraphs = soup.find_all('p')
    for para in paragraphs:
        if para.text.strip():
            return para.text.strip()
    return "No summary found."

# Step 4: Extract Headings (h2, h3, h4)
def get_headings(soup):
    return [heading.text.strip() for heading in soup.find_all(['h2', 'h3', 'h4'])]

# Step 5: Extract Related Links (limit to 5, unique)
def get_related_links(soup):
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/wiki/') and ":" not in href:
            full_url = f"https://en.wikipedia.org{href}"
            links.append(full_url)
    return list(set(links))[:5]

# Step 6: Main Program
def main():
    topic = input("Enter a topic to search on Wikipedia: ").strip()
    soup = get_wikipedia_page(topic)
    
    if soup:
        title = get_article_title(soup)
        summary = get_article_summary(soup)
        headings = get_headings(soup)
        related_links = get_related_links(soup)

        print("\n--- Wikipedia Article Details ---")
        print(f"\nTitle: {title}")
        print(f"\nSummary: {summary}")

        print("\nHeadings:")
        for heading in headings:
            print(f"- {heading}")

        print("\nRelated Links:")
        for link in related_links:
            print(f"- {link}")

# Run Program
if __name__ == "__main__":
    main()
