#!/bin/sh

a=0
GIT=`which git`
echo Commit message:
read message
while [ $a -lt 10 ]
do
	ls -l
	touch test.txt
	echo File Created
	${GIT} add --all .
	${GIT} commit -m "$message"
	${GIT} push
	
	rm -f test.txt
	echo File Deleted
	ls -l
    a=`expr $a + 1`
	echo $a
	sleep 10
done
