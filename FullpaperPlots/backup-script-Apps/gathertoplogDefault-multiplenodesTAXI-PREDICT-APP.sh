#!/usr/bin/env bash

file_serverinfo=/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/script/PrivateIPs.txt

#file_outputcommands=usefulcommands.txt

#file_pem=/home/ubuntu/anshu.pem

expNum=22136000
#expNum=$1


for i in `cat $file_serverinfo`
do



path_dest="/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/cpu/$expNum/$i"
#path_src=

mkdir -p "$path_dest"
	printf " sshpass -p dream@119 scp -r  -o \"ProxyCommand corkscrew proxy.iisc.ernet.in 3128  $i  22\"  anshu@$i:/home/anshu/toplogFinalSC/toplogFloatPI/cpuRstorm-$expNum*  $path_dest/$i-logFileWorkerTOP.txt "


/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128  $i 22"  anshu@$i:/home/anshu/toplogFinalSC/toplogBlobUpload/cpuIoTPredictionTopologyTAXI-$expNum*  $path_dest
#sshpass -p dream@119  scp -o "ProxyCommand corkscrew proxy.iisc.ernet.in 3128  $i 22"  anshu@$i:/home/anshu/toplogFinalSC/toplogFloatPI/cpuRstorm-$expNum*  $path_dest/$i-logFileWorkerTOP.txt

done
echo DONE

#echo "url1=http://`sed -n '1p' $file_serverinfo`:8080/cloud9-project0-web/echoweb" >> $file_outputcommands
#echo "url2=http://`sed -n '2p' $file_serverinfo`:8080/cloud9-project0-rest/echo" >> $file_outputcommands