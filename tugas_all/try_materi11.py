import requests
import re
import string
import nltk
import pandas as pd
from urllib import request
from bs4 import BeautifulSoup as bs
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
nltk.download('stopwords')
nltk.download('punkt')

URL = 'https://regional.kompas.com/read/2021/01/18/15434451/kristen-gray-dicari-petugas-karena-ajak-turis-asing-ramai-ramai-tinggal-di?page=all'
USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'
ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

header = {
    'user_agent': USER_AGENT,
    'accept': ACCEPT
}

req = request.Request(URL, headers=header)
html = request.urlopen(req)

scrap = bs(html, 'html.parser')
content = scrap.find('div', {'class': 'read__content'})
strong_element = content.findAll('strong')
for i in strong_element:
    i.decompose()

parag = content.findAll('p')
result = [item.get_text() for item in parag]
stop_words = set(stopwords.words('indonesian'))
# cleaning
clear_sentence = []
for sentence in result:
    low = sentence.lower()
    num = re.sub(r"^\d+|^\d+\s|\d+|\d+\s|\d+/\d/\d+|\s\d+|\s\d+$", " ", low)
    punct_1 = re.sub(r"[^A-Za-z]", ' ', num)
    punct_2 = punct_1.translate(str.maketrans('', '', string.punctuation))
    striped = punct_2.strip()
    token = word_tokenize(striped)
    not_stopword = [word for word in token if word not in stop_words]
    clear_sentence.append(' '.join(not_stopword))

# stemming
stemmer = StemmerFactory().create_stemmer()
clean = []
for sentence in clear_sentence:
    clean.append(stemmer.stem(sentence))

clean.insert(
    0, 'Kristen Gray Dicari Petugas karena Ajak Turis Asing Ramai-ramai Tinggal di Bali')
clean.insert(1, URL)
del clean[21]
data = pd.Series(clean)
data.to_csv('tweet_file/berta_TA.csv', index=False)
