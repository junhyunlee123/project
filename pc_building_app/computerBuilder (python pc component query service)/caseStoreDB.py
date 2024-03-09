from bs4 import BeautifulSoup
import requests
from time import sleep
from random import randint
from componentScraper import storeComponentDataToDB


def find_cases(url, pageNum):
    componentList = []

    while True:
        casesPage = requests.get(url)

        if 403 == casesPage.status_code:
            print("Newegg automatic block detected. Waiting for Newegg to unblock the host...")
            sleep(3 * 60 * 60 + 60 * 30)
        else:
            casesPage = casesPage.text
            break

    casesPageParsed = BeautifulSoup(casesPage, 'html.parser')

    cases = casesPageParsed.find_all('a', attrs={'class': 'item-title'})
    prices = casesPageParsed.find_all('li', class_='price-current')

    imageLinks = casesPageParsed.find_all('a', class_='item-img')
    productDetailPageLinks = casesPageParsed.find_all('a', class_='item-title')
    # product detail page's <a> tag. Reference href to get the value of that attribute

    print('PC Cases for Page ' + str(pageNum) + ':\t')
    i = 0
    for case, price, imageLink, productDetailPageLink in zip(cases, prices, imageLinks, productDetailPageLinks):
        i += 1

        componentName = case.text.strip()
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


def caseStoreToList():
    firstPageScraped = False

    caseList = []
    for page in range(1, 101):
        sleep(randint(1, 10))

        if not firstPageScraped:
            caseList.append(find_cases('https://www.newegg.com/Computer-Cases/SubCategory/ID-7?Tid=7583', page))
            firstPageScraped = True
        else:
            URL = 'https://www.newegg.com/Computer-Cases/SubCategory/ID-7/Page-' + str(page) + '?Tid=7583'
            caseList.append(find_cases(URL, page))
    return caseList


if __name__ == '__main__':
    caseListOuter = caseStoreToList()
    print('PC Case Product List:\n' + str(caseListOuter))
    storeComponentDataToDB(caseListOuter, 'cases')
