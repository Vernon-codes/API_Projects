import pandas as pd
import requests
r=requests.get('https://official-joke-api.appspot.com/random_ten')
print(r.status_code)
data=r.json()
#extracting relevant information
data_list=[]
for joke in data:
    data_list.append({'ID':joke['id'],'Type':joke['type'],'Setup':joke['setup'],'Punchline':joke['punchline']})
df=pd.DataFrame(data_list)
print(df.head())
df.to_csv('jokes.csv',index=False)
