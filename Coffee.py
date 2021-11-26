import plotly.express as px
import csv
import numpy as np

def getDataSource(dataPath):
    hrsOfSleep = []
    coffeeTaken = []
    with open(dataPath) as csv_file:
        csvReader = csv.DictReader(csv_file)
        for row in csvReader:
            hrsOfSleep.append(float(row["sleepingHours"]))
            coffeeTaken.append(float(row["Coffee-ml"]))
    return{"x":hrsOfSleep, "y":coffeeTaken}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("correlation between the amount of coffee taken in ml and hours of sleep is: ",correlation[0, 1])

def setup():
    dataPath = './Data2.csv'
    dataSource = getDataSource(dataPath)
    findCorrelation()


setup()