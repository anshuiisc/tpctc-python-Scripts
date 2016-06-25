import collections
import matplotlib.pyplot as plt

def slice(x):
    # id1=int(s1.split("/")[-1].split("-")[2])
    # ratelist1=x.split("/")[-1].split("-")[3].split(".")
    # ratelist1.pop()
    # rate1=float(".".join(ratelist1))

    if (x.split("/")[0].split("-")[-1] == "BlockWindowAverage"):
        return "AVG"
    if (x.split("/")[0].split("-")[-1] == "DistinctApproxCount"):
        return "DAC"
    if (x.split("/")[0].split("-")[-1] == "BloomFilterCheck"):
        return "BLF"
    if (x.split("/")[0].split("-")[-1] == "AzureBlobDownload"):
        return "ABD"
    if (x.split("/")[0].split("-")[-1] == "AzureBlobUpload"):
        return "ABU"
    if (x.split("/")[0].split("-")[-1] == "AzureTable"):
        return "ATQ"
    if (x.split("/")[0].split("-")[-1] == "MQTTPublish"):
        return "MQP"
    if (x.split("/")[-1].split("-")[-1] == "IdentityTopologyFloat"):
        return x.split("/")[-1].split("-")[-4]
    if (x.split("/")[0].split("-")[-1] == "XMLParse"):
        return "XML"
    if (x.split("/")[0].split("-")[-1] == "DecisionTreeClassify"):
        return "DTC"
    if (x.split("/")[0].split("-")[-1] == "LinearRegressionPredictor"):
        return "MLR"
    if (x.split("/")[0].split("-")[-1] == "SimpleLinearRegressionPredictor"):
        return "SLR"
    if (x.split("/")[0].split("-")[-1] == "KalmanFilter"):
        return "KAL"
    if (x.split("/")[0].split("-")[-1] == "SecondOrderMoment"):
        return "SOM"
    # else:
        # return x.split("/")[-1].split("/")[-1] + "-(" + str(int(100 / rate1)) + ")"





outDirForBoxplot="/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/plot/"
expID="*"


fig = plt.figure(1, figsize=(12, 8))
ax = fig.add_subplot(111)

# dictionary = plt.figure()



D = {

    u'01-XMLParse': 310,

    u'02-BloomFilterCheck': 63000,

    u'03-BlockWindowAverage': 12000,
    u'04-DistinctApproxCount': 63000,
    u'05-KalmanFilter': 68000,
    u'06-SecondOrderMoment': 3000,

    u'07-DecisionTreeClassify': 15000,
    u'08-LinearRegressionPredictor': 15000,
    u'09-SimpleLinearRegressionPredictor': 34000,

    u'10-AzureBlobDownload': 4,
    u'11-AzureBlobUpload': 2,
    u'12-AzureTable': 3,
    u'13-MQTTPublish': 8400,

    ######## un-ordered ###
    # u'01-BlockWindowAverage':12000,
    # u'02-DistinctApproxCount': 63000,
    #
    # u'03-BloomFilterCheck':63000,
    #
    # u'04-AzureBlobDownload': 4,
    # u'05-AzureBlobUpload': 2,
    # u'06-AzureTable': 3,
    # u'07-MQTTPublish': 8400,
    #
    # # u'08-PiByViete': 105,
    #
    # u'09-XMLParse': 310,
    #
    # u'10-DecisionTreeClassify': 15000,
    # u'11-LinearRegressionPredictor': 15000,
    # u'12-SimpleLinearRegressionPredictor': 34000,
    #
    # u'13-KalmanFilter': 68000,
    # u'14-SecondOrderMoment': 3000,


}



od = collections.OrderedDict(sorted(D.items()))


ax.set_yscale('log')

print D.values()
print od.values()

# barlist=plt.bar(range(len(D)), D.values(), align='center')
# plt.xticks(range(len(D)), D.keys() , rotation='45',ha='right')
print map(slice,od.keys())


barlist=plt.bar(range(len(od)), od.values(), align='center', zorder=10)
# plt.xticks(range(len(od)), od.keys() , rotation='45',ha='right')
# plt.xticks(range(len(od)), od.keys() )

plt.xticks(range(len(od)), map(slice,od.keys()) )


# plt.grid(True)
# plt.xlim([0,13])
plt.axis('tight')
ax.set_ylim([1-0.1,100000+1])


import numpy as np
#setting horizontal and vertical lines for grid
# for i in np.arange(0.2,100000,10000):
for i in xrange(1,6,1):
    # print 10**i
    ax.axhline(10**i, color='k',  alpha=0.7)


# for i in xrange(1,6,1):
#     print 5**i
#     ax.axhline(5**i, color='k',  alpha=0.5)

# for i in np.arange(1, 100000,  1000):
#     print i
#     ax.axhline(i, color='k', alpha=0.5)

const=[1,2,3,4,5,6,7,8,9,10]

for i in xrange(1,10):

    ax.axhline((i), color='k', alpha=0.5)


for i in xrange(1,10):
    p=10**i
    for j in xrange(1,10):
        print j,10**i,j*(10**i)
        ax.axhline(j*(10**i), color='k', alpha=0.4)



barlist[0].set_color('b')

barlist[1].set_color('g')

barlist[2].set_color('r')
barlist[3].set_color('r')
barlist[4].set_color('r')
barlist[5].set_color('r')

barlist[6].set_color('y')
# barlist[7].set_color('c')
barlist[7].set_color('y')
barlist[8].set_color('y')

barlist[9].set_color('m')
barlist[10].set_color('m')
barlist[11].set_color('m')
barlist[12].set_color('m')

        # b: blue
        # g: green
        # r: red
        # c: cyan
        # m: magenta
        # y: yellow
        # k: black
        # w: white
        #
plt.tick_params(axis='x', which='major', labelsize=22)
plt.tick_params(axis='y', which='major', labelsize=26)
plt.ylabel("Peak Rate (msg/sec) [log scale]", fontsize=26)
plt.title('[Colors indicate different IoT Tasks Categories]', fontsize=26)



# plt.tick_params(axis='both', which='major', labelsize=16)

# plt.ylabel("Frequency", fontsize=20)


# plt.ylabel('Peak Rate (log scale) ', fontsize=15)




# fig.savefig(outDirForBoxplot+'TEST-Bar-Plot-rename-ord'+expID+'.pdf', bbox_inches='tight')
fig.savefig("/Users/anshushukla/Downloads/Incomplete/pubs/vldbw-tpctc-2016/latex/plots/microBenchmark/peakRateBarplot.pdf", bbox_inches='tight')