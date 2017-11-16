#!/bin/bash
#test read

#read -p "Please enter two number: " first next
#echo the sum is $[ $first + $next ]


#test timing the data entry
:<<BLOCK
if read -t 5 -p "Please enter your name: " name
then
	echo "Hello $name, welcome to my script"
else
	echo
	echo "Sorry, too slow!"
fi
BLOCK

#test number limit   
#-n1 means the same line and own letter
#
read -s -n1 -p "Do you want to continue [Y/N]?" answer
case $answer in
	Y | y)echo
		echo "fine,continue on...";;
	N | n)echo
		echo OK,goodbye
		exit;;
esac
echo "This is the end of the script"












