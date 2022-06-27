from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup

timeNow = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
f = open('stock prices - started at ' + timeNow + '.txt', 'a')
f.write('Web scrapping for stock prices on investing.com \n\n')

def getData():
    r = requests.get(url)
    soup  = BeautifulSoup(r.content, 'html.parser')
    price = soup.find(attrs={ 'data-test' : "instrument-price-last"})
    company_name = soup.find(class_='text-2xl font-semibold instrument-header_title__GTWDv mobile:mb-2')
    changePrecent = soup.find(attrs={'data-test' : 'instrument-price-change-percent'})
    output  = timeNow + ' -- ' + company_name.text + ': $' + price.text + ' ' + changePrecent.text
    print(output)

    f.write(output + '\n')


print('Web scrapping for stock prices on investing.com')
company = input('Enter the company name or URL on investing.com: ')
timeGap  = int(input('Enter time gap to fetch stock data (in seconds): '))
if(company.startswith('http')):
    url = company
    while True:
        getData()
        time.sleep(timeGap)
else:
    url = 'https://www.investing.com/equities/' + company
    while True:
        getData()
        time.sleep(timeGap)
