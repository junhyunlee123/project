from bs4 import BeautifulSoup
import requests
from time import sleep
from random import randint
from componentScraper import storeComponentDataToDB


def find_coolings(url, pageNum):
    componentList = []

    while True:
        coolingsPage = requests.get(url)

        if 403 == coolingsPage.status_code:
            print("Newegg automatic block detected. Waiting for Newegg to unblock the host...")
            sleep(3 * 60 * 60 + 60 * 30)
        else:
            coolingsPage = coolingsPage.text
            break

    coolingsPageParsed = BeautifulSoup(coolingsPage, 'html.parser')

    coolings = coolingsPageParsed.find_all('a', attrs={'class': 'item-title'})
    prices = coolingsPageParsed.find_all('li', class_='price-current')

    imageLinks = coolingsPageParsed.find_all('a', class_='item-img')
    productDetailPageLinks = coolingsPageParsed.find_all('a', class_='item-title')
    # product detail page's <a> tag. Reference href to get the value of that attribute

    print('PC Cooling for Page ' + str(pageNum) + ':\t')
    i = 0
    for cooling, price, imageLink, productDetailPageLink in zip(coolings, prices, imageLinks, productDetailPageLinks):
        i += 1

        componentName = cooling.text.strip()
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


def coolingStoreToList():
    # CPU Air cooler
    print('CPU Air Cooler:')

    firstPageScraped = False

    airProcessorCoolerList = []
    for page in range(1, 101):
        sleep(randint(1, 10))

        if not firstPageScraped:
            airProcessorCoolerList.append(
                find_coolings('https://www.newegg.com/CPU-Fans-Heatsinks/SubCategory/ID-574', page))
            firstPageScraped = True
        else:
            URL = 'https://www.newegg.com/CPU-Fans-Heatsinks/SubCategory/ID-574/Page-' + str(page)
            airProcessorCoolerList.append(find_coolings(URL, page))

    # Liquid/Water cooler
    print('Liquid/Water Cooler:')

    firstPageScraped = False

    liquidOrWaterCoolerList = []
    for page in range(1, 101):
        sleep(randint(1, 10))

        if not firstPageScraped:
            liquidOrWaterCoolerList.append(find_coolings('https://www.newegg.com/Water-Liquid-Cooling/SubCategory/ID'
                                                         '-575?cm_sp=Cat_Fans-PC-Cooling_2-_-VisNav-_-Water-Liquid'
                                                         '-Coolers',
                                                         page))
            firstPageScraped = True
        else:
            URL = 'https://www.newegg.com/p/pl?cm_sp=Cat_Fans-PC-Cooling_2-_-VisNav-_-Water-Liquid-Coolers&page=2' + \
                  str(page) + '&N=100008008'
            liquidOrWaterCoolerList.append(find_coolings(URL, page))

    # Case Fans
    print('PC Case Fans:')

    firstPageScraped = False

    caseFanList = []
    for page in range(1, 101):
        sleep(randint(1, 10))

        if not firstPageScraped:
            caseFanList.append(find_coolings('https://www.newegg.com/Case-Fans/SubCategory/ID-573?cm_sp=Cat_Fans-PC'
                                             '-Cooling_3-_-VisNav-_-Case-Fans', page))
            firstPageScraped = True
        else:
            URL = 'https://www.newegg.com/p/pl?cm_sp=Cat_Fans-PC-Cooling_3-_-VisNav-_-Case-Fans&page=' + \
                  str(page) + '&N=100007998'
            caseFanList.append(find_coolings(URL, page))
    return airProcessorCoolerList, liquidOrWaterCoolerList, caseFanList


if __name__ == '__main__':
    coolingListOuter = coolingStoreToList()

    print('CPU Air Cooler Product List:\n' + str(coolingListOuter[0]))
    storeComponentDataToDB(coolingListOuter[0], 'cpuAirCoolerCoolings')

    print('Waiting for just 10 minutes until going to next query...')
    sleep(60 * 10)  # sleep 10 minutes

    print('Liquid/Water Cooler Product List:\n' + str(coolingListOuter[1]))
    storeComponentDataToDB(coolingListOuter[1], 'liquidOrWaterCoolerCoolings')

    print('Waiting for just 10 minutes until going to next query...')
    sleep(60 * 10)  # sleep 10 minutes

    print('PC Case Fan Product List:\n' + str(coolingListOuter[2]))
    storeComponentDataToDB(coolingListOuter[2], 'pcCaseFanCoolings')
