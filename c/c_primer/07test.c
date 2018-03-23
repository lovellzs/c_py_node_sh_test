#include<stdio.h>


const int aaaaa = 1000;

int test(){
	const int aaaaa = 100;
	return aaaaa;
}

int test1(){
	// char a[] = "qqqqq";
	// a[2] = 'b';

	char *a = "qqqqq";
	*(a+1) = 'c';
	printf("%s\n", a);

	return 0;
}

int test2(){
	// const char b[] = "aaaaa";
	// // b[1] = 'q';
	// char *p = b;
	// *(p+1) = 'b';
	// printf("%s\n", p);

	return 0;
}



int main(void)
{
	test1();


	char a[] = "aaaaa";
	a[1] = 'q';
	printf("%s\n", a);

	// test2();

	const int aa = 1;
	int *ap = (int *)&aa;
	*ap = 10;
	printf("%d\n", *ap);


	int  ccccc = test();
	ccccc = 33;
	printf("%d\n", ccccc );
	printf("%d\n", test() );

	printf("%d\n", aaaaa );
	
	return 0;
}