import requests
from urllib.parse import unquote

geturl=r'https://www.barchart.com/futures/quotes/SBH23'
apiurl=r'https://www.barchart.com/proxies/core-api/v1/quotes/get'


getheaders={

    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }

getpay={
    'page': 'all'
}

s=requests.Session()
r=s.get(geturl,params=getpay, headers=getheaders)



headers={
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.barchart.com/futures/quotes/SBH23',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'x-xsrf-token': unquote(unquote(s.cookies.get_dict()['XSRF-TOKEN']))

}
#'root': 'SB - sugar, CL Crude Oil Cash, GC Gold Cash, NG Natural Gas Cash
payload={
    #'fields': 'symbol,contractSymbol,lastPrice,priceChange,openPrice,highPrice,lowPrice,previousPrice,volume,openInterest,tradeTime,symbolCode,symbolType,hasOptions',
    'fields': 'symbol,lastPrice,priceChange,highPrice,lowPrice,volume,tradeTime',
    'list': 'futures.contractInRoot',
    #'root': 'SB', #SB is the sugar root
    #'root': 'CL', #CL is the Crude Oil WTI Cash root
    #'root': 'GC', #GC is the Gold Cash root
    #'root': 'NG', #NG is the Natural Gas Cash root
    'root': 'SB', #Sugar
    'meta': 'field.shortName,field.type,field.description',
    'hasOptions': 'true',
    'raw': '0' #1 añade un raw extra

}

r=s.get(apiurl,params=payload,headers=headers)
j=r.json()
print(j)