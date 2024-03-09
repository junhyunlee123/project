from bs4 import BeautifulSoup
import requests
from time import sleep
from random import randint
from componentScraper import storeComponentDataToDB


def find_motherboards(url, pageNum):
    componentList = []

    while True:
        motherboardsPage = requests.get(url)

        if 403 == motherboardsPage.status_code:
            print("Newegg automatic block detected. Waiting for Newegg to unblock the host...")
            sleep(3 * 60 * 60 + 60 * 30)
        else:
            motherboardsPage = motherboardsPage.text
            break

    motherboardsPageParsed = BeautifulSoup(motherboardsPage, 'html.parser')

    motherboards = motherboardsPageParsed.find_all('a', attrs={'class': 'item-title'})
    prices = motherboardsPageParsed.find_all('li', class_='price-current')

    imageLinks = motherboardsPageParsed.find_all('a', class_='item-img')
    productDetailPageLinks = motherboardsPageParsed.find_all('a', class_='item-title')
    # product detail page's <a> tag. Reference href to get the value of that attribute

    print('Motherboard (Mainboard) for Page ' + str(pageNum) + ':\t')
    i = 0
    for motherboard, price, imageLink, productDetailPageLink in \
            zip(motherboards, prices, imageLinks, productDetailPageLinks):

        i += 1

        componentName = motherboard.text.strip()
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


def motherboardStoreToList():
    # AMD motherboards
    print('AMD Motherboards (Mainboards):')

    firstPageScraped = False

    amdMotherBoardList = []

    for page in range(1, 76):
        sleep(randint(1, 10))

        if not firstPageScraped:
            amdMotherBoardList.append(find_motherboards(
                'https://www.newegg.com/AMD-Motherboards/SubCategory/ID-22?Tid=7625&cm_sp=Cat_Motherboards_1'
                '-_-Visnav-_-AMD-Motherboards_2', page))
            firstPageScraped = True
        else:
            URL = 'https://www.newegg.com/p/pl?tid=7625&page=' + str(page) + '&N=100007625'
            amdMotherBoardList.append(find_motherboards(URL, page))

    # Intel Motherboards
    print('Intel Motherboards (Mainboards):')

    firstPageScraped = False

    intelMotherBoardList = []
    for page in range(1, 101):
        sleep(randint(1, 10))

        if not firstPageScraped:
            intelMotherBoardList.append(
                find_motherboards('https://www.newegg.com/Intel-Motherboards/SubCategory/ID-280?Tid=7627&cm_sp'
                                  '=Cat_Motherboards_2-_-Visnav-_-Intel-Motherboards_1', page))
            firstPageScraped = True
        else:
            URL = 'https://www.newegg.com/Intel-Motherboards/SubCategory/ID-280/Page-' + str(page) + '?Tid=7627'
            intelMotherBoardList.append(find_motherboards(URL, page))
    return amdMotherBoardList, intelMotherBoardList


if __name__ == '__main__':
    motherboardListOuter = motherboardStoreToList()

    print('AMD MotherBoard (Mainboard) Product List:\n' + str(motherboardListOuter[0]))
    storeComponentDataToDB(motherboardListOuter[0], 'amdMotherboards')

    print('Waiting for just 10 minutes until going to next query...')
    sleep(60 * 10)  # sleep 10 minutes

    print('Intel MotherBoard (Mainboard) Product List:\n' + str(motherboardListOuter[1]))
    storeComponentDataToDB(motherboardListOuter[1], 'intelMotherboards')
