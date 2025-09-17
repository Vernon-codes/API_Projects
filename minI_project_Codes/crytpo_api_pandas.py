import pandas as pd
import requests
url='https://api.coingecko.com/api/v3/simple/price'
params={'ids':'bitcoin,ethereum,ripple,litecoin,cardano','vs_currencies':'usd'}
r=requests.get(url,params=params)
data=r.json()
df=pd.DataFrame(data)
print(df.head())
df.to_csv('crypto_prices.csv',index=False)