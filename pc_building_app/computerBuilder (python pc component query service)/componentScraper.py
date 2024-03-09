import datetime
from time import sleep
import mysql.connector


def storeComponentDataToDB(componentList, componentTypeDBName):
    mysqlDB = mysql.connector.connect(
        host='ec2-18-218-17-22.us-east-2.compute.amazonaws.com',
        port='3306',
        time_zone='-06:00',

        user='root',
        password='EaCJoon@ted',
        database='computerParts'
    )
    print('MySQL Database connected. mysql object:\t' + str(mysqlDB))

    mysqlDBCursor = mysqlDB.cursor()
    mysqlDBCursor.execute('DELETE FROM ' + componentTypeDBName)

    sqlStatement = 'INSERT INTO ' + componentTypeDBName + \
                   ' (productName, price, productImage, productDetailURL) VALUES (%s, %s, %s, %s)'

    for page in componentList:
        for product in page:
            tupleProduct = tuple(product)
            print('Inserting tuple Data... :\t' + str(tupleProduct))
            mysqlDBCursor.execute(sqlStatement, tuple(product))
            print(str(mysqlDBCursor.rowcount) + ' Records inserted')

    mysqlDB.commit()  # actually writes data to the database


if __name__ == '__main__':
    import caseStoreDB, coolingStoreDB, graphicsCardStoreDB, memoryStoreDB, motherboardStoreDB, powerSupplyStoreDB, \
        processorStoreDB, storageStoreDB

    print("This program updates MySQL database every 8 hours to match Newegg's newest PC components.")

    while True:
        timeNow = datetime.datetime.now()
        # timezone not configured correctly (displayed in +0:00). Correct it in the future development.

        print(
            timeNow.strftime('%A') + '\t' + timeNow.strftime('%B') + ' / ' + str(timeNow.day) + ' / '
            + str(timeNow.year) + '\t' + timeNow.strftime('%I') + ' : ' + str(timeNow.minute) + ' : '
            + str(timeNow.second) + ' ' + timeNow.strftime('%p'))

        print('Querying and Updating PC components from Newegg to the Database...\n')
        processorList = processorStoreDB.processorStoreToList()
        print('Processor (CPU) Query complete. Queried components:\n' + str(processorList))
        storeComponentDataToDB(processorList, 'processors')

        motherboardList = motherboardStoreDB.motherboardStoreToList()
        print('AMD MotherBoard (Mainboard) Query complete. Queried components:\n' + str(motherboardList[0]))
        storeComponentDataToDB(motherboardList[0], 'amdMotherboards')

        print("Waiting for 25 minutes to avoid newegg blocking mechanism...")
        sleep(0.25 * 60 * 60)
        print('Update Process resuming after 25 minutes...')
        # sleep 25 minutes (to avoid blocking)

        print('Intel MotherBoard (Mainboard) Query complete. Queried components:\n' + str(motherboardList[1]))
        storeComponentDataToDB(motherboardList[1], 'intelMotherboards')

        vgaList = graphicsCardStoreDB.graphicsCardStoreToList()
        print('AMD Graphics Card (VGA) Query complete. Queried components:\n' + str(vgaList[0]))
        storeComponentDataToDB(vgaList[0], 'amdGraphicsCards')

        print("Waiting for 25 minutes to avoid newegg blocking mechanism...")
        sleep(0.25 * 60 * 60)
        print('Update Process resuming after 25 minutes...')
        # sleep 25 minutes (to avoid blocking)

        print('NVIDIA Graphics Card (VGA) Query complete. Queried components:\n' + str(vgaList[1]))
        storeComponentDataToDB(vgaList[1], 'nvidiaGraphicsCards')

        caseList = caseStoreDB.caseStoreToList()
        print('PC Case Query complete. Queried components:\n' + str(caseList))
        storeComponentDataToDB(caseList, 'cases')

        print("Waiting for 25 minutes to avoid newegg blocking mechanism...")
        sleep(0.25 * 60 * 60)
        print('Update Process resuming after 25 minutes...')
        # sleep 25 minutes (to avoid blocking)

        memoryList = memoryStoreDB.memoryStoreToList()
        print('Memory (RAM) Query complete. Queried components:\n' + str(memoryList))
        storeComponentDataToDB(memoryList, 'memories')

        storageList = storageStoreDB.storageStoreToList()
        print('HDD (Hard Disk Drive) Query complete. Queried components:\n' + str(storageList[0]))
        storeComponentDataToDB(storageList[0], 'hddStorages')

        print("Waiting for 25 minutes to avoid newegg blocking mechanism...")
        sleep(0.25 * 60 * 60)
        print('Update Process resuming after 25 minutes...')
        # sleep 25 minutes (to avoid blocking)

        print('SSD (Solid State Drive) Query complete. Queried components:\n' + str(storageList[1]))
        storeComponentDataToDB(storageList[1], 'ssdStorages')

        powerSupplyList = powerSupplyStoreDB.powerSupplyStoreToList()
        print('Power Supply Query complete. Queried components:\n' + str(powerSupplyList))
        storeComponentDataToDB(powerSupplyList, 'powerSupplies')

        print("Waiting for 25 minutes to avoid newegg blocking mechanism...")
        sleep(0.25 * 60 * 60)
        print('Update Process resuming after 25 minutes...')
        # sleep 25 minutes (to avoid blocking)

        coolingList = coolingStoreDB.coolingStoreToList()
        print('CPU Air Cooler Query complete. Queried components:\n' + str(coolingList[0]))
        storeComponentDataToDB(coolingList[0], 'cpuAirCoolerCoolings')

        print('Liquid/Water Cooler Query complete. Queried components:\n' + str(coolingList[1]))
        storeComponentDataToDB(coolingList[1], 'liquidOrWaterCoolerCoolings')

        print("Waiting for 25 minutes to avoid newegg blocking mechanism...")
        sleep(0.25 * 60 * 60)
        print('Update Process resuming after 25 minutes...')
        # sleep  25 minutes (to avoid blocking)

        print('PC Case Fan Query complete. Queried components:\n' + str(coolingList[2]))
        storeComponentDataToDB(coolingList[2], 'pcCaseFanCoolings')

        print('\nAll PC components are newly Queried and Updated to the Database.')

        for i in range(1, 73):
            timeNow = datetime.datetime.now()
            print(
                timeNow.strftime('%A') + '\t' + timeNow.strftime('%B') + ' / ' + str(timeNow.day) + ' / ' + str(
                    timeNow.year) +
                '\t' + timeNow.strftime('%I') + ' : ' + str(timeNow.minute) + ' : '
                + str(timeNow.second) + ' ' + timeNow.strftime('%p'))
            sleep(0.5 * 60 * 10)  # sleep 5 minutes

        print('6 hrs elapsed. Update process will start again after 360 Minutes or 6 Hours from the Last '
              'Update')
