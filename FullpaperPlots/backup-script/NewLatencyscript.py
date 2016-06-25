
import pandas as pd
import numpy as np
import matplotlib
import os
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
import sys
import os.path
# outDir="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/VMpushTest/8with300-36000/out"
# cmd="ls -1 "+"/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/VMpushTest/8with300-36000/spout*  #*-1121-*"

# outDir="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/parsing/logwithstringxml/dat"
# cmd="ls -1 "+"/Users/anshushukla/PycharmProjects/DataAnlytics1/schedulxer/parsing/logwithstringxml/log/spout*"

# outDir="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/floatpi/log1/dat"
# cmd="ls -1 "+"/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/floatpi/log1/log/spout*"

outDir="/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/dat"
cmd="ls -1 "+"/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/log/spout*-8113411000*"


out_dir_list=[]

for out_dir in os.popen(cmd).read().split("\n"):
   if out_dir:
       out_dir_list.append(out_dir)
print out_dir_list

filename1=outDir+"/ExecLatency.txt"
if os.path.exists(filename1 ):
    print "yes present"
    os.remove(filename1)
filename2=outDir+"/MeanLatency.txt"
if os.path.exists(filename2 ):
    os.remove(filename2)


for spoutFileName in out_dir_list:
    # sinkFileName=("/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/121to126/sink-IdentityTopology-PLUG-124-0.33.log")
    # spoutFileName=("/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/121to126/spout-IdentityTopology-PLUG-124-0.33.log")

    fileIdentifier = '-'.join(spoutFileName.split('/')[-1].split('-')[1:])
    sinkFileName = spoutFileName[0:spoutFileName.rfind('/')+1] + 'sink-' + fileIdentifier
    print sinkFileName

    dSpout = pd.read_csv(spoutFileName, engine='python', header=None, names = ['hostname', 'thread', 'component', 'timestamp', 'key','value']);
    dSpout['timestamp'] = dSpout['timestamp'].astype(long)

    # dSink = pd.read_csv(sinkFileName, engine='python', header=None, names = ['hostname', 'thread', 'component', 'timestamp','value','execlatency']);
    dSink = pd.read_csv(sinkFileName, engine='python', header=None,
                        names=['hostname', 'thread', 'component', 'timestamp', 'value']);
    dSink['timestamp'] = dSink['timestamp'].astype(long)

    dRes = pd.merge(dSpout, dSink, on='value')
    dRes['latency'] = dRes.timestamp_y - dRes.timestamp_x
    # print dRes.head(10)

    dgrouped = dRes.groupby('value')

    meanDF = dgrouped.mean()
    print meanDF['latency'].mean()



    fileIdentifier=sinkFileName.split("/")[-1]
    meanDF.to_csv(outDir + '/L-AVG-' + fileIdentifier + '.dat', header=False, columns=['timestamp_x', 'timestamp_y', 'latency'])


    Meanlatency=meanDF['latency'].mean()
    with open(outDir+"/MeanLatency.txt", "a") as myfile:
        myfile.write(fileIdentifier+"\t\t"+str(Meanlatency)+"\n")
    #
    #
    # ##Code for  Execute Latency
    # execLatency=dSink['execlatency'].mean()
    # print "Mean ExecLatency is - ",execLatency
    # with open(outDir+"/ExecLatency.txt", "a") as myfile:
    #     myfile.write(fileIdentifier+"\t\t"+str(execLatency)+"\n")
    #     # myfile.write(str(execLatency)+"\n")