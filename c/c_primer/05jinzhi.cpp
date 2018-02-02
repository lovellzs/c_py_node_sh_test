#include <stdio.h> 

int main (void)
{
	int x = 100;
	printf ("dec = %d; octal=%o; hex=%x\n",x,x,x); //dec 十进制，octal 八进制， hec  十六进制
	printf ("dec = %d; octal=%#o; hex=%#x\n",x,x,x); 

	int a = 0x20;

	printf("a = %#x\n", a);
		a=020;
	printf("a = %#o\n", a);

	a=-11;
	printf("%x\n", a);
	printf("%d\n", a);
	getchar();
	return 0;
}