import csv
import numpy as np

def getdata(data_path):
    size=[]
    time=[]
    
    with open (data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for i in csv_reader:
            size.append(float(i["Days Present"]))
            time.append(float(i["Marks In Percentage"]))

    return {"x":size,"y":time}

def findCorr(dataSource):
    corr=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation is :",corr[0,1])

def setup():
    data_path="data1.csv"
    DataSource=getdata(data_path)
    findCorr(DataSource)

setup()

