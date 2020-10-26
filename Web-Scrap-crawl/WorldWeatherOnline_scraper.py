#from platform import python_version
#print(python_version())

import urllib
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import demjson
import pandas as pd
from functools import reduce
#pip install demjson
#test website: https://www.worldweatheronline.com/jakarta-weather-averages/jakarta-raya/id.aspx

print('Enter the website: ')
web = input()
try:
    html = urllib.request.urlopen(web)
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(), "html5lib")
    # print(res)
    # get title
    print(res.title.getText())
    title = res.title.getText()
    title = title.strip('\n')
    title = title.replace('|', '_')
    filename = title+'.csv'
    # print(res.prettify())
    scripts = res.findAll("script")
    data_regex = re.compile("{name:.+?data:.+?}")
    dfs =[]
    for script in scripts:
        data_all = data_regex.findall(script.getText())
        if data_all:
            #print(data_all)
            for data in data_all:
#                 print(type(data))
#                 print(data)
                data_parsed = demjson.decode(data) # class: dict
#                 print(type(data_parsed))
#                 print(data_parsed['name'])
#                 print(data_parsed['data'])
#                 print(type(data_parsed['data']))
                df = pd.DataFrame(columns = ['YearMonth', data_parsed['name']], data = data_parsed['data'])
                dfs.append(df)
                #print(df)

#     df_merge = pd.DataFrame()
#     for df in dfs:
#         if df_merge.empty:
#             #print("empty")
#             df_merge = df
#             continue
#         else:
#             #print("not empty")
#             df_merge = pd.merge(df_merge, df, on = 'YearMonth')
#     print(df_merge.head())

    df_final = reduce(lambda left,right: pd.merge(left,right,on='YearMonth'), dfs)
    print(df_final.head())
    df_final.to_csv(filename, header = True)





