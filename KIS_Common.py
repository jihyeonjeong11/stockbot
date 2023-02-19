import yaml


stock_info = None

#설정 파일 정보를 읽어 옵니다.
with open('/var/autobot/myStockInfo.yaml', encoding='UTF-8') as f:
    stock_info = yaml.load(f, Loader=yaml.FullLoader)
    
    
#앱 키를 반환하는 함수
def GetAppKey(dist = "REAL"):
    
    global stock_info
    
    key = ""
    
    if dist == "REAL":
        key = "REAL_APP_KEY"
    elif dist == "VIRTUAL":
        key = "VIRTUAL_APP_KEY"
        
    return stock_info[key]


#앱시크릿을 리턴!
def GetAppSecret(dist = "REAL"):
    
    global stock_info
    
    key = ""
    
    if dist == "REAL":
        key = "REAL_APP_SECRET"
    elif dist == "VIRTUAL":
        key = "VIRTUAL_APP_SECRET"
        
    return stock_info[key]


#계좌 정보(계좌번호)를 리턴!
def GetAccountNo(dist = "REAL"):
    global stock_info
    
    key = ""
    
    if dist == "REAL":
        key = "REAL_CANO"
    elif dist == "VIRTUAL":
        key = "VIRTUAL_CANO"
        
    return stock_info[key]


#계좌 정보(삼품코드)를 리턴!
def GetPrdtNo(dist = "REAL"):
    global stock_info
    
    key = ""
    
    if dist == "REAL":
        key = "REAL_ACNT_PRDT_CD"
    elif dist == "VIRTUAL":
        key = "VIRTUAL_ACNT_PRDT_CD"
        
    return stock_info[key]


#URL주소를 리턴!
def GetUrlBase(dist = "REAL"):
    global stock_info
    
    key = ""
    
    if dist == "REAL":
        key = "REAL_URL"
    elif dist == "VIRTUAL":
        key = "VIRTUAL_URL"
        
    return stock_info[key]





        
    
    