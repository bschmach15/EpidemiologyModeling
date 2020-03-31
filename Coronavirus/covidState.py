from Coronavirus import getCovidData
import matplotlib.pyplot as plot
import requests
import json
import pandas as pd
import numpy as np
from types import SimpleNamespace


class State:


    def __init__(self, state):
        self.state = state
        self.data = getCovidData.getHistoricalStateData(state)
        stateInfo = requests.get('https://covidtracking.com/api/states/info?state={0}'.format(state))
        stateInfo = json.loads(stateInfo.content)
        self.name = stateInfo['name']


    def update(self):
        self.data = getCovidData.getHistoricalStateData(self.state)

    def plotCases(self):
        plot.plot(self.data.date, self.data.positive)
        plot.xlabel('Date')
        plot.ylabel('Positive Cases')
        plot.title(self.name)
        plot.show()

    def getData(self):
        data = SimpleNamespace()
        data.state = self.name
        data.dates = self.data.date
        data.positive = self.data.positive
        return data


class US:


    def __init__(self):
        self.state = 'United States'
        self.data = getCovidData.getUsData()

    def update(self):
        self.data = getCovidData.getUsData()

    def plotCases(self):
        plot.plot(self.data.date, self.data.positive)
        plot.xlabel('Date')
        plot.ylabel('Positive Cases')
        plot.title('United States')
        plot.show()


if __name__ == '__main__':
    CO = State("CO")
    MD = State("MD")
    CA = State("CA")
    NY = State("NY")

    COdata = CO.getData()
    MDdata = MD.getData()
    CAdata = CA.getData()
    NYdata = NY.getData()

    plot.plot(COdata.dates, COdata.positive, label=COdata.state)
    plot.plot(MDdata.dates, MDdata.positive, label=MDdata.state)
    plot.plot(CAdata.dates, CAdata.positive, label=CAdata.state)
    plot.legend()
    plot.show()

    UnitedStates = US()
    UnitedStates.plotCases()