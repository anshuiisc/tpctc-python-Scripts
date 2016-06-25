#!/bin/bash

expNum=$1

#files="/data/tetc/tetc-final/dataset/RECEIVED/$expNum/"
#internalFiles="/Users/anshushukla/PycharmProjects/DataAnlytics1/Storm-Scheduler-SC-scripts/data/Rstorm/dat/"
#dest="/Users/anshushukla/PycharmProjects/DataAnlytics1/Storm-Scheduler-SC-scripts/data/Rstorm/plot/"
#
#internalFiles="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/floatpi/log1/dat/"
#dest="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/floatpi/log1/plot/"
#
#internalFiles="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/AzureTable/log1/dat/"
#dest="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/AzureTable/log1/plot/"

internalFiles="/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/dat/"
dest="/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/plot/"



for i in `ls $internalFiles/T-spout*6211211000*.dat`
do
echo ./plotThroughput.py $i $internalFiles
#  ./plotThroughput.py $i $internalFiles
#python /Users/anshushukla/PycharmProjects/DataAnlytics1/Storm-Scheduler-SC-scripts/resultgenScripts/plotThroughput.py    $i $dest

python  /Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/script/plotThroughput.py    $i $dest
#python  /Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/script/plotThroughput-scatter.py    $i   $dest

#  break
done


