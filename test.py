
from pykrx import stock
import KIS_API_Helper_KR as KisKR
import pprint


#계좌 잔고를 가지고 온다!
Balance = KisKR.GetBalance()
#####################################################################################################################################

'''-------통합 증거금 사용자는 아래 코드도 사용할 수 있습니다! -----------'''
#통합증거금 계좌 사용자 분들중 만약 미국계좌랑 통합해서 총자산을 계산 하고 포트폴리오 비중에도 반영하고 싶으시다면 아래 코드를 사용하시면 되고 나머지는 동일합니다!!!
#Balance = Common.GetBalanceKrwTotal()

'''-----------------------------------------------------------'''
#####################################################################################################################################


print("--------------내 보유 잔고---------------------")

pprint.pprint(Balance)

print("--------------------------------------------")

# #코스닥 지수 확인
# for index_v in stock.get_index_ticker_list(market='KOSDAQ'): #KOSPI 지수도 확인 가능!
#     print(index_v, stock.get_index_ticker_name(index_v))

# print("-----------------------------------------------------------------")

# #코스피 지수 확인
# for index_v in stock.get_index_ticker_list(market='KOSPI'): #KOSPI 지수도 확인 가능!
#     print(index_v, stock.get_index_ticker_name(index_v))