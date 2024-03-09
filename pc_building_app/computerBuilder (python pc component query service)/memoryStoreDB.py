from bs4 import BeautifulSoup
import requests
from time import sleep
from random import randint
from componentScraper import storeComponentDataToDB


def find_rams(url, pageNum):
    componentList = []

    while True:
        ramsPage = requests.get(url)

        if 403 == ramsPage.status_code:
            print("Newegg automatic block detected. Waiting for Newegg to unblock the host...")
            sleep(3 * 60 * 60 + 60 * 30)
        else:
            ramsPage = ramsPage.text
            break

    ramsPageParsed = BeautifulSoup(ramsPage, 'html.parser')
    
    rams = ramsPageParsed.find_all('a', attrs={'class': 'item-title'})
    prices = ramsPageParsed.find_all('li', class_='price-current')
    
    imageLinks = ramsPageParsed.find_all('a', class_='item-img')
    productDetailPageLinks = ramsPageParsed.find_all('a', class_='item-title')
    # product detail page's <a> tag. Reference href to get the value of that attribute

    print('Memory (RAM) for Page ' + str(pageNum) + ':\t')
    i = 0
    for ram, price, imageLink, productDetailPageLink in zip(rams, prices, imageLinks, productDetailPageLinks):
        i += 1

        componentName = ram.text.strip()
        componentImageLink = imageLink.img['src'].strip()

        index = 0
        componentPrice = price.text.strip()
        for j in componentPrice:
            if j == ' ':
                break
            index += 1

        try:
            componentPrice = float(componentPrice[1:index].replace(',', ''))
        except ValueError:
            componentPrice = -1

        print(str(i) + ':\t' + componentName + '\tPrice: $' + str(componentPrice) + '\tImage Link: ' +
              componentImageLink + '\tProduct Detail Page Link: ' + productDetailPageLink['href'])

        componentList.append([componentName, componentPrice, componentImageLink, productDetailPageLink['href']])
    return componentList


def memoryStoreToList():
    firstPageScraped = False

    memoryList = []
    for page in range(1, 101):
        sleep(randint(1, 10))

        if not firstPageScraped:
            memoryList.append(find_rams('https://www.newegg.com/Desktop-Memory/SubCategory/ID-147?Tid=7611', page))
            firstPageScraped = True
        else:
            URL = 'https://www.newegg.com/Desktop-Memory/SubCategory/ID-147/Page-' + str(page) + '?Tid=7611'
            memoryList.append(find_rams(URL, page))
    return memoryList


if __name__ == '__main__':
    memoryListOuter = memoryStoreToList()
    print('Memory (RAM) Product List:\n' + str(memoryListOuter))
    storeComponentDataToDB(memoryListOuter, 'memories')
