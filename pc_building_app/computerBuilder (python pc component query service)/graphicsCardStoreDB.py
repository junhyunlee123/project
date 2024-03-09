from bs4 import BeautifulSoup
import requests
from time import sleep
from random import randint


from componentScraper import storeComponentDataToDB


def find_vgas(url, pageNum):
    componentList = []

    while True:
        vgasPage = requests.get(url)

        if 403 == vgasPage.status_code:
            print("Newegg automatic block detected. Waiting for Newegg to unblock the host...")
            sleep(3 * 60 * 60 + 60 * 30)
        else:
            vgasPage = vgasPage.text
            break

    vgasPageParsed = BeautifulSoup(vgasPage, 'html.parser')

    vgas = vgasPageParsed.find_all('a', attrs={'class': 'item-title'})
    prices = vgasPageParsed.find_all('li', class_='price-current')

    imageLinks = vgasPageParsed.find_all('a', class_='item-img')
    productDetailPageLinks = vgasPageParsed.find_all('a', class_='item-title')
    # product detail page's <a> tag. Reference href to get the value of that attribute

    print('Graphics Card (VGA) for Page ' + str(pageNum) + ':\t')
    i = 0
    for vga, price, imageLink, productDetailPageLink in zip(vgas, prices, imageLinks, productDetailPageLinks):
        i += 1

        componentName = vga.text.strip()
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
              componentImageLink + '\tProduct Detail Page Link:  ' + productDetailPageLink['href'])

        componentList.append([componentName, componentPrice, componentImageLink, productDetailPageLink['href']])
    return componentList


def graphicsCardStoreToList():
    # AMD VGAs
    print('AMD Graphics Cards (VGAs):')

    firstPageScraped = False

    amdVGAList = []
    for page in range(1, 15):
        sleep(randint(1, 10))

        if not firstPageScraped:
            amdVGAList.append(find_vgas('https://www.newegg.com/p/pl?N=100007709%20600100181', page))
            firstPageScraped = True
        else:
            URL = 'https://www.newegg.com/p/pl?N=100007709%20600100181&page=' + str(page)
            amdVGAList.append(find_vgas(URL, page))

    # NVIDIA VGAs
    print('NVIDIA Graphics Cards (VGAs):')

    firstPageScraped = False

    nvidiaVGAList = []
    for page in range(1, 51):
        sleep(randint(1, 10))

        if not firstPageScraped:
            nvidiaVGAList.append(find_vgas('https://www.newegg.com/p/pl?N=100007709%20600030348', page))
            firstPageScraped = True
        else:
            URL = 'https://www.newegg.com/p/pl?N=100007709%20600030348&page=' + str(page)
            nvidiaVGAList.append(find_vgas(URL, page))
    return amdVGAList, nvidiaVGAList


if __name__ == '__main__':
    vgaListOuter = graphicsCardStoreToList()

    print('AMD Graphics Card (VGA) Product List:\n' + str(vgaListOuter[0]))
    storeComponentDataToDB(vgaListOuter[0], 'amdGraphicsCards')

    print('Waiting for just 10 minutes until going to next query...')
    sleep(60 * 10)  # sleep 10 minutes

    print('NVIDIA Graphics Card (VGA) Product List:\n' + str(vgaListOuter[1]))
    storeComponentDataToDB(vgaListOuter[1], 'nvidiaGraphicsCards')
