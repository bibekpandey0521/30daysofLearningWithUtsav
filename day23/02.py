from bs4 import BeautifulSoup

html_content = "<h1>Main Title</h1><p>This is a sample paragraph</p><a href='https://example.com'>Click Here</a>"
soup = BeautifulSoup(html_content,"html.parser")
print(soup.h1.text)
print(soup.p.text)