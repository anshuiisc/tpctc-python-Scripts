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


files="/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/log"
internalFiles="/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/dat"




for i in `ls $files/spout*22116000-0.001*log`
do
  echo "Processing File $i"

echo   ./thruput.py $i $internalFiles
  ./thruput.py $i $internalFiles
done

for i in `ls $files/sink*22116000-0.001*log`
do
  echo "Processing File $i"
  ./thruput.py $i $internalFiles
done

