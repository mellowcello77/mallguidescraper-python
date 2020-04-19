import urllib
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import csv
from datetime import datetime
import requests
import numpy as np
import random
import requests
from bs4 import BeautifulSoup
import re


print('---------Getting All Mall URLS From Website---------')
print('')
print('')
print('')


time.sleep(4)

# get
data = requests.get("https://www.mallguide.co.za/malls")

# load into bs4
soup = BeautifulSoup(data.text, 'html.parser')

for div in soup.find_all("a", {"class": "bluetextthin cool-link"}):
    f = open('mallsurls.txt', 'a+')
    f.write('http://www.mallguide.co.za'+div.get('href'))
    f.write('\n')
    print('www.mallguide.co.za'+div.get('href'))

print('')
print('')
print('')
print('---------All URLS Saved to File, Please Wait---------')
print('')
print('')
print('')

time.sleep(3)

# header presented to server
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
r = requests.get("https://www.mallguide.co.za/", headers=headers, timeout=5)

# open the file with URL's
f = open('mallsurls.txt', 'r')


print('---------Opening File With URL\'S To Scrape---------')
print('')
print('')
print('')


time.sleep(1)

with open('mallsurls.txt') as file:
    line_count = 0
    for line in file:
        line_count += 1

print('---------Total Malls To Scrape : %s ---------' % (line_count))
print('')
print('')
print('')

time.sleep(1)

print('---------Fetching Mall Information at Random Intervals, This Will Take Long---------')
print('')
print('')
print('')


time.sleep(1)

# for every line in the file
for line in f:
    try:
        page = urllib.request.urlopen(line)
    except Exception:
        continue

    # soup fetch content from the page if site response on link link is succ 200
    if r.status_code == 200:
        soup = BeautifulSoup(page, 'html.parser')

    # get items details
    mallName = soup.find_all('span', {'class':'darkbluetext'})[0]
    mallName = mallName.text.strip()

    mallTel = soup.find_all('span', {'class':'darkbluetext'})[1]
    mallTel = mallTel.text.strip()

    mallLocation = soup.find_all('span', {'class':'darkbluetext'})[2]
    mallLocation = mallLocation.text.strip()

    mallUrl = soup.find('a', {'class':'darkbluetext'})
    mallUrl = mallUrl.text.strip()

    mallAddress = soup.find('div', {'class':'mallbluebocks text-left'})
    mallAddress = mallAddress.text.strip()

    # Fix up Physicall Address
    mallAddressNoSpace = re.sub('[ \t\n]+', ' ', mallAddress)
    # print(mallAddressNoSpace)

    str1a = mallAddressNoSpace
    str1b = str1a.replace("PHYSICAL ADDRESS", "|")

    str2a = str1b
    str2b = str2a.replace("POSTAL ADDRESS", "")

    str3a = str2b
    str3b = str3a.replace("PROVINCE", "|")

    str4a = str3b
    str4b = str4a.replace("CITY", "|")

    str5a = str4b
    str5b = str5a.replace(",", ";")

    # set variable to write
    results = (mallName+'|'+mallTel+'|'+mallLocation+'|'+mallUrl+'|'+str5b)


    #write data to file
    f = open('scrapeddata.csv', 'a+')
    f.write(results)
    f.write('\n')
    f.close()
    print(results)
    print('')
    print('-----------Fetching Next at Random Intervals, Please Be Patient--------------')
    print('')
    
    # Random delays before calling next url to prevent being blocked
    delays = [1, 1, 2, 3, 2, 1, 3]
    delay = np.random.choice(delays)
    time.sleep(delay)

print('')
print('')
print('')
print('-----------FINISHED, CHECK "SCRAPEDDATA.CSV" FILE--------------')
print('')
print('')
print('')
print('-----------HAVE A NICE DAY - WB--------------')
print('')
print('')
print('')