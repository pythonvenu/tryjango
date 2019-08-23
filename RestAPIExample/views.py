from django.shortcuts import render

# Create your views here.

def CryptoHome(request):
    import requests
    import json
    news = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(news.content)
    #price_req = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC&tsyms=USD,EUR,INR")
    #api =  json.loads(price_req.content)
    return render(request, 'RestAPI/cryptohome.html', {"api":api})

def price(request):
    import requests
    import json
    if request.method=="POST":
        cur = request.POST['CurrencyName']
        price_req = requests.get("https://min-api.cryptocompare.com/data/price?fsym=" + cur +"&tsyms=USD,JPY,EUR,INR")
        print('price_req', price_req)
        cry_json = json.loads(price_req.content)
        crypto_data()
        print('cry_json', cry_json)
        #multi_req = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,EUR")
        #multi_json = json.loads(multi_req.content)
        return render(request, 'RestAPI/price.html', {"price": cry_json,
                                                      #"mprice": multi_json
                                                      })
    else:
        return render(request, 'RestAPI/price.html',{})

