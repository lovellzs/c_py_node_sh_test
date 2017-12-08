#include <stdio.h>

void shuchu(void); //声明一个函数

int main()
{
	int num;
	num = 1;

	printf("Hello World !\n"); //这是注释 C99注释

	shuchu();

	return 0;
}

void shuchu(void)
{

	printf("我是 func shuchu");
	return;
}