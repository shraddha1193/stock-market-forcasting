
#!/user/bin/python

import os
os.system('pip install pandas')
os.system('pip install requests')
from io import StringIO
import requests
from datetime import datetime
import datetime
import pandas as pd 

dates=[]
start = datetime.datetime.strptime("2011-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2021-09-27", "%Y-%m-%d")
date_array = \
    (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))
for date_object in date_array:
    dates.append(date_object.strftime("%d-%b-%Y"))


li=[]

for i in dates:
    
    cols={'nav_date':[],'schame_code':[],'schame_name':[],'rta_schame_code':[],'div_reinvestflog':[],'isin':[],'nav_value':[],'rta_code':[]}
    url = "https://bsestarmf.in/RptNavMaster.aspx"
    payload = "_VIEWSTATE=dxbutRoM6sY7gFJslLxTaszwmGeNr5Xmn5hypVeVb57POGbzcVYGJsDnRMobZE%2FWgImAw2NMOHOiqOsy3PjdLKTHTDMTzh5G4WS7Ie2nnqwDQ89FVMYgmVjHG26gZc%2FYT55sqg%3D%3D&VIEWSTATEGENERATOR=8EE3ED57&VIEWSTATEENCRYPTED=&_EVENTVALIDATION=XmQhb5jn7vNBN08NWuZcqkQaODZf%2FFWNGWcn080SGW7DiB3OpSqkmHD6lLyTGeGv0w9GhT%2BQMRX6gDYAhKMzlckR6POwa%2BpoJeRQpt7FRw8LBwjg%2BaWlCI1lgcDQaJswYFP%2B1q76%2BSJlXIJJGjsu3O3O01O4pZJX11wSLxm5U5ihZSRb&txtToDate="+(i)+"&btnText=Export+to+Text"
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    data=response.content.decode('utf8')
    data_n=StringIO(data)
    df=pd.read_csv(data_n,sep='|',header=None,names=list(cols.keys()),index_col=False)
#     df.to_csv(f"{i}.csv",index=None)
    li.append(df)
    frame = pd.concat(li, axis=0, ignore_index=True)
    
frame.to_csv("HISTORICAL_NAV.csv",index=None)