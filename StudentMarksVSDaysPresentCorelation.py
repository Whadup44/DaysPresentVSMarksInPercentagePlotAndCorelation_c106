import plotly.express as py
import csv
import numpy as np

def getDataSource(dataPath):
    Marks = []
    DaysPresent = []
    with open(dataPath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks.append(float(row["Marks In Percentage"]))
            DaysPresent.append(float(row["Days Present"]))
    return{"x": Marks, "y": DaysPresent}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("The Corelation between the Marks a student scores (percentage) and their Attendance is: " + str(corelation[0, 1]))

def setup():
    dataPath = './Student Marks vs Days Present.csv'
    dataSource = getDataSource(dataPath)
    findCorelation(dataSource)

setup()