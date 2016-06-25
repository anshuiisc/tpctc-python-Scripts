import pandas as pd
import numpy as np
# import matplotlib
import os
# matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
import sys
import os.path


# if(len(sys.argv) != 3):  # 4
#        print "Expected spout Throughput .dat file as first argument (spout word will be replaced with sink to get sink file name)!!! Exiting!!!"
#        #print "Expected sink Throughput .dat file as second argument!!! Exiting!!!"
#        print "Expected Output Dir Path as second argument!!! Exiting!!!"
#        exit(1)



csvSpoutFileName = sys.argv[1]  #'/home/tarun/dream/SCRIPTS/TETC-KEY/RECEIVED/T-spout-SplitContentBasedTopology-SYS-333-1.0.dat'  'T-spout-WordCountTopology-SYS-333-1.0.dat'
#csvSinkFileName = sys.argv[2]
outDir = sys.argv[2]  #'/home/tarun/dream/SCRIPTS/TETC-KEY/RECEIVED/'
#csvFileName = '/home/tarun/dream/SCRIPTS/TETC-KEY/RECEIVED/L-AVG-DataGen_1_N_Topology-TAXI-222-1.0.dat'
fileIdentifier = '-'.join(csvSpoutFileName.split('/')[-1].split('-')[2:])
csvSinkFileName = csvSpoutFileName[0:csvSpoutFileName.rfind('/')+1] + 'T-sink-' + fileIdentifier
fileIdentifier = 'T-' + fileIdentifier
# outPlotFileName = outDir + '/' + fileIdentifier + '.pdf'
outPlotFileName = outDir + '/' + fileIdentifier + '.png'
outRelativePlotFileName = outDir + '/T-R-' + fileIdentifier[2:] + '.pdf'
outRelativeAbsolutePlotFileName = outDir + '/T-R-A-' + fileIdentifier[2:] + '.pdf'
outRelativeAbsoluteMeanValueFileName = outDir + '/T-R-A-M-' + fileIdentifier[2:] + '.pdf'

dSpoutThr = pd.read_csv(csvSpoutFileName, engine='python', header=None);
dSinkThr = pd.read_csv(csvSinkFileName, engine='python', header=None);

x = dSpoutThr[0]
ySpout = dSpoutThr[1]
ySink = dSinkThr[1]

lenSpout = len(dSpoutThr)
lenSink = len(dSinkThr)

for i in xrange(0, lenSpout-lenSink):
    ySink.ix[lenSink+i] = 0

delta = x.ix[len(x)-1] - x.ix[len(x)-2]

for i in xrange(0, lenSink-lenSpout):
    ySpout.ix[lenSpout+i] = 0
    x.ix[lenSpout+i] = x.ix[lenSpout-1+i] + delta


plt.scatter(x, ySpout,c= 'r', label='Input Rate')
plt.scatter(x, ySink, c='b', label='Output Rate')


legend = plt.legend(loc='upper right', shadow=True)
# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
frame.set_facecolor('0.90')


rate = fileIdentifier.split("-")[-1].split(".")[0] + "." + fileIdentifier.split("-")[-1].split(".")[1]
print rate
plt.title(fileIdentifier+' Throughput('+  str(int(50 / float(rate)))+")")
plt.xlabel('Relative Time (in secs)')
plt.ylabel('Throughput (msgs/sec)')
plt.savefig(outPlotFileName)
plt.cla()

print 'Figure saved at ' + outPlotFileName

exit(1)

### Relative Output Throughput and Turbulence Plot

#selMap = {'Split' : 1.0, 'Fork' : 3.0, 'Seq' : 1.0, 'WordCount' : 5.0/60.0, 'Project' : 1.0, 'Identity' : 1.0}  #, 'DataGen' : } Word Count also dataset dependent, WC Return w.r.t. SYS dataset
selMap = {'Split' : 1.0, 'Fork' : 3.0, 'Seq' : 1.0, 'WordCount' : 1.0, 'AvgAgg' : 1.0, 'Project' : 1.0, 'Grep' : 1.0, 'Identity' : 1.0, 'DataGen' : 1.0}  # 'DataGen' , 'WordCount' ('AvgAgg'), 'Grep'  are dataset dependent

sel = 0.0
for k in selMap:
    if csvSpoutFileName.rfind(k) != -1:
		sel = selMap[k]
		break

if k.find('WordCount') != -1 or k.find('AvgAgg') != -1:
    if csvSpoutFileName.rfind('TAXI') != -1:
        sel = 8.0/60.0
    elif csvSpoutFileName.rfind('SYS') != -1:
        sel = 5.0/60.0
    elif csvSpoutFileName.rfind('PLUG') != -1:
        sel = 1.0/60.0
        
if k.find('Grep') != -1:
    if csvSpoutFileName.rfind('TAXI') != -1:
        sel = 17169.0/450504.0
    elif csvSpoutFileName.rfind('SYS') != -1:
        sel = 1383.0/3779.0
    elif csvSpoutFileName.rfind('PLUG') != -1:
        sel = 400879.0/1002199.0

if k.find('DataGen') != -1:
    if csvSpoutFileName.rfind('TAXI') != -1:
        sel = 17.0
    elif csvSpoutFileName.rfind('SYS') != -1:
        sel = 9.0
    elif csvSpoutFileName.rfind('PLUG') != -1:
        sel = 7.0

yRelative = pd.DataFrame(columns = [0])
yRelativeAbsolute = pd.DataFrame(columns = [0])
avgAbsolute = 0.0
for i in xrange(0, max(lenSpout, lenSink)):
    if ySink.ix[i] != 0 and ySpout.ix[i] != 0:
       yRelative.loc[i] = ySink.ix[i]/(sel*ySpout.ix[i])
       yRelativeAbsolute.loc[i] = abs(1.0 - yRelative.loc[i])
       avgAbsolute += yRelativeAbsolute.ix[i,0]
    else:
       yRelative.loc[i] = 0
       yRelativeAbsolute.loc[i] = 0

avgAbsolute = avgAbsolute / max(lenSpout, lenSink)

plt.plot(x, yRelative)

plt.title(fileIdentifier+'Relative Throughput')
plt.xlabel('Relative Time (in secs)')
plt.ylabel('Relative Throughput (Ratio)')
plt.savefig(outRelativePlotFileName)
plt.cla()

print 'Figure saved at ' + outRelativePlotFileName

plt.plot(x, yRelativeAbsolute)

plt.title(fileIdentifier+'Relative Absolute Throughput')
plt.xlabel('Relative Time (in secs)')
plt.ylabel('Relative Absolute Throughput (Ratio) (Turbulence)')
plt.savefig(outRelativeAbsolutePlotFileName)
plt.cla()

outRelativeAbsoluteMeanValueFileName = outDir + '/T-R-A-M-' + fileIdentifier[2:] + '.dat'
with open(outRelativeAbsoluteMeanValueFileName, 'w') as f:
    f.write(fileIdentifier + ',' + str(avgAbsolute) + '\n')

print 'Average Relative Absolute Throughput (Turbulence) file at ' + outRelativeAbsoluteMeanValueFileName
