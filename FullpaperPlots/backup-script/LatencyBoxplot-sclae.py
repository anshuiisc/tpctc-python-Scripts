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


outDirForBoxplot="/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/plot/"
expID="-13*"
# expID="*-0.11.*"
print expID
cmd="ls -1 "+"/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/dat/L-*"+expID+"*.dat"



# for out_dir in os.popen(cmd).read().split("\n"):
#     if(len(out_dir)!=0):
#         # print out_dir.split("/")[-1]
#         temp=out_dir.split("/")
#         # print temp
#         temp[-1]="clear-"+temp[-1]
#         newout_dir="/".join(temp)
#
#         cmdforGrep="grep Cpu "+out_dir +"> " +newout_dir
#         print cmdforGrep
#         os.popen(cmdforGrep)

out_dir_list=[]
for out_dir in os.popen(cmd).read().split("\n"):
   if out_dir:
       out_dir_list.append(out_dir)

print out_dir_list



## using x as method declared above
# out_dir_list=sorted(out_dir_list,key=orderinglogic)
# print out_dir_list

out_dir_list=sorted(out_dir_list,key=orderinglogicForThreadFromEXPID)
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
bp = ax.boxplot(p)
ax.set_ylabel('Latency (in millisec.)', color='b')
ax.set_ylim([0,15000])

def slice(i):

    rate = i.split("/")[-1].split("-")[-1].split(".")[0] + "." + i.split("/")[-1].split("-")[-1].split(".")[1]
    print rate, 100 / float(rate)
    return i.split("/")[-1].split("-")[-2] + "-" + i.split("/")[-1].split("-")[-1] + "(" + str(int(100 / float(rate))) + ")"
    # [-3]+ "-" + x.split("/")[-1].split("-")[-2] +"-"+x.split("/")[-1].split("-")[-1]
print map(slice,out_dir_list)
print len(out_dir_list)
# ax.set_yticklabels(1000,2000,3000,4000,5000,7000,1000,15000,20000)
# ax.set_xticklabels(map(slice,out_dir_list), rotation='90')

plt.yticks(np.arange(0, 15000, 1000))

ax.yaxis.grid(which='minor', alpha=0.5)
ax.yaxis.grid(which='major', alpha=0.5)

ax.set_xticklabels(map(slice,out_dir_list), rotation='45',ha='right')

# plt.yticks(np.arange(0, 15000, 1000))
#
# ax.yaxis.grid(which='minor', alpha=0.5)
# ax.yaxis.grid(which='major', alpha=0.5)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(15.5, 6.5)

#
# Save the figure
fig.savefig(outDirForBoxplot+"FullBoxPlot-Latency-"+ expID +".png", bbox_inches='tight')