#include <stdio.h> 

int main (void)
{
	int x = 100;
	printf ("dec = %d; octal=%o; hex=%x\n",x,x,x); //dec 十进制，octal 八进制， hec  十六进制
	printf ("dec = %d; octal=%#o; hex=%#x\n",x,x,x); 
	getchar();
	return 0;
}