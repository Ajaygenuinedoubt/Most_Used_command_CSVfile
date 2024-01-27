# -*- coding: utf-8 -*-
"""Most-use-command-in-CSVfile.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nUBrqX1S2MR5PFkTECjz22TZajoNEsNx

**Import Pandas**
"""

import pandas as pd

"""**2. Opening a local csv file**"""

df = pd.read_csv('aug_train.csv')
df

"""**Opening a csv file from an URL**"""

import requests
from io import StringIO

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=headers)
data = StringIO(req.text)

pd.read_csv(data)

"""**Sep Parameter**"""

pd.read_csv('movie_titles_metadata.tsv',sep='\t',names=['sno','name','release_year','rating','votes','genres'])

"""**5. Index_col parameter**"""

pd.read_csv('aug_train.csv',index_col='enrollee_id')

"""**6. Header parameter**"""

pd.read_csv('test.csv',header=1)

"""**7. use_cols parameter**"""

pd.read_csv('aug_train.csv',usecols=['enrollee_id','gender','education_level'])

"""**8. Squeeze parameters**"""

pd.read_csv('aug_train.csv',usecols=['gender'],squeeze=True)

"""**9. Skiprows/nrows Parameter**"""

pd.read_csv('aug_train.csv',nrows=100)

"""**10. Encoding parameter**"""

pd.read_csv('test.csv',encoding='latin-1')

"""**11. Skip bad lines**"""

pd.read_csv('test.csv', sep=';', encoding="latin-1",error_bad_lines=False)

"""**12. dtypes parameter**"""

pd.read_csv('aug_train.csv',dtype={'target':int}).info()

"""**
13. Handling Dates**
"""

pd.read_csv('IPL Matches 2008-2020.csv',parse_dates=['date']).info()

"""**14. Convertors**"""

# rename function
def rename(name):
    if name == "Royal Challengers Bangalore":
        return "RCB"
    else:
        return name
rename("Royal Challengers Bangalore")

pd.read_csv('IPL Matches 2008-2020.csv',converters={'team1':rename})

"""**15. na_values parameter**"""

pd.read_csv('aug_train.csv',na_values=['Male',])

"""**16. Loading a huge dataset in chunks**"""

dfs = pd.read_csv('aug_train.csv',chunksize=5000)

for chunks in dfs:
    print(chunk.size)

