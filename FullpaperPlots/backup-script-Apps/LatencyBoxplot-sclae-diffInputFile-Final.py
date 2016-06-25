def orderinglogicForThreadFromEXPID(i):
    # id1=int(s1.split("/")[-1].split("-")[6])
    # ratelist1=s1.split("/")[-1].split("-")[7].split(".")
    # ratelist1.pop()
    # rate1=float(".".join(ratelist1))
    #
    # return id1-rate1
    expID = i.split("/")[-1].split("-")[-2]
    print expID
    return int(expID)

def orderinglogic(i):

    rate = i.split("/")[-1].split("-")[-1].split(".")[0] + "." + i.split("/")[-1].split("-")[-1].split(".")[1]
    return (10 / float(rate))

import pandas as pd
import numpy as np
import matplotlib
import os
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
import sys
import os.path

# outDirForBoxplot="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/float/log1/plot/"
# expID="*-0.29*"
# print expID
# cmd="ls -1 "+"/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/float/log1/dat/*-"+expID+"-*.dat"



# outDirForBoxplot="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/parsing/logwithstringxml/plot/"
# expID="*-0.27.*"
# print expID
# cmd="ls -1 "+"/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/parsing/logwithstringxml/dat/*"+expID+"*.dat"


outDirForBoxplot="/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/plot/"
expID="18_with_Linear_scaling"
# expID="*-0.11.*"
print expID
cmd="ls -1 "+"/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/dat/L-*"+expID+"*.dat"


# out_dir_list=[]
# for out_dir in os.popen(cmd).read().split("\n"):
#    if out_dir:
#        out_dir_list.append(out_dir)
#
# print out_dir_list
#
# out_dir_list=sorted(out_dir_list,key=orderinglogicForThreadFromEXPID)
# print out_dir_list


baseClearFilepath="/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/dat/"
out_dir_list=[]
clear_out_dir_list = [


## STATS apps
    "L-AVG-sink-IoTStatsTopologySYS-SYS-1826000-0.001.log.dat",
    # "L-AVG-sink-IoTStatsTopologySYS-SYS-1816000-0.001.log.dat",
    # "L-AVG-sink-IoTStatsTopologyTAXI-TAXI-1852000-0.001.log.dat",
    "L-AVG-sink-IoTStatsTopologyTAXI-TAXI-1872000-0.001.log.dat",


##############################################################################



    # "L-AVG-sink-IoTStatsTopologySYS-SYS-1716000-0.001.log.dat",
    # "L-AVG-sink-IoTStatsTopologyTAXI-TAXI-1752000-0.001.log.dat"


    # "L-AVG-sink-IoTStatsTopology-SYS-12561600-0.01.log.dat"
      # "L-AVG-sink-BlockWindowAverage-PLUG-6211211000-1.0.log.dat",
      # "L-AVG-sink-DistinctApproxCount-PLUG-9216311000-1.0.log.dat",
      # "L-AVG-sink-BloomFilterCheck-PLUG-9216311000-1.0.log.dat",
      # "L-AVG-sink-IdentityTopologyBlob-PLUG-271111-2.5.log.dat",
      # "L-AVG-sink-AzureBlobUpload-PLUG-71111002-1.0.log.dat",
      # "L-AVG-sink-IdentityTopologyTable-PLUG-6011103-1.0.log.dat",
      # "L-AVG-sink-MQTTPublish-PLUG-8111211000-1.0.log.dat",
      # "L-AVG-sink-IdentityTopologyFloat-PLUG-91111105-1.0.log.dat",
      # "L-AVG-sink-IdentityTopologyParse-PLUG-85111310-1.0.log.dat",
      # "L-AVG-sink-DecisionTreeClassify-PLUG-8111511000-1.0.log.dat",
      # "L-AVG-sink-LinearRegressionPredictor-PLUG-8211511000-1.0.log.dat",
      # "L-AVG-sink-SimpleLinearRegressionPredictor-PLUG-8313411000-1.0.log.dat",
      # "L-AVG-sink-KalmanFilter-PLUG-9416811000-1.0.log.dat",
      # "L-AVG-sink-SecondOrderMoment-PLUG-8110311000-1.0.log.dat"
]


for i in clear_out_dir_list:
    out_dir_list.append(baseClearFilepath+i)

print out_dir_list



# exit()
## Full box plot

filename1=outDirForBoxplot + "/Latency-BoxplotDetails-"+expID+".txt"
if os.path.exists(filename1 ):
    print "yes present"
    os.remove(filename1)

p=[]

for i in out_dir_list:
    dSpout = pd.read_csv(i, engine='python', header=None, names=['msgid', 'ts1', 'ts2', 'latency'])
    # print dSpout['ts1']-dSpout['ts1'][0]
    rate = i.split("/")[-1].split("-")[-1].split(".")[0] + "." + i.split("/")[-1].split("-")[-1].split(".")[1]
    print rate, 10 / float(rate)
    print dSpout.head(10)

    dSpout = dSpout[dSpout['latency'] > 0]

    # dSpout = dSpout[dSpout['latency'] < 50000]

    p.append(dSpout['latency'])
    print dSpout.describe()

    with open(filename1, "a") as myfile:
        myfile.write(i+"\n\n")
        myfile.write("\t\t" + str(dSpout['latency'].describe()) + "\n")
    # exit()


#
fig = plt.figure(1, figsize=(9, 6))
# Create an axes instance
ax = fig.add_subplot(111)
# Create the boxplot
bp = ax.boxplot(p,whis=1000000000,showfliers=False)
# ax.set_ylabel('Latency (in millisec.)', color='b')



for box in bp['boxes']:
    # change outline color
    box.set( color='k', linewidth=2)
for cap in bp['whiskers']:
    cap.set(color='b', linewidth=2)
for median in bp['medians']:
    median.set(color='r', linewidth=2)


def slice(i):

    rate = i.split("/")[-1].split("-")[-1].split(".")[0] + "." + i.split("/")[-1].split("-")[-1].split(".")[1]
    newrate=i.split("/")[-1].split("-")[-2][-3:]
    # print rate, 100 / float(rate)
    # return i.split("/")[-1].split("-")[-2] + "-" + i.split("/")[-1].split("-")[-1] + "(" + str(int(100 / float(rate))) + ")"
    # return i.split("/")[-1].split("-")[-2] + "-" + i.split("/")[-1].split("-")[-1] + "(" + newrate + ")"
    # return i.split("/")[-1].split("-")[-4]
    return i.split("/")[-1].split("-")[-4]
    # return i

print map(slice,out_dir_list)
print len(out_dir_list)
# ax.set_yticklabels(1000,2000,3000,4000,5000,7000,1000,15000,20000)
# ax.set_xticklabels(map(slice,out_dir_list), rotation='90')


max_lat_val=201
ax.set_ylim([0,max_lat_val])
plt.yticks(np.arange(0, max_lat_val, 50))

# ax.yaxis.grid(which='minor', alpha=0.5)
# ax.yaxis.grid(which='major', alpha=0.5)

ax.set_xticklabels(map(slice,out_dir_list), rotation='45',ha='right')

# plt.yticks(np.arange(0, 15000, 1000))
#
# ax.yaxis.grid(which='minor', alpha=0.5)
# ax.yaxis.grid(which='major', alpha=0.5)

# fig = matplotlib.pyplot.gcf()
# fig.set_size_inches(15.5, 6.5)

#setting horizontal and vertical lines for grid
for i in np.arange(0.1,max_lat_val,100):
    print i
    plt.hlines(i,0,25,colors='0.80',linestyles='-')
for i in np.arange(0.1,600,25):
    print i
    plt.hlines(i,0,25,colors='0.50',linestyles='-')

# ax.xaxis.grid(which='minor', alpha=0.5)
# ax.yaxis.grid(which='major', alpha=0.5)

plt.ylabel('Latency (in milli.sec.) APPs-1000x', fontsize=15)
plt.xlabel('Micro-Benchmarks', fontsize=15)


# Save the figure
fig.savefig(outDirForBoxplot+"FullBoxPlot-Latency-"+ expID +".png", bbox_inches='tight')