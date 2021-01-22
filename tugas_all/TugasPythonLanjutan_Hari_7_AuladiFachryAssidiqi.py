import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

def kompas():
    KOMPAS = "https://www.kompas.com/"
    html = urlopen(KOMPAS)
    data = BeautifulSoup(html, 'html.parser')

    items = data.findAll("h4", {"class":"most__title"})
    data = []
    for item in items:
        data.append(item.get_text())
    print(pd.DataFrame(data, columns=['Judul Berita Populer']))

kompas()