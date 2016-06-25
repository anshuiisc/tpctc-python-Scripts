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
print mpl.__version__

# exit()

expID="18_with_Linear_scaling"

outDirForBoxplot="/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/plot/"
listclearedfiles="ls -1 "+"/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/cpu/clear-cpu*"+expID+".txt"
listbeforegrep="ls -1 "+"/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/cpu/cpu*"+expID+".txt"

#
# # use for removing 100% before commenting below line ...
# # sed   -i .bak  '/100/d'  clear-cpuFloat-251*
#
# # sed_command="sed   -i .bak  's/100/ 100/g'  "
# sed_command="sed   -i .bak  's/100/ 100/g'  "
# print sed_command

# commented after first run

# for out_dir in os.popen(listbeforegrep).read().split("\n"):
#     if(len(out_dir)!=0):
#         # print out_dir.split("/")[-1]
#         temp=out_dir.split("/")
#         # print temp
#         temp[-1]="clear-"+temp[-1]
#         newout_dir="/".join(temp)
#
#         cmdforGrep="grep Cpu "+out_dir +"> " +newout_dir
#         print cmdforGrep
#         cmdforSED=sed_command+"  "+newout_dir
#         print cmdforSED
#         os.popen(cmdforGrep)
#         os.popen(cmdforSED)

baseClearFilepath="/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/dat/"

# commented for final
out_dir_list=[]
# for out_dir in os.popen(listclearedfiles).read().split("\n"):
#    if out_dir:
#        out_dir_list.append(out_dir)

clear_out_dir_list=[


## stats app

# "T-spout-IoTStatsTopologySYS-SYS-1826000-0.001.dat",
"T-spout-IoTStatsTopologySYS-SYS-1816000-0.001.dat", # =-----------
# "T-spout-IoTStatsTopologyTAXI-TAXI-1852000-0.001.dat",
"T-spout-IoTStatsTopologyTAXI-TAXI-1872000-0.001.dat",#-----------------

##  predict app

"T-spout-IoTPredictionTopologySYS-SYS-2246000-0.001.dat",
"T-spout-IoTPredictionTopologyTAXI-TAXI-22116000-0.001.dat",


## microbenchmarks


    # "T-spout-IoTStatsTopologySYS-SYS-1716000-0.001.dat",
    # "T-spout-IoTStatsTopologyTAXI-TAXI-1752000-0.001.dat",



#     "T-spout-DistinctApproxCount-PLUG-9216311000-1.0.dat",
#     "T-spout-BloomFilterCheck-PLUG-9216311000-1.0.dat",
#     "T-spout-IdentityTopologyBlob-PLUG-12111004-1.0.dat",     # "T-spout-IdentityTopologyBlob-PLUG-271111-2.5.dat",
#     "T-spout-AzureBlobUpload-PLUG-71111002-1.0.dat",
# "T-spout-IdentityTopologyTable-PLUG-12211003-1.0.dat",      # "T-spout-IdentityTopologyTable-PLUG-271111-3.33.dat",
# "T-spout-MQTTPublish-PLUG-8111211000-1.0.dat",
# "T-spout-IdentityTopologyFloat-PLUG-91111105-1.0.dat",
# "T-spout-IdentityTopologyParse-PLUG-85111310-1.0.dat",
# "T-spout-DecisionTreeClassify-PLUG-8111511000-1.0.dat",
# "T-spout-LinearRegressionPredictor-PLUG-8211511000-1.0.dat",
# "T-spout-SimpleLinearRegressionPredictor-PLUG-8313411000-1.0.dat",
# "T-spout-KalmanFilter-PLUG-9416811000-1.0.dat",
# "T-spout-SecondOrderMoment-PLUG-8110311000-1.0.dat",
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
        # print i.split("/")[-1].split("-")[2]
        if(i.split("/")[-1].split("-")[2]=="BlockWindowAverage"):
            sel=0.1
            print "yes"
            print ((pSink[m] - pSpout[m] * 1.0) / (avgI * 1.0))
            res.append(((pSink[m]  - pSpout[m]* sel) / (avgI * sel)))

        if(i.split("/")[-1].split("-")[2]=="IoTStatsTopologySYS"):
            sel=(41033530/4523000)
            print "yes"
            print ((pSink[m] - pSpout[m] * sel) / (avgI * sel))
            res.append(((pSink[m]  - pSpout[m]* sel) / (avgI * sel)))

        if(i.split("/")[-1].split("-")[2]=="IoTStatsTopologyTAXI"):
            sel=( 12058760 /753300)
            print "yes"
            print ((pSink[m] - pSpout[m] * sel) / (avgI * sel))
            res.append(((pSink[m]  - pSpout[m]*sel) / (avgI * sel)))

        if(i.split("/")[-1].split("-")[2]=="IoTPredictionTopologySYS"):
            print "IoTPredictionTopologySYS-yes"
            sel = (4229400 / 73310) ## either flip the sel or flip the formulae
            print "yes"
            res.append(((pSink[m] * sel - pSpout[m]) / (avgI * sel)))

        if(i.split("/")[-1].split("-")[2]=="IoTPredictionTopologyTAXI"):
            print "IoTPredictionTopologyTAXI-yes"
            # sel = (  753300 /    13070 ) ## either flip the sel or flip the formulae
            sel=60
            print "yes"
            res.append(((pSink[m] * sel - pSpout[m]) / (avgI * sel)))
        print sel
    print i,res
        # res.append((abs(pSink[m]*sel-pSpout[m])/(avgI*sel)))

    res_total.append(res)


#
fig = plt.figure(1, figsize=(9, 6.1))
# Create an axes instance
ax = fig.add_subplot(111)
# Create the boxplot
bp = ax.boxplot(res_total,whis=1000000000,showfliers=False)
# bp = ax.boxplot(res_total)

print "Uncomment to get final plot"


# ax.set_ylabel('Latency (in millisec.)', color='b')



for box in bp['boxes']:
    # change outline color
    box.set( color='k', linewidth=3)
for cap in bp['whiskers']:
    cap.set(color='b', linewidth=4)
for median in bp['medians']:
    median.set(color='r', linewidth=4)


def slice(i):
    rate = i.split("/")[-1].split("-")[-1].split(".")[0] + "." + i.split("/")[-1].split("-")[-1].split(".")[1]
    newrate = i.split("/")[-1].split("-")[-2][-3:]
    # print rate, 100 / float(rate)
    # return i.split("/")[-1].split("-")[-2] + "-" + i.split("/")[-1].split("-")[-1] + "(" + str(int(100 / float(rate))) + ")"
    # return i.split("/")[-1].split("-")[-2] + "-" + i.split("/")[-1].split("-")[-1] + "(" + newrate + ")"
    # return i.split("/")[-1].split("-")[-4]
    return i.split("/")[-1]

    # if(i.split("/")[-1].split("-")[-4]=="IoTStatsTopologySYS"):
    #     print i.split("/")[-1]
    #     if (i.split("/")[-1].split("-")[-3] == "SYS"):
    #         return "STATS-CITY"
    #     else:
    #         return "'STATS-"+i.split("/")[-1].split("-")[-3]
    #
    # if (i.split("/")[-1].split("-")[-4] == "IoTPredictionTopologySYS"):
    #     print i.split("/")[-1]
    #     if (i.split("/")[-1].split("-")[-3] == "SYS"):
    #         return "-CITY"
    # else:
    #     return "PRED-" + i.split("/")[-1].split("-")[-3]


print map(slice, out_dir_list)
axisLabel=["STATS-CITY","STATS-TAXI","PRED-CITY","PRED-TAXI"]


# max_lat_val=8000
# ax.set_ylim([0,max_lat_val])
# plt.yticks(np.arange(0, max_lat_val, 1000))


# ax.set_xticklabels(map(slice,out_dir_list), rotation='45',ha='right')
ax.set_xticklabels(axisLabel, fontsize=22)

ax.set_ylim([-4,4])

#setting horizontal and vertical lines for grid
for i in np.arange(-4,4,0.25):
    print i
    plt.hlines(i,0,25,colors='0.80',linestyles='-')

for i in np.arange(-4, 4, 1):
    print i
    plt.hlines(i, 0, 25, colors='0.50', linestyles='-')

# for i in np.arange(20,120,20):
#     print i
#     plt.hlines(i,0,25,colors='0.50',linestyles='-')

# fig.suptitle('Jitter box-plot', fontsize=15)
# plt.ylabel('Relative throughput', fontsize=15)
# plt.xlabel('APP-Benchmarks', fontsize=15)

plt.tick_params(axis='x', which='major', labelsize=20)
plt.tick_params(axis='y', which='major', labelsize=22)
plt.ylabel('Relative throughput', fontsize=22)
# plt.xlabel('PRED (1000x)', fontsize=22)


# Save the figure
# fig.savefig(outDirForBoxplot+'FullBoxPlot-Jitter-APPS-PREDICT'+expID+'.pdf', bbox_inches='tight')
fig.savefig("/Users/anshushukla/Downloads/Incomplete/pubs/vldbw-tpctc-2016/latex/plots/apps/app-jitter-boxplot.pdf", bbox_inches='tight')

exit()

plt.close()
plt.gca()
fig = plt.figure(1, figsize=(9, 6))
ax = fig.add_subplot(111)


# Get a list of Line2D objects, representing a single line from the
# minimum to the maximum flier points.

jitterRangeWhisker=[]

fliers = bp['fliers']
fly_count=0
for fly in fliers:
    fly_count+=1
    data = fly.get_data()
    if(len(data[1])!=0):
        print fly_count, min(data[1]), max(data[1]),"range-",(max(data[1])-min(data[1]))
        jitterRangeWhisker.append((max(data[1])-min(data[1])))

    else:
        jitterRangeWhisker.append(0)

    # fly.set_data([data[0][0],data[0][-1]],[data[1][0],data[1][-1]])

print jitterRangeWhisker
Inputrates=[12000,63000,63000,4,2,3,12000,105,310,15000,15000,34000,68000,3000]

ax.set_xscale('log')

x = Inputrates
y = jitterRangeWhisker
plt.plot(x, y, "o")

plt.ylabel('Diff between min and max whisker value ', fontsize=15, rotation='45',ha='right')
plt.xlabel('Peak rate (log scale)', fontsize=15)

fig.savefig(outDirForBoxplot+'scatterPlotPeakrateAndWhiskerrange-'+expID+'.png', bbox_inches='tight')

exit()


# print "Median values are - "
# medianList1=[]
# medianList=[]
# i=1
# for medline in bp['medians']:
#     linedata = medline.get_ydata()
#     medianList1.append((i,float(linedata[0])))
#     medianList.append(float(linedata[0]))
#     print i,float(linedata[0])
#     i=i+1
#
# print "Median values are-\n",medianList1
# print  "Average Median value is -",np.mean(medianList)
# print "Min median value",min(medianList)
#
# # whisList1=[]
# # for medline in bp['whiskers']:
# #     whisList2=[]
# #     linedata = medline.get_ydata()
# #     medianList2.append((i,float(linedata[0])))
# # print medianList2
# # print max(p1[10]),max(p1[11])
#
# # print "Max values  values of CPU usage each hour - "
# # for i in xrange(0,24):
# #     print i,max(res[i])
# #
# # print "Min values  values of CPU usage each hour - "
# # for i in xrange(0,24):
# #     print i,min(res[i])
#
# print "whisker values -"
# print [item.get_ydata()[0] for item in bp['whiskers']]
#
#
# print "fliers"
#
# fliers = bp['fliers']
#
# exit()
#
# print "printimg first and 3rd quartiles - "
# quartiles=[]
# # medianList=[]
# i=1
# for medline in bp['boxes']:
#     linedata = medline.get_ydata()
#     # print i,linedata
#     quartiles.append((i,float(linedata[0])))
#     # medianList.append(float(linedata[0]))
#     print i,linedata[0],linedata[2]
#     i=i+1







