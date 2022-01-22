import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics 

df = pd.read_csv("medium_data.csv") 

data = df["reading_time"].tolist()

pmean = statistics.mean(data)
print("the population mean is ", pmean)
psd = statistics.stdev(data)
print("the population standarddeviation is ", psd)

def samplingmean() :
    smple = []
    for i in range(0,30) :
        rindex = random.randint(0,len(data)-1)
        value = data[rindex]
        smple.append(value)

    mean = statistics.mean(smple)
    return mean

def showfig(meanlist) :
    fig = ff.create_distplot([meanlist],["sample mean"],show_hist = False)
    fig.show()

def setup() :
    meanlist = [] 
    for i in range(0,100) :
        mean = samplingmean()
        meanlist.append(mean)
    showfig(meanlist)
    smean = statistics.mean(meanlist)
    print("the sampling mean is ", smean)
    ssd = statistics.stdev(meanlist)
    print("the smapling standarddeviation is ", ssd)

setup()