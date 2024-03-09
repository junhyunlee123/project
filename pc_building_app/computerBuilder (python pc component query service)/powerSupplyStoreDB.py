from bs4 import BeautifulSoup
import requests
from time import sleep
from random import randint
from componentScraper import storeComponentDataToDB


def find_power_supply(url, pageNum):
    componentList = []

    while True:
        powerSuppliesPage = requests.get(url)

        if 403 == powerSuppliesPage.status_code:
            print("Newegg automatic block detected. Waiting for Newegg to unblock the host...")
            sleep(3 * 60 * 60 + 60 * 30)
        else:
            powerSuppliesPage = powerSuppliesPage.text
            break

    powerSuppliesPageParsed = BeautifulSoup(powerSuppliesPage, 'html.parser')

    powerSupplies = powerSuppliesPageParsed.find_all('a', attrs={'class': 'item-title'})
    prices = powerSuppliesPageParsed.find_all('li', class_='price-current')

    imageLinks = powerSuppliesPageParsed.find_all('a', class_='item-img')
    productDetailPageLinks = powerSuppliesPageParsed.find_all('a', class_='item-title')
    # product detail page's <a> tag. Reference href to get the value of that attribute

    print('Power Supply for Page ' + str(pageNum) + ':\t')
    i = 0
    for powerSupply, price, imageLink, productDetailPageLink in \
            zip(powerSupplies, prices, imageLinks, productDetailPageLinks):
        i += 1

        componentName = powerSupply.text.strip()
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


def powerSupplyStoreToList():
    firstPageScraped = False

    powerSupplyList = []
    for page in range(1, 101):
        sleep(randint(1, 10))

        if not firstPageScraped:
            powerSupplyList.append(find_power_supply('https://www.newegg.com/Power-Supplies/SubCategory/ID-58?Tid=7657',
                                                     page))
            firstPageScraped = True
        else:
            URL = 'https://www.newegg.com/Power-Supplies/SubCategory/ID-58/Page-' + str(page) + '?Tid=7657'
            powerSupplyList.append(find_power_supply(URL, page))
    return powerSupplyList


if __name__ == '__main__':
    powerSupplyListOuter = powerSupplyStoreToList()
    print('Power Supply Product List:\n' + str(powerSupplyListOuter))
    storeComponentDataToDB(powerSupplyListOuter, 'powerSupplies')
