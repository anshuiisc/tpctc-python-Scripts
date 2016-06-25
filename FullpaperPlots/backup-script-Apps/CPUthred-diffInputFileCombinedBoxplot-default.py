def orderinglogic(s1):
    id1=int(s1.split("/")[-1].split("-")[2])
    ratelist1=s1.split("/")[-1].split("-")[3].split(".")
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
import os
import os.path


# outDirForBoxplot="/Users/anshushukla/PycharmProjects/FullTopoSC/script/test/"
# listclearedfiles="ls -1 "+"/Users/anshushukla/PycharmProjects/FullTopoSC/script/test/anshudreamdfsup1.cloudapp.net/clear-cpu*.txt"
# # use for removing 100% before commenting below line ...
# # sed   -i .bak  '/100/d'  clear-cpuFloat-251*
# listbeforegrep="ls -1 "+"/Users/anshushukla/PycharmProjects/FullTopoSC/script/test/anshudreamdfsup1.cloudapp.net/cpu*.txt"



expID="*-1872000**"
folderID=1872000

# expID="*-163*"
# folderID=1631480480611210

outDirForBoxplot="/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/cpu/"+str(folderID)+"/"
listclearedfiles="ls -1 "+"/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/cpu/"+str(folderID)+"/*.net/clear-cpu*"+expID+".txt"
listbeforegrep="ls -1 "+"/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/cpu/"+str(folderID)+"/*.net/cpu*"+expID+".txt"


# use for removing 100% before commenting below line ...
# sed   -i .bak  '/100/d'  clear-cpuFloat-251*
sed_command="sed   -i .bak  '/100/d'  "
print sed_command


for out_dir in os.popen(listbeforegrep).read().split("\n"):
    if(len(out_dir)!=0):
        # print out_dir.split("/")[-1]
        temp=out_dir.split("/")
        # print temp
        temp[-1]="clear-"+temp[-1]
        newout_dir="/".join(temp)

        cmdforGrep="grep Cpu "+out_dir +"> " +newout_dir
        print cmdforGrep
        cmdforSED=sed_command+"  "+newout_dir
        print cmdforSED
        os.popen(cmdforGrep)
        # os.popen(cmdforSED)

out_dir_list = []
for out_dir in os.popen(listclearedfiles).read().split("\n"):
    if out_dir:
        out_dir_list.append(out_dir)

## using x as method declared above
out_dir_list = sorted(out_dir_list, key=orderinglogic)
print out_dir_list


filename1 = outDirForBoxplot + "/CPU-BoxplotDetails-" + expID + ".txt"
if os.path.exists(filename1):
    print "yes present"
    os.remove(filename1)

## Full box plot
# name1="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/VMpushTest/c/top_1thread-Base-clear.txt"
p = []
for i in out_dir_list:
    # dSpout = pd.read_csv(i, engine='python', header=None)
    dSpout = pd.read_csv(i, engine='c', header=None, delim_whitespace=True)

    # dSpout[1] = dSpout[1]-1
    # dSpout = dSpout[dSpout[1] < 100]
    # dSpout = dSpout[dSpout[1] >= 10]
    # print dSpout[1]+dSpout[3]
    print i, "--", (dSpout[1] + dSpout[3]).mean()
    p.append(dSpout[1] + dSpout[3])

    print dSpout.describe()

    with open(filename1, "a") as myfile:
        myfile.write(i + "\n\n")
        myfile.write("\t\t" + str((dSpout[1] + dSpout[3]).describe()) + "\n")



#######MEMORY CODE###############################################################################################################################################

# expID="*-60*"

# outDirForBoxplotMem="/Users/anshushukla/PycharmProjects/FullTopoSC/script/test/"
listclearedfilesMem="ls -1 "+"/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/cpu/"+str(folderID)+"/*.net/clear-Mem-*"+expID+".txt"
listbeforegrepMem="ls -1 "+"/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/cpu/"+ str(folderID) +"/*.net/cpu*"+expID+".txt"

def orderinglogicMem(s1):
    id1=int(s1.split("/")[-1].split("-")[3])
    ratelist1=s1.split("/")[-1].split("-")[4].split(".")
    ratelist1.pop()
    rate1=float(".".join(ratelist1))

    return id1-rate1

for out_dir in os.popen(listbeforegrepMem).read().split("\n"):
    if(len(out_dir)!=0):
        # print out_dir.split("/")[-1]
        temp=out_dir.split("/")
        # print temp
        temp[-1]="clear-Mem-"+temp[-1]
        newout_dir="/".join(temp)

        cmdforGrep = "grep Mem: " + out_dir + "> " + newout_dir
        print cmdforGrep
        os.popen(cmdforGrep)

out_dir_listmem=[]
for out_dir in os.popen(listclearedfilesMem).read().split("\n"):
   if out_dir:
       out_dir_listmem.append(out_dir)

## using x as method declared above
out_dir_list=sorted(out_dir_listmem,key=orderinglogicMem)
print out_dir_list

filename1=outDirForBoxplot + "/MEM-BoxplotDetails-"+expID+".txt"
if os.path.exists(filename1 ):
    print "yes present"
    os.remove(filename1)



q=[]
total_RAM=28811756
for i in out_dir_list:
       # dSpout = pd.read_csv(i, engine='python', header=None)
       dSpoutMem = pd.read_csv(i, engine='c', header=None,delim_whitespace=True)
       print dSpoutMem.head(10)
       # exit()

       # dSpout = dSpout[dSpout[4] >= 10]
       # print dSpout[1]+dSpout[3]

       print dSpoutMem[4]
       # p.append(dSpout[4])
       #
       # with open(filename1, "a") as myfile:
       #     myfile.write(i + "\n\n")
       #     myfile.write("\t\t" + str((dSpout[4]).describe()) + "\n")


       print (dSpoutMem[4] / total_RAM) * 100
       q.append((dSpoutMem[4] / total_RAM) * 100)

       with open(filename1, "a") as myfile:
           myfile.write(i + "\n\n")
           myfile.write("\t\t" + str((100 * (dSpoutMem[4] / total_RAM)).describe()) + "\n")
###########################################################################################################################################################################################





print len(p),len(q)
# exit()
########
from pylab import plot, show, savefig, xlim, figure, \
    hold, ylim, legend, boxplot, setp, axes
# function for setting the colors of the box plots pairs
def setBoxColors(bp):
    setp(bp['boxes'][0], color='blue')
    setp(bp['caps'][0], color='blue')
    setp(bp['caps'][1], color='blue')
    setp(bp['whiskers'][0], color='blue')
    setp(bp['whiskers'][1], color='blue')
    setp(bp['fliers'][0], color='blue')
    # setp(bp['fliers'][1], color='blue')
    setp(bp['medians'][0], color='blue')

    setp(bp['boxes'][1], color='red')
    setp(bp['caps'][2], color='red')
    setp(bp['caps'][3], color='red')
    setp(bp['whiskers'][2], color='red')
    setp(bp['whiskers'][3], color='red')
    # setp(bp['fliers'][2], color='red')
    # setp(bp['fliers'][3], color='red')
    setp(bp['medians'][1], color='red')

fig = figure()
ax = axes()
hold(True)


# Some fake data to plot
# A = [p, [7, 2]]
# B = [q, [7, 2, 5]]
# C = [[3, 2, 5, 7], [6, 7, 3]]

#
# A = [p, [7, 2]]
# B = [q, [7, 2, 5]]
# C = [[3, 2, 5, 7], [6, 7, 3]]

A=[p[0],q[0]]
B=[p[1],q[1]]
C=[p[2],q[2]]

D=[p[3],q[3]]
E=[p[4],q[4]]
# F=[p[5],q[5]]
# G=[p[6],q[6]]
# H=[p[7],q[7]]
# I=[p[8],q[8]]



fig = figure()
ax = axes()
hold(True)

# first boxplot pair
bp = boxplot(A, positions=[1, 2], widths=0.6,whis=100000000)
setBoxColors(bp)

for box in bp['boxes']:
    # change outline color
    box.set( linewidth=2)
for cap in bp['whiskers']:
    cap.set(linewidth=2)
for median in bp['medians']:
    median.set(linewidth=2)

# second boxplot pair
bp = boxplot(B, positions=[4, 5], widths=0.6,whis=100000000)
setBoxColors(bp)

for box in bp['boxes']:
    # change outline color
    box.set( linewidth=2)
for cap in bp['whiskers']:
    cap.set(linewidth=2)
for median in bp['medians']:
    median.set(linewidth=2)

# thrid boxplot pair
bp = boxplot(C, positions=[7, 8], widths=0.6,whis=100000000)
setBoxColors(bp)

for box in bp['boxes']:
    # change outline color
    box.set( linewidth=2)
for cap in bp['whiskers']:
    cap.set(linewidth=2)
for median in bp['medians']:
    median.set(linewidth=2)
#
bp = boxplot(D, positions=[10,11], widths=0.6,whis=100000000)
setBoxColors(bp)

for box in bp['boxes']:
    # change outline color
    box.set( linewidth=2)
for cap in bp['whiskers']:
    cap.set(linewidth=2)
for median in bp['medians']:
    median.set(linewidth=2)
#
bp = boxplot(E, positions=[13, 14], widths=0.6,whis=100000000)
setBoxColors(bp)

for box in bp['boxes']:
    # change outline color
    box.set( linewidth=2)
for cap in bp['whiskers']:
    cap.set(linewidth=2)
for median in bp['medians']:
    median.set(linewidth=2)

#
# bp = boxplot(F, positions=[16, 17], widths=0.6, whis=100000000)
# setBoxColors(bp)
#
# for box in bp['boxes']:
#     # change outline color
#     box.set(linewidth=2)
# for cap in bp['whiskers']:
#     cap.set(linewidth=2)
# for median in bp['medians']:
#     median.set(linewidth=2)
#
# #
# bp = boxplot(G, positions=[19, 20], widths=0.6, whis=100000000)
# setBoxColors(bp)
#
# for box in bp['boxes']:
#     # change outline color
#     box.set(linewidth=2)
# for cap in bp['whiskers']:
#     cap.set(linewidth=2)
# for median in bp['medians']:
#     median.set(linewidth=2)


#
# bp = boxplot(H, positions=[22, 23], widths=0.6,whis=100000000)
# setBoxColors(bp)
#
# for box in bp['boxes']:
#     # change outline color
#     box.set( linewidth=2)
# for cap in bp['whiskers']:
#     cap.set(linewidth=2)
# for median in bp['medians']:
#     median.set(linewidth=2)

#
# bp = boxplot(I, positions=[25, 26], widths=0.6, whis=100000000)
# setBoxColors(bp)
#
# for box in bp['boxes']:
#     # change outline color
#     box.set(linewidth=2)
# for cap in bp['whiskers']:
#     cap.set(linewidth=2)
# for median in bp['medians']:
#     median.set(linewidth=2)

##

## visual improvement
# for box in bp['boxes']:
#     # change outline color
#     box.set( color='k', linewidth=2)
# for cap in bp['whiskers']:
#     cap.set(color='b', linewidth=2)
# for median in bp['medians']:
#     median.set(color='r', linewidth=2)

# plt.tick_params(axis='both', which='major', labelsize=15)

#setting horizontal and vertical lines for grid
for i in np.arange(0.1,100,5):
    print i
    plt.hlines(i,0,25,colors='0.80',linestyles='-')
for i in np.arange(20,120,20):
    print i
    plt.hlines(i,0,25,colors='0.50',linestyles='-')

##

# set axes limits and labels
xlim(0, 15)
ylim(0, 100)
ax.set_xticklabels(['1', '2', '3','4',  '5'  ])
ax.set_xticks([1.5,      4.5, 7.5 ,10.5 ,13.5 ])

# ax.set_xticklabels(['1', '2'])
# ax.set_xticks([1.5, 4.5])

# draw temporary red and blue lines and use them to create a legend
hB, = plot([1, 1], 'b-')
hR, = plot([1, 1], 'r-')

legend((hB, hR), ('CPU', 'Memory'),loc='upper center', bbox_to_anchor=(0.5, 1.12),
          ncol=3, fancybox=True, shadow=True)

hB.set_visible(False)
hR.set_visible(False)

plt.ylabel('Cumulative CPU/Mem %',fontsize=15)
plt.xlabel('Virtual Machines',fontsize=15)

# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
#           ncol=3, fancybox=True, shadow=True)



# # first boxplot pair
# bp = boxplot([p,q], positions=[1, 2], widths=0.6)
# setBoxColors(bp)

# if(len(p)==len(q)):
#     for i in xrange(len(p)):
#         # first boxplot pair
#         bp = boxplot([p,q], positions=[1,2], widths=0.6)
#         setBoxColors(bp)
#
#         # second boxplot pair
#         # bp = boxplot(q[i], positions=[i+2], widths=0.6)
#         # setBoxColors(bp)

# savefig(outDirForBoxplot+'VMwiseCPUMEMBoxPlotDefault-'+expID+'.png', bbox_inches='tight')

savefig(outDirForBoxplot+'BoxPlotLatency-MaxAlloc-OurMapping.png', bbox_inches='tight')



# savefig('boxcompare2.png')
# fig.savefig(outDirForBoxplot+'FullBoxPlot-CPU-FULL-'+expID+'.png', bbox_inches='tight')
# show()




######

exit()


fig = plt.figure(1, figsize=(9, 6))
ax = fig.add_subplot(111)
bp = ax.boxplot(p)

def slice(i):

    rate = i.split("/")[-1].split("-")[-1].split(".")[0] + "." + i.split("/")[-1].split("-")[-1].split(".")[1]
    newrate=i.split("/")[-1].split("-")[-2][-2:]
    # print rate, 100 / float(rate)
    # return i.split("/")[-1].split("-")[-2] + "-" + i.split("/")[-1].split("-")[-1] + "(" + str(int(100 / float(rate))) + ")"
    return i.split("/")[-1].split("-")[-2] + "-" + i.split("/")[-1].split("-")[-1] + "(" + newrate + ")"

# print map(slice,out_dir_list)
# print len(out_dir_list)
# ax.set_yticklabels(1000,2000,3000,4000,5000,7000,1000,15000,20000)
# ax.set_xticklabels(map(slice,out_dir_list), rotation='90')

ax.yaxis.grid(which='minor', alpha=0.5)
ax.yaxis.grid(which='major', alpha=0.5)

ax.set_xticklabels(map(slice,out_dir_list), rotation='45',ha='right')
#
# Save the figure
# fig.savefig(outDirForBoxplot+'FullBoxPlot-CPU-FULL-'+expID+'.png', bbox_inches='tight')
