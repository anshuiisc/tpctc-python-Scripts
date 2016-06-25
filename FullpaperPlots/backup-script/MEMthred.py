def orderinglogic(s1):
    id1=int(s1.split("/")[-1].split("-")[3])
    ratelist1=s1.split("/")[-1].split("-")[4].split(".")
    ratelist1.pop()
    rate1=float(".".join(ratelist1))

    # id2=int(s2.split("/")[-1].split("-")[2])
    # ratelist2=s2.split("/")[-1].split("-")[3].split(".")
    # ratelist2.pop()
    # rate2=float(".".join(ratelist2))
    # # print id2,rate2
    #
    # # if(id1 >id2):
    # #     return id1-id2
    # # elif(id1<id2):
    # #     return id2-id1
    # print rate1,rate2
    # if(rate1>rate2):
    #     return 1
    # else:
    #     return 0
    return id1-rate1

import pandas as pd
import numpy as np
import matplotlib
import os
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
import sys
import os.path
outDirForBoxplot="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/parsing/log2/plot/"
listclearedfiles="ls -1 "+"/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/parsing/log2/cpu/clear-Mem-*.txt"

listbeforegrep="ls -1 "+"/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/parsing/log2/cpu/cpu*.txt"
for out_dir in os.popen(listbeforegrep).read().split("\n"):
    if(len(out_dir)!=0):
        # print out_dir.split("/")[-1]
        temp=out_dir.split("/")
        # print temp
        temp[-1]="clear-Mem-"+temp[-1]
        newout_dir="/".join(temp)

        # cmdforGrep="grep Mem "+out_dir +"> " +newout_dir
        cmdforGrep = "grep Mem: " + out_dir + "> " + newout_dir
        print cmdforGrep
        os.popen(cmdforGrep)

out_dir_list=[]
for out_dir in os.popen(listclearedfiles).read().split("\n"):
   if out_dir:
       out_dir_list.append(out_dir)

## using x as method declared above
out_dir_list=sorted(out_dir_list,key=orderinglogic)
print out_dir_list

## Full box plot
# name1="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/VMpushTest/c/top_1thread-Base-clear.txt"
p=[]
for i in out_dir_list:
       # dSpout = pd.read_csv(i, engine='python', header=None)
       dSpout = pd.read_csv(i, engine='c', header=None,delim_whitespace=True)
       print dSpout.head(10)
       # exit()

       dSpout = dSpout[dSpout[4] >= 10]
       # print dSpout[1]+dSpout[3]
       print dSpout[4]
       p.append(dSpout[4])

       # exit()
# dSpout = pd.read_csv(name1, engine='c', header=None,delim_whitespace=True)
                     # names=['us','sy','ni','id','wa','hi','si','st'],sep=' ')
# print dSpout
# file sample
#      0      1    2     3    4   5    6     7    8    9    10  11   12  13   14  15  16
# %Cpu(s):   9.3  us,   4.0  sy,   0  ni,  85.7  id,  0.9   wa, 0    hi, 0.1  si, 0   st

# print p
#
fig = plt.figure(1, figsize=(9, 6))
# Create an axes instance
ax = fig.add_subplot(111)
# Create the boxplot
bp = ax.boxplot(p)

def slice(x):
    # id1=int(s1.split("/")[-1].split("-")[2])
    ratelist1=x.split("/")[-1].split("-")[4].split(".")
    ratelist1.pop()
    rate1=float(".".join(ratelist1))
    return x.split("/")[-1].split("/")[-1]+"-("+str(int(100/rate1))+")"
    # [-3]+ "-" + x.split("/")[-1].split("-")[-2] +"-"+x.split("/")[-1].split("-")[-1]
print map(slice,out_dir_list)
print len(out_dir_list)
# ax.set_yticklabels(1000,2000,3000,4000,5000,7000,1000,15000,20000)
ax.set_xticklabels(map(slice,out_dir_list), rotation='90')

# Save the figure
# fig.savefig(outDirForBoxplot+'FullBoxPlot-IDLE.png', bbox_inches='tight')

fig.savefig(outDirForBoxplot+'FullBoxPlot-MEM.png', bbox_inches='tight')