import numpy as np
import pandas as pd
import requests
from datetime import  datetime as dt
import json

# Columns are 'state', 'positive', 'positiveScore', 'negativeScore',
#             'negativeRegularScore', 'commercialScore', 'grade', 'score', 'negative',
#             'pending', 'hospitalized', 'death', 'total', 'lastUpdateEt',
#             'checkTimeEt', 'totalTestResults', 'fips', 'dateModified',
#             'dateChecked', 'notes', 'hash'




def getMostRecentStateData(state):
    apiString = 'https://covidtracking.com/api/states?state={0}'.format(state)
    coronaStateData = requests.get(apiString)
    coronaStateData = coronaStateData.json()
    coronaStateData = pd.json_normalize(coronaStateData)
    return coronaStateData

def getHistoricalStateData(state):
    apiString = 'https://covidtracking.com/api/states/daily?state={0}'.format(state)
    coronaStateData = requests.get(apiString)
    coronaStateData = coronaStateData.json()
    coronaStateData = pd.json_normalize(coronaStateData)
    return coronaStateData


def getUsData():
    apiString = 'https://covidtracking.com/api/us/daily'
    coronaStateData = requests.get(apiString)
    coronaStateData = coronaStateData.json()
    coronaStateData = pd.json_normalize(coronaStateData)
    return coronaStateData

if __name__ == '__main__':
    mddf = getHistoricalStateData('MD')
    print(mddf[['state','date','positive','negative']])