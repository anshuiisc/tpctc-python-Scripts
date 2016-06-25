#!/bin/bash
sleep 20
filename=$1
#echo $filename
count=$2
#print $count
#while [ 0 ]
#do
    top -b -n $count  -d 2 >>/home/anshu/toplogFinalSC/toplogBlobUpload/$filename
#done