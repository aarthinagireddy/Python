from bs4 import BeautifulSoup
import requests
import csv

url = "https://scikit-learn.org/stable/modules/clustering.html#clustering"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "html.parser")

table = soup.find("table")
rows = table.select('tr')

with open('output1.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        header = [th.text.rstrip() for th in rows[0].find_all('th')]
        writer.writerow(header)
        for tr in rows[1:]:
            td = tr.find_all("td")
            row1 = [i.text.rstrip() for i in td]
            writer.writerow(row1)


