import requests
import re
import string
from urllib import request
from bs4 import BeautifulSoup as bs
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'
ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
URL = 'https://nasional.kompas.com/read/2020/10/15/18022671/polri-ungkap-percakapan-para-tersangka-di-grup-whatsapp-kami-medan?page=all#page2'

header = {
    'user_agent': USER_AGENT,
    'accept': ACCEPT
}
req = request.Request(URL, headers=header)
op = request.urlopen(req)

data = bs(op, 'html.parser')
box = data.find('div', {'class': 'read__content'})
strong_element = box.findAll('strong')
for i in strong_element:
    i.decompose()
items = box.findAll('p')
result = [item.get_text() for item in items]

low = [i.lower() for i in result]
clr_punct = [word.translate(str.maketrans('', '', string.punctuation)).strip() for word in low]
split = [clr.split() for clr in clr_punct]
joined = []
for i in split:
    joined.append(' '.join(i))
print(joined)