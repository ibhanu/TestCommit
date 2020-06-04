#!/bin/sh

a=0
GIT=`which git`
#message = "File Changed"
while [ $a -lt 10 ]
do
	touch test.txt
	${GIT} add --all .
	${GIT} commit -m "File Changed at $(date)"
	${GIT} push
	rm -f test.txt
	${GIT} add --all .
	${GIT} commit -m "File changed at $(date)"
	${GIT} push
    a=`expr $a + 2`
	echo "Pushed No: $a "
done
