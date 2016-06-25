#!/bin/bash

expNum=$1

#file_src="/data/tetc/tetc-final/dataset/RECEIVED/$expNum"
#file_dest="/data/tetc/tetc-final/dataset/RECEIVED/$expNum"

file_src="/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/log"
file_dest="/Users/anshushukla/PycharmProjects/tpctc/apps-STATS/log1/log"





for i in $(ls  $file_src/spout*-22146000-0.001*)


	do
     	echo  initial string $i
	

	original_string=$i
	string_to_replace=.log
	result_string="${original_string/.log*/$string_to_replace}"
	echo  result string   $result_string
	
	cat  $original_string >> $result_string
	head -20  $original_string
	echo  "updated file" 
	head -20  $result_string	

	#sort -k1,1nr -k2,2 inputfile
	#$i>>temp.txt
	#echo  $(sed -i -e 's/*.log/*.logx/g' $i	)
	#	echo ${i::-4}
	done


exit()

for i in $(ls  $file_src/node*.log)


        do
        echo  initial string $i


        original_string=$i
        #string_to_replace=.log
        result_string="${original_string/node*-sink-/sink-}"
        echo  result string   $result_string

        cat  $original_string >> $result_string
        head -20  $original_string
        echo  "updated file"
        head -20  $result_string

        #sort -k1,1nr -k2,2 inputfile
        #$i>>temp.txt
        #echo  $(sed -i -e 's/*.log/*.logx/g' $i        )
        #       echo ${i::-4}
        done



#cp $file_src $file_dest

#ls   /data/tetc/tetc-final/dataset/RECEIVED/$expNum/skew*csv > $file_dest/skewFileNames.txt

#/data/tetc/tetc-final/dataset/RECEIVED/29
# ls /data/tetc/tetc-final/scripts/skew*csv > $file_dest/skewFileNames.txt

#sed -i '1,$s/\/.*\///g'  $file_dest/skewFileNames.txt
