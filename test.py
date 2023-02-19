import KIS_Common as common


print("REAL_APP_KEY:" , common.GetAppKey("REAL"))
print("REAL_APP_SECRET:" , common.GetAppSecret("REAL"))
print("REAL_CANO" , common.GetAccountNo("REAL"))
print("REAL_ACNT_PRDT_CD" , common.GetPrdtNo("REAL"))
print("REAL_URL" , common.GetUrlBase("REAL"))

print("----------------------------------------------------")

print("VIRTUAL_APP_KEY:" , common.GetAppKey("VIRTUAL"))
print("VIRTUAL_APP_SECRET:" , common.GetAppSecret("VIRTUAL"))
print("VIRTUAL_CANO" , common.GetAccountNo("VIRTUAL"))
print("VIRTUAL_ACNT_PRDT_CD" , common.GetPrdtNo("VIRTUAL"))
print("VIRTUAL_URL" , common.GetUrlBase("VIRTUAL"))
