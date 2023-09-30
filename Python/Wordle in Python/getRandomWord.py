import re
import random

import requests

# We get list of five-letter words from meaningpedia.com
# found it linked from Wikipedia:
# https://en.wikipedia.org/wiki/Lists_of_English_words#External_links

# Get gameWord 4

meaningpedia_resp4 = requests.get("https://meaningpedia.com/4-letter-words?show=all")

pattern = re.compile(r'<span itemprop="name">(\w+)</span>')

word_list4 = pattern.findall(meaningpedia_resp4.text)

# Get gameWord 5

meaningpedia_resp5 = requests.get("https://meaningpedia.com/5-letter-words?show=all")

pattern = re.compile(r'<span itemprop="name">(\w+)</span>')

word_list5 = pattern.findall(meaningpedia_resp5.text)

# Get gameWord 6

meaningpedia_resp6 = requests.get("https://meaningpedia.com/6-letter-words?show=all")

pattern = re.compile(r'<span itemprop="name">(\w+)</span>')

word_list6 = pattern.findall(meaningpedia_resp6.text)


gameWord4 = random.choice(word_list4)
gameWord5 = random.choice(word_list5)
gameWord6 = random.choice(word_list6)
