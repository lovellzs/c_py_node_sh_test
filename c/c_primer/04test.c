#include <stdio.h> 


int main (void){
	int ten = 10; int tow = 2;
	printf("Doing it right:");
	printf("%d minus %d is %d\n",ten,2,ten-tow); 
	printf("Doing it wrong:");
	printf("%d minus %d is %d\n",ten); //忘掉二个参数
	getchar();
	return 0;
}