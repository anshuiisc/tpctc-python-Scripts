#!/bin/bash

expNum=$1

#files="/Users/anshushukla/PycharmProjects/DataAnlytics1/Storm-Scheduler-SC-scripts/data/Rstorm/log/18777"
#internalFiles="/Users/anshushukla/PycharmProjects/DataAnlytics1/Storm-Scheduler-SC-scripts/data/Rstorm/dat"

#files="/Users/anshushukla/PycharmProjects/DataAnlytics1/Storm-Scheduler-SC-scripts/data/default/log/14777"
#internalFiles="/Users/anshushukla/PycharmProjects/DataAnlytics1/Storm-Scheduler-SC-scripts/data/default/dat"

#files="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/floatpi/log1/log"
#internalFiles="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/floatpi/log1/dat"
#
#
#files="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/AzureTable/log1/log"
#internalFiles="/Users/anshushukla/PycharmProjects/DataAnlytics1/scheduler/AzureTable/log1/dat"


files="/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/log"
internalFiles="/Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/dat"

#T-sink-IdentityTopologyTable-PLUG-271111-3.33.dat
expNum=12211003

for i in `ls $files/spout*$expNum*log`
do
  echo "Processing File $i"

echo   ./thruput.py $i $internalFiles
  ./thruput.py $i $internalFiles
done

for i in `ls $files/sink*$expNum*log`
do
  echo "Processing File $i"
  ./thruput.py $i $internalFiles
done

