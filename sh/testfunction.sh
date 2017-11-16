#!/bin/bash
#test function

:<<BLOCK
#这种方法内部不能有local 变量
function echoName {
	echo $USER
}

#建议使用这种写法 内部可以使用local变量
echoAge() {
	echo I\'m 16 years old
}

echoName
echoAge
BLOCK

if false ;then 
db1(){
	read -p "Enter a number: " value
   echo $[ $value * 2 ]
}

#result=`db1`
echo "The new value is $result"
fi

add(){
	if [ $# -eq 2 ]
	then
		echo $[ $1 + $2 ]	
	fi
}

echo -n "Add 10 + 20 = "
value=`add 10 20`
echo $value


