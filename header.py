import requests
from bs4 import BeautifulSoup

url = "https://dir.indiamart.com/impcat/steel-plates.html"

payload = {}
headers = {
  'Cookie': 'r=g'
}

response = requests.request("GET", url, headers=headers, data=payload)

html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

Steelinfo = soup.find('div', class_='lst-cell flx1')
print(Steelinfo.text.split('\n'))
print(type(Steelinfo))

with open('indiamart.txt', 'w',encoding='utf-8') as file:


# Loop through the contents of the tag
    for item in Steelinfo.contents:
        # Check if the item is a NavigableString (text) or another Tag
        if isinstance(item, str):
            # print(f"Text: {item.strip()}")
            file.write("Text: " + item.strip() + "\n")

        elif item.name:
            # print(f"Tag Name: {item.name}")
            # print(f"Tag Content: {item.text.strip()}")
            file.write("Tag Name: " + item.name.strip() + "\n")
            file.write("Tag Content: " + item.text.strip() + "\n")

        else:
            # print("Unknown content")
            file.write("Unknown content" + "\n")
            
