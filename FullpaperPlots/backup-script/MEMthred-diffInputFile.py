def orderinglogic(s1):
    id1=int(s1.split("/")[-1].split("-")[3])
    ratelist1=s1.split("/")[-1].split("-")[4].split(".")
    ratelist1.pop()
    rate1=float(".".join(ratelist1))

    return id1-rate1

import pandas as pd
import numpy as np
import matplotlib
import os
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
import sys
import os.path

# outDirForBoxplot="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/parsing/log2/plot/"
# listclearedfiles="ls -1 "+"/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/parsing/log2/cpu/clear-Mem-*.txt"
#
# listbeforegrep="ls -1 "+"/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/parsing/log2/cpu/cpu*.txt"



expID="*"

outDirForBoxplot="/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/plot/"
listclearedfiles="ls -1 "+"/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/cpu/clear-Mem-*"+expID+".txt"
listbeforegrep="ls -1 "+"/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/cpu/cpu*"+expID+".txt"


# for out_dir in os.popen(listbeforegrep).read().split("\n"):
#     if(len(out_dir)!=0):
#         # print out_dir.split("/")[-1]
#         temp=out_dir.split("/")
#         # print temp
#         temp[-1]="clear-Mem-"+temp[-1]
#         newout_dir="/".join(temp)
#
#         # cmdforGrep="grep Mem "+out_dir +"> " +newout_dir
#         cmdforGrep = "grep Mem: " + out_dir + "> " + newout_dir
#         print cmdforGrep
#         os.popen(cmdforGrep)

# out_dir_list=[]
# for out_dir in os.popen(listclearedfiles).read().split("\n"):
#    if out_dir:
#        out_dir_list.append(out_dir)
#
# ## using x as method declared above
# out_dir_list=sorted(out_dir_list,key=orderinglogic)
# print out_dir_list

baseClearFilepath="/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/cpu/"
out_dir_list=[]
clear_out_dir_list = [


"clear-Mem-cpuParse-85111310-1.0.txt",
"clear-Mem-cpuBloomFilterCheck-9216311000-1.0.txt",
"clear-Mem-cpuBlockWindow-6211211000-1.0.txt",
"clear-Mem-cpuDistinctApproxCount-9216311000-1.0.txt",
"clear-Mem-cpuKalmanFilter-9416811000-1.0.txt",
"clear-Mem-cpuSecondOrderMoment-8110311000-1.0.txt",
"clear-Mem-cpuDecisionTreeClassify-8111511000-1.0.txt",
"clear-Mem-cpuLinearRegressionPredictor-8211511000-1.0.txt",
"clear-Mem-cpuSimpleLinearRegressionPredictor-8313411000-1.0.txt",
"clear-Mem-cpuBlob-271111-2.5.txt",
"clear-Mem-cpuBlobUpload-71111002-1.0.txt",
"clear-Mem-cpuTable-6011103-1.0.txt",
"clear-Mem-cpuMQTTPublish-8111211000-1.0.txt",

# ####un-ordered #####
#
# "clear-Mem-cpuBlockWindow-6211211000-1.0.txt",
# "clear-Mem-cpuDistinctApproxCount-9216311000-1.0.txt",
# "clear-Mem-cpuBloomFilterCheck-9216311000-1.0.txt",
# "clear-Mem-cpuBlob-271111-2.5.txt",
# "clear-Mem-cpuBlobUpload-71111002-1.0.txt",
# "clear-Mem-cpuTable-6011103-1.0.txt",
# "clear-Mem-cpuMQTTPublish-8111211000-1.0.txt",
# # "clear-Mem-cpuFloat-91111105-1.0.txt",
# "clear-Mem-cpuParse-85111310-1.0.txt",
# "clear-Mem-cpuDecisionTreeClassify-8111511000-1.0.txt",
# "clear-Mem-cpuLinearRegressionPredictor-8211511000-1.0.txt",
# "clear-Mem-cpuSimpleLinearRegressionPredictor-8313411000-1.0.txt",
# "clear-Mem-cpuKalmanFilter-9416811000-1.0.txt",
# "clear-Mem-cpuSecondOrderMoment-8110311000-1.0.txt"

]

for i in clear_out_dir_list:
    out_dir_list.append(baseClearFilepath+i)

print out_dir_list

filename1=outDirForBoxplot + "/MEM-BoxplotDetails-"+expID+".txt"
if os.path.exists(filename1 ):
    print "yes present"
    os.remove(filename1)

## Full box plot
# name1="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/VMpushTest/c/top_1thread-Base-clear.txt"
p=[]
total_RAM=3523124
for i in out_dir_list:
       # dSpout = pd.read_csv(i, engine='python', header=None)
       dSpout = pd.read_csv(i, engine='c', header=None,delim_whitespace=True)
       print dSpout.head(10)
       # exit()

       # dSpout = dSpout[dSpout[4] >= 10]
       # print dSpout[1]+dSpout[3]

       # print dSpout[4]
       # p.append(dSpout[4])
       #
       # with open(filename1, "a") as myfile:
       #     myfile.write(i + "\n\n")
       #     myfile.write("\t\t" + str((dSpout[4]).describe()) + "\n")

       print (dSpout[4] / total_RAM) * 100
       p.append((dSpout[4] / total_RAM) * 100)

       with open(filename1, "a") as myfile:
           myfile.write(i + "\n\n")
           myfile.write("\t\t" + str((100 * (dSpout[4] / total_RAM)).describe()) + "\n")

       # exit()
# dSpout = pd.read_csv(name1, engine='c', header=None,delim_whitespace=True)
                     # names=['us','sy','ni','id','wa','hi','si','st'],sep=' ')
# print dSpout
# file sample
#      0      1    2     3    4   5    6     7    8    9    10  11   12  13   14  15  16
# %Cpu(s):   9.3  us,   4.0  sy,   0  ni,  85.7  id,  0.9   wa, 0    hi, 0.1  si, 0   st

# print p
#
# fig = plt.figure(1, figsize=(9, 6))
fig = plt.figure(1, figsize=(12, 8))

# Create an axes instance
ax = fig.add_subplot(111)
# Create the boxplot
# bp = ax.boxplot(p)

## visual improvement
bp = ax.boxplot(p,whis=1000000000,showfliers=False)

# bp=ax.boxplot(p, notch=False, sym='+', vert=True, whis=1.5,
#         positions=None, widths=None, patch_artist=False,
#         bootstrap=None, usermedians=None, conf_intervals=None)


for box in bp['boxes']:
    # change outline color
    box.set( color='k', linewidth=3)
for cap in bp['whiskers']:
    cap.set(color='b', linewidth=4)
for median in bp['medians']:
    median.set(color='r', linewidth=4)

def slice(i):

    rate = i.split("/")[-1].split("-")[-1].split(".")[0] + "." + i.split("/")[-1].split("-")[-1].split(".")[1]
    newrate=i.split("/")[-1].split("-")[-2][-2:]
    # print rate, 100 / float(rate)
    # return i.split("/")[-1].split("-")[-2] + "-" + i.split("/")[-1].split("-")[-1] + "(" + str(int(100 / float(rate))) + ")"
    # return i.split("/")[-1].split("-")[-2] + "-" + i.split("/")[-1].split("-")[-1] + "(" + newrate + ")"

    # return i.split("/")[-1].split("-")[-3].replace("cpu", "Mem")


    if (i.split("/")[-1].split("-")[-3] == "cpuBlockWindow"):
        return "AVG"
    if (i.split("/")[-1].split("-")[-3] == "cpuDistinctApproxCount"):
        return "DAC"
    if (i.split("/")[-1].split("-")[-3] == "cpuBloomFilterCheck"):
        return "BLF"
    if (i.split("/")[-1].split("-")[-3] == "cpuBlob"):
        return "ABD"
    if (i.split("/")[-1].split("-")[-3] == "cpuBlobUpload"):
        return "ABU"
    if (i.split("/")[-1].split("-")[-3] == "cpuTable"):
        return "ATQ"
    if (i.split("/")[-1].split("-")[-3] == "cpuMQTTPublish"):
        return "MQP"
    # if (i.split("/")[-1].split("-")[-4] == "IdentityTopologyFloat"):
    #     return i.split("/")[-1].split("-")[-4]
    if (i.split("/")[-1].split("-")[-3] == "cpuParse"):
        return "XML"
    if (i.split("/")[-1].split("-")[-3] == "cpuDecisionTreeClassify"):
        return "DTC"
    if (i.split("/")[-1].split("-")[-3] == "cpuLinearRegressionPredictor"):
        return "MLR"
    if (i.split("/")[-1].split("-")[-3] == "cpuSimpleLinearRegressionPredictor"):
        return "SLR"
    if (i.split("/")[-1].split("-")[-3] == "cpuKalmanFilter"):
        return "KAL"
    if (i.split("/")[-1].split("-")[-3] == "cpuSecondOrderMoment"):
        return "SOM"
    else:
        return i.split("/")[-1].split("-")[-3]

print map(slice,out_dir_list)
print len(out_dir_list)

# ax.set_yticklabels(1000,2000,3000,4000,5000,7000,1000,15000,20000)
# ax.set_xticklabels(map(slice,out_dir_list), rotation='90')

# ax.xaxis.grid(which='minor', alpha=0.5)
# ax.yaxis.grid(which='major', alpha=0.5)

ax.set_xticklabels(map(slice,out_dir_list))

# Save the figure
# fig.savefig(outDirForBoxplot+'FullBoxPlot-IDLE.png', bbox_inches='tight')

#setting horizontal and vertical lines for grid
for i in np.arange(0.1,100,5):
    print i
    plt.hlines(i,0,25,colors='0.70')
for i in np.arange(20,120,20):
    print i
    plt.hlines(i,0,25,colors='0.50')

# ax.xaxis.grid(which='minor', alpha=0.5)
# ax.yaxis.grid(which='major', alpha=0.5)

plt.tick_params(axis='x', which='major', labelsize=22)
plt.tick_params(axis='y', which='major', labelsize=26)
plt.ylabel("MEM%", fontsize=26)

# fig.savefig(outDirForBoxplot+'TEST-FullBoxPlot-MEM-rename-ord'+expID+'.pdf', bbox_inches='tight')
fig.savefig("/Users/anshushukla/Downloads/Incomplete/pubs/vldbw-tpctc-2016/latex/plots/microBenchmark/FullBoxPlotMEM.pdf", bbox_inches='tight')
