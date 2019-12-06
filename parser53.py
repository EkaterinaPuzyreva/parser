import requests
import json


numbers = set()
response = requests.get("https://mu-kgt.ru/informing/wap/marsh/?m=53&action=getMarshData")
dict = response.json()

print(dict['directions']['A']['first'], '->', dict['directions']['A']['last'])

dictstop = dict['ts_line']['A']
for key in dictstop:
   
    if key['obj']== 'stop':
    
        print(key['st_arrive'], ' ', key['st_title'])
       
    else: 
        print(key['ts_model'])
