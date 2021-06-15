import csv 
import numpy as np
def getDataSource(data_path):
    cup_of_coffee=[]
    Average_time_spent=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            cup_of_coffee.append(float(row["Cup of Coffee"]))
            Average_time_spent.append(float(row["/Average time spent in sleep(hours)"]))

    return{"x":cup_of_coffee,"y":Average_time_spent}


def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("cups of coffee vs hours of sleep:-\n--->",correlation[0,1])

def setup():
    data_path="1.csv"

    datasource=getDataSource(data_path)
    findCorrelation(datasource)

setup()