from bs4 import BeautifulSoup
import requests
from time import sleep
from random import randint
from componentScraper import storeComponentDataToDB


def find_storages(url, pageNum):
    componentList = []

    while True:
        storagesPage = requests.get(url)

        if 403 == storagesPage.status_code:
            print("Newegg automatic block detected. Waiting for Newegg to unblock the host...")
            sleep(3 * 60 * 60 + 60 * 30)
        else:
            storagesPage = storagesPage.text
            break

    storagesPageParsed = BeautifulSoup(storagesPage, 'html.parser')

    storages = storagesPageParsed.find_all('a', attrs={'class': 'item-title'})
    prices = storagesPageParsed.find_all('li', class_='price-current')
    
    imageLinks = storagesPageParsed.find_all('a', class_='item-img')
    productDetailPageLinks = storagesPageParsed.find_all('a', class_='item-title')
    # product detail page's <a> tag. Reference href to get the value of that attribute

    print('Storage for Page ' + str(pageNum) + ':\t')
    i = 0
    for storage, price, imageLink, productDetailPageLink in zip(storages, prices, imageLinks, productDetailPageLinks):
        i += 1

        componentName = storage.text.strip()
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
            componentPrice = -1  # value -1 means out of stock

        print(str(i) + ':\t' + componentName + '\tPrice: $' + str(componentPrice) + '\tImage Link: ' +
              componentImageLink + '\tProduct Detail Page Link: ' + productDetailPageLink['href'])

        componentList.append([componentName, componentPrice, componentImageLink, productDetailPageLink['href']])
    return componentList


def storageStoreToList():
    # HDD (Hard Disk Drive)
    print('HDDs (Hard Disk Drives):')

    firstPageScraped = False

    HDDList = []
    for page in range(1, 101):
        sleep(randint(1, 10))

        if not firstPageScraped:
            HDDList.append(find_storages('https://www.newegg.com/Desktop-Internal-Hard-Drives/SubCategory/'
                                         'ID-14?Tid=167523',
                                         page))
            firstPageScraped = True
        else:
            URL = 'https://www.newegg.com/Desktop-Internal-Hard-Drives/SubCategory/ID-14/Page-' + str(page) + \
                  '?Tid=167523'
            HDDList.append(find_storages(URL, page))

    # SSD (Solid State Drive)
    print('SSDs (Solid State Drives):')

    firstPageScraped = False

    SSDList = []
    for page in range(1, 101):
        sleep(randint(1, 10))

        if not firstPageScraped:
            SSDList.append(find_storages('https://www.newegg.com/Internal-SSDs/SubCategory/ID-636?Tid=11693', page))
            firstPageScraped = True
        else:
            URL = 'https://www.newegg.com/Internal-SSDs/SubCategory/ID-636/Page-' + str(page) + '?Tid=11693'
            SSDList.append(find_storages(URL, page))
    return HDDList, SSDList


if __name__ == '__main__':
    storageListOuter = storageStoreToList()

    print('HDD (Hard Disk Drive) Product List:\n' + str(storageListOuter[0]))
    storeComponentDataToDB(storageListOuter[0], 'hddStorages')

    print('Waiting for just 10 minutes until going to next query...')
    sleep(60 * 10)  # sleep 10 minutes

    print('SSD (Solid State Drive) Product List:\n' + str(storageListOuter[1]))
    storeComponentDataToDB(storageListOuter[1], 'ssdStorages')
