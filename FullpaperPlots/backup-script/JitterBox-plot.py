# def orderinglogic(s1):
#     id1=int(s1.split("/")[-1].split("-")[2])
#     ratelist1=s1.split("/")[-1].split("-")[3].split(".")
#     ratelist1.pop()
#     rate1=float(".".join(ratelist1))
#
#     return id1-rate1

import pandas as pd
import numpy as np
import matplotlib
import os
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
import sys
import os
import os.path

import matplotlib as mpl

expID="*"

outDirForBoxplot="/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/plot/"
listclearedfiles="ls -1 "+"/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/cpu/clear-cpu*"+expID+".txt"
listbeforegrep="ls -1 "+"/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/cpu/cpu*"+expID+".txt"


baseClearFilepath="/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/dat/"

# commented for final
out_dir_list=[]
# for out_dir in os.popen(listclearedfiles).read().split("\n"):
#    if out_dir:
#        out_dir_list.append(out_dir)

clear_out_dir_list=[

"T-spout-IdentityTopologyParse-PLUG-85111310-1.0.dat",
"T-spout-BloomFilterCheck-PLUG-9216311000-1.0.dat",
"T-spout-BlockWindowAverage-PLUG-6211211000-1.0.dat",
"T-spout-DistinctApproxCount-PLUG-9216311000-1.0.dat",
"T-spout-KalmanFilter-PLUG-9416811000-1.0.dat",
"T-spout-SecondOrderMoment-PLUG-8110311000-1.0.dat",
"T-spout-DecisionTreeClassify-PLUG-8111511000-1.0.dat",
"T-spout-LinearRegressionPredictor-PLUG-8211511000-1.0.dat",
"T-spout-SimpleLinearRegressionPredictor-PLUG-8313411000-1.0.dat",
"T-spout-IdentityTopologyBlob-PLUG-12111004-1.0.dat",     # "T-spout-IdentityTopologyBlob-PLUG-271111-2.5.dat",
"T-spout-AzureBlobUpload-PLUG-71111002-1.0.dat",
"T-spout-IdentityTopologyTable-PLUG-12211003-1.0.dat",      # "T-spout-IdentityTopologyTable-PLUG-271111-3.33.dat",
"T-spout-MQTTPublish-PLUG-8111211000-1.0.dat",


]


for i in clear_out_dir_list:
    out_dir_list.append(baseClearFilepath+i)



## using x as method declared above
# out_dir_list=sorted(out_dir_list,key=orderinglogic)

print out_dir_list


filename1=outDirForBoxplot + "/jitter-BoxplotDetails-"+expID+".txt"
if os.path.exists(filename1 ):
    print "yes present"
    os.remove(filename1)

index = 0
dFullPlot = pd.DataFrame(columns = [0])

pSpout=[]
pSink=[]

res_total=[]

for i in out_dir_list:
    iSink=i.replace("spout","sink")

    print i,iSink

    dSpoutThr = pd.read_csv(i, engine='python', header=None,names=['ts', 'rate']);
    dSinkThr = pd.read_csv(iSink, engine='python', header=None,names=['ts', 'rate']);

    print dSpoutThr.describe()
    print dSinkThr.describe()


    pSpout=dSpoutThr['rate'].tolist()
    pSink = dSinkThr['rate'].tolist()

    print len(pSpout),len(pSink)

    avgI = np.mean(dSpoutThr['rate'])
    print "avgI-",avgI

    res = []
    sel=1.0
    for m in xrange(min(len(pSpout),len(pSink))):
        print ((pSink[m]-pSpout[m]*1.0)/(avgI*1.0))
        # print i.split("/")[-1].split("-")[2]
        if(i.split("/")[-1].split("-")[2]=="BlockWindowAverage"):
            sel=0.1
            print "yes"

        print sel
        res.append(((pSink[m]-pSpout[m]*sel)/(avgI*sel)))

    res_total.append(res)


#
# fig = plt.figure(1, figsize=(9, 6))

fig = plt.figure(1, figsize=(12, 8))
# Create an axes instance
ax = fig.add_subplot(111)
# Create the boxplot
bp = ax.boxplot(res_total,whis=1000000000,showfliers=False)
# bp = ax.boxplot(res_total)

print "Uncomment to get final plot"


# ax.set_ylabel('Latency (in millisec.)', color='b')

def slice(i):

    rate = i.split("/")[-1].split("-")[-1].split(".")[0] + "." + i.split("/")[-1].split("-")[-1].split(".")[1]
    newrate=i.split("/")[-1].split("-")[-2][-3:]
    # print rate, 100 / float(rate)
    # return i.split("/")[-1].split("-")[-2] + "-" + i.split("/")[-1].split("-")[-1] + "(" + str(int(100 / float(rate))) + ")"
    # return i.split("/")[-1].split("-")[-2] + "-" + i.split("/")[-1].split("-")[-1] + "(" + newrate + ")"

    if(i.split("/")[-1].split("-")[-4]=="BlockWindowAverage"):
        return "AVG"
    if(i.split("/")[-1].split("-")[-4]=="DistinctApproxCount"):
        return "DAC"
    if(i.split("/")[-1].split("-")[-4]=="BloomFilterCheck"):
        return "BLF"
    if(i.split("/")[-1].split("-")[-4]=="IdentityTopologyBlob"):
        return "ABD"
    if(i.split("/")[-1].split("-")[-4]=="AzureBlobUpload"):
        return "ABU"
    if(i.split("/")[-1].split("-")[-4]=="IdentityTopologyTable"):
        return "ATQ"
    if(i.split("/")[-1].split("-")[-4]=="MQTTPublish"):
        return "MQP"
    if(i.split("/")[-1].split("-")[-4]=="IdentityTopologyFloat"):
        return i.split("/")[-1].split("-")[-4]
    if(i.split("/")[-1].split("-")[-4]=="IdentityTopologyParse"):
        return "XML"
    if(i.split("/")[-1].split("-")[-4]=="DecisionTreeClassify"):
        return "DTC"
    if(i.split("/")[-1].split("-")[-4]=="LinearRegressionPredictor"):
        return "MLR"
    if(i.split("/")[-1].split("-")[-4]=="SimpleLinearRegressionPredictor"):
        return "SLR"
    if(i.split("/")[-1].split("-")[-4]=="KalmanFilter"):
        return "KAL"
    if(i.split("/")[-1].split("-")[-4]=="SecondOrderMoment"):
        return "SOM"
    else:
        return i.split("/")[-1].split("-")[-4]



print map(slice, out_dir_list)

# max_lat_val=8000
# ax.set_ylim([0,max_lat_val])
# plt.yticks(np.arange(0, max_lat_val, 1000))


ax.set_xticklabels(map(slice,out_dir_list))
ax.set_ylim([-6,6])


#setting horizontal and vertical lines for grid
# for i in np.arange(-8,6,1):
#     print i
#     plt.hlines(i,0,25,colors='0.80',linestyles='-')

# for i in np.arange(20,120,20):
#     print i
#     plt.hlines(i,0,25,colors='0.50',linestyles='-')

# fig.suptitle('Jitter box-plot', fontsize=15)
# plt.ylabel('Relative throughput', fontsize=15)
# plt.xlabel('Micro-Benchmarks', fontsize=15)

#setting horizontal and vertical lines for grid
for i in np.arange(-6,6,0.5):
    print i
    plt.hlines(i,0,25,colors='0.70')
for i in np.arange(-6, 6, 2):
    print i
    plt.hlines(i,0,25,colors='0.50')

plt.tick_params(axis='x', which='major', labelsize=22)
plt.tick_params(axis='y', which='major', labelsize=26)
plt.ylabel("Relative throughput", fontsize=26)


for box in bp['boxes']:
    # change outline color
    box.set( color='k', linewidth=3)
for cap in bp['whiskers']:
    cap.set(color='b', linewidth=4)
for median in bp['medians']:
    median.set(color='r', linewidth=4)

# # for special ticks at top
# new_tick_locations = np.array([8.5, 13])
# ax2 = ax.twiny()
# ax2.set_xticks(new_tick_locations)
# ax2.set_xticklabels([4513 , 1],rotation=45)



# Save the figure
# fig.savefig(outDirForBoxplot+'TEST-FullBoxPlot-Jitter-FULL-Rename-ord'+expID+'.pdf', bbox_inches='tight')
fig.savefig("/Users/anshushukla/Downloads/Incomplete/pubs/vldbw-tpctc-2016/latex/plots/microBenchmark/FullBoxPlotJitter.pdf", bbox_inches='tight')




exit()

