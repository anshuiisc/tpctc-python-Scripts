#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib
# matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
import sys
import re



# if(len(sys.argv) != 3):
#        print "Expected CSV file as first argument!!! Exiting!!!"
#        print "Expected Output Directory as second argument!!! Exiting!!!"
#        exit(1)

#baseDir = sys.argv[1]
#csvFileName = baseDir

#csvFileName="/home/tarun/dream/SCRIPTS/TETC-KEY/RECEIVED/spout-DataGen_1_N_Topology-SYS-01-1.0.log"
# csvFileName = "/Users/anshushukla/PycharmProjects/DataAnlytics1/Storm/11/spout-GrepColumnTopology-SYS-11-0.01.log"; # spout-DataGen_1_N_Topology-TAXI-222-1.0.log
print sys.argv[1]
print sys.argv[2]
csvFileName=sys.argv[1]
outDir = sys.argv[2]

d = pd.read_csv(csvFileName, engine='python', header=None);
# d = d.ix[1:]  # delete the first dummy row

# anshuStormSCsup1,Thread-5-spout,spout,1460404079568,MSGID,1217000000010
if(len(re.findall('spout', csvFileName)) == 1):
       my_columns = ["hostname","thread","component","timestamp","type","id"]
       fileIdentifier = csvFileName.split('/')[-1][:-4]
elif(len(re.findall('sink', csvFileName)) == 1):
       my_columns = ["hostname","thread","component","timestamp","id"]
       fileIdentifier = csvFileName.split('/')[-1][:-4]


#my_columns=["id","timestamp","value","property","plug_id","household_id","house_id"]
d.columns = my_columns

d['ts'] = d['timestamp']
###d = d.sort('ts')

mints = min(d.ts)
maxts = max(d.ts)
d['rt'] = (d.ts-mints)  # Relative Time

# bin_size = 3600000   # in milli secs
bin_size = 1000
bins_seq = list()
bins_seq.append(-1)
for j in xrange(0, (maxts-mints), bin_size):
    bins_seq.append(j)

bins_seq.append(j+bin_size)
d['bucket'] = pd.cut(d['rt'], bins_seq)
#ans = d.groupby('bucket', sort=False).count('rt').rt
ans = d.groupby('bucket', sort=True).count('rt').rt

bucketIndex = ans.index
upperIndex= [float(re.split(", |\]|\(", x)[-2]) for x in bucketIndex]
ans.index = upperIndex
ans.to_csv(outDir + '/T-' + fileIdentifier + '.dat')
