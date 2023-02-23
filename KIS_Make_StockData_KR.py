# -*- coding: utf-8 -*-

import KIS_Common as Common
import pprint
import json
import time
import KIS_API_Helper_KR as KisKR
import line_alert #라인 메세지를 보내기 위함!



Common.SetChangeMode("REAL")


KoreaStockList = list()
#파일 경로입니다.
korea_file_path = "./var/autobot/KrStockCodeList.json"

try:
    #이 부분이 파일을 읽어서 리스트에 넣어주는 로직입니다. 
    with open(korea_file_path, 'r') as json_file:
        KoreaStockList = json.load(json_file)

except Exception as e:
    print("Exception by First")



line_alert.SendMessage("Make Stock Data Korea Start!!")


KrStockDataList = list()


for stock_code in KoreaStockList:

    try:


        print(stock_code, " ..Start.. ")

        data = KisKR.GetCurrentStatus(stock_code)

        
        
        if data['StockNowStatus'] == '00' or data['StockNowStatus'] == '55' or data['StockNowStatus'] == '57' : 

            if data['StockMarket'] == "ETN" or data['StockMarket'] == "ETF" or (float(data['StockPER']) == 0 and float(data['StockPBR']) == 0 and float(data['StockEPS']) == 0  and float(data['StockBPS']) == 0) :
                print("Maybe...ETF..ETN.. ")
            else:

                KrStockDataList.append(data)
                
                pprint.pprint(data)
            

            
        time.sleep(0.2)

        print(stock_code, " ..Done.. ")

    except Exception as e:
        print("Exception ", e)




print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
pprint.pprint(KrStockDataList)

print("--------------------------------------------------------")


#파일 경로입니다.
kr_data_file_path = "./var/autobot/KrStockDataList.json"
#파일에 리스트를 저장합니다
with open(kr_data_file_path, 'w') as outfile:
    json.dump(KrStockDataList, outfile)



line_alert.SendMessage("Make Stock Data Korea Done!!" + str(len(KrStockDataList)))

