#!/usr/bin/env bash


expid="22146000-0.001"


# PREDICT topo  SYS
#/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudreamd2.cloudapp.net 22"  anshu@anshudreamd2.cloudapp.net:/home/anshu/data/storm/output/iotbm-app/*-IoTPredictionTopologySYS-SYS*-$expid*   /Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/log


# PREDICT topo  TAXI
/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudreamd2.cloudapp.net 22"  anshu@anshudreamd2.cloudapp.net:/home/anshu/data/storm/output/iotbm-app/*-IoTPredictionTopologyTAXI-TAXI*-$expid*   /Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/log







#/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshustormscsup3d1.cloudapp.net 22"  anshu@anshustormscsup3d1.cloudapp.net:/home/anshu/data/storm/output/BlobUpload/*-SimpleLinearRegressionPredictor-PLUG*-$expid*   /Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/log
#/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshustormscsup4d1.cloudapp.net 22"  anshu@anshustormscsup4d1.cloudapp.net:/home/anshu/data/storm/output/BlobUpload/*-SimpleLinearRegressionPredictor-PLUG*-$expid*   /Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/log
#
#/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshustormscsup2d1.cloudapp.net 22"  anshu@anshustormscsup2d1.cloudapp.net:/home/anshu/toplogFinalSC/toplogBlobUpload/cpuSimpleLinearRegressionPredictor*-$expid*  /Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/cpu




#/usr/local/bin/sshpass -p dream@119  scp -r -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshustormscsup2d1.cloudapp.net 22"  anshu@anshustormscsup2d1.cloudapp.net:/home/anshu/storm/apache-storm-1.0.1/logs/workers-artifacts/IoTStatsTopology-26-1465851601/6723/worker.log.out  /Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/erroe

