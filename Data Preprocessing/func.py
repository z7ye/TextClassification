import pandas as pd
import os
import sys
import gzip

### data path


### function to extract and parse the data
def parse(path):
    g = gzip.open(path, 'rb')
    for l in g:
        yield eval(l)

def getDF(path):
    i = 0
    df = {}
    for d in parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient='index')



def load_data(data = 'musical'):
    path0 = 'Data/'
    if data == 'musical':
        filename = 'reviews_Musical_Instruments_5.json.gz'
    else:
        filename = 'reviews_Amazon_Instant_Video_5.json.gz'
    path = path0 + filename
    df = getDF(path)
    return df



