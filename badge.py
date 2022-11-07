# 網路連線
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as request
import json
src="https://badge.g0v.tw/_/user/api/ronnywang"
with request.urlopen(src) as response:
    data=json.load(response) #利用json模組讀取資料
# 可以印出所有資料打 print(data)
plist=data["services"]
#可以印出特定位置資料 例如這邊只印有哪些服務的區塊 print(plist)
for person in plist:
    print(person["service"])

with open("dataservices.txt","w",encoding="utf-8") as file: # 打開一個新檔案，w 代表寫入, 資料有中文
    for person in plist: #抓公司資料
        file.write(person["service"]+"\n") #寫入檔案變成一個 txt 檔案