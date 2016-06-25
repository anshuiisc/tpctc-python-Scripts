#!/usr/bin/env bash


expid="2126000"

/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudreamd2.cloudapp.net 22"  anshu@anshudreamd2.cloudapp.net:/home/anshu/data/storm/output/iotbm-app/*-*-$expid*   /Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/log

#/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshudreamd.cloudapp.net 22"  anshu@anshudreamd.cloudapp.net:/home/anshu/data/storm/output/tableLog/*-*-$expid*   /Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/log

#/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshustormscsup3d1.cloudapp.net 22"  anshu@anshustormscsup3d1.cloudapp.net:/home/anshu/data/storm/output/BlobUpload/*-BloomFilterCheck-PLUG*-$expid*   /Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/log
#/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshustormscsup4d1.cloudapp.net 22"  anshu@anshustormscsup4d1.cloudapp.net:/home/anshu/data/storm/output/BlobUpload/*-BloomFilterCheck-PLUG*-$expid*   /Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/log

#/usr/local/bin/sshpass -p dream@119  scp -o "ProxyCommand /usr/local/bin/corkscrew proxy.iisc.ernet.in 3128 anshustormscsup2d1.cloudapp.net 22"  anshu@anshustormscsup2d1.cloudapp.net:/home/anshu/toplogFinalSC/toplogBlobUpload/cpuBloomFilterCheck*-$expid*  /Users/anshushukla/PycharmProjects/tpctc/FullpaperPlots/log1/cpu




