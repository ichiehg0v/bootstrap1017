#MACOS 要 ssl 過認證一定要寫的
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
url="https://www.ptt.cc/bbs/Gossiping/index.html"

#建立一個 request 附加 request header 資訊（在 F12 Network→Index.html→Request headers 獲得）
request=req.Request(url,headers={
    "user-agent": "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1"
})

with req.urlopen(request) as response:
    data=response.read() .decode("utf-8")
print(data)

# 卡在要裝 beautifulsoup，但 ronny 建議熟悉建議對於 python 的 virtualenv 或是 venv 要多了解一些
# 他對於讓每個專案自己有不一樣的套件版本很重要
# 慕約的視覺化專案很多死掉不能用就是因為他沒善用 nodejs 的類似工具，導致很多套件一升級舊專案就死了



