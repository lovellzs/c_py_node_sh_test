#include <stdio.h>
int func(int a,int b)
{
	int c;
	c=a+b;
	return c;
}
int main(void)
{
	int x=6,r;
	r=func(x,x+=2);
	printf("%d\n",r);
	return 0;
}