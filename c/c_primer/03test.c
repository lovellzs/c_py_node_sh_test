#include <stdio.h> 


int main (void){
	float weight; //用户的体重
	float value; //相等重量体重的价值
	printf (" Are you worth your weight in rhodium?\n"); 
	printf ("Let's check it out.\n");
	printf ("Please enter your weight in pounds: ");


	scanf ("%f",&weight); // 仅用户处获取输入 此处为返个示例的关键处
	/* 假设铑为每盎司 770 美元， 14.5833 抂常衡制的英镑转换为金衡制盎司 */ 
	value = 770 * weight * 14.5833;
	printf ("your weight in rhodium is $%.2f.\n",value); //$%.2f 看仇绅返个输出参数
	printf ("You are easily worth that! If rhodium prices drop,\n"); 
	printf ("eat more to maintain your value.\n");

	getchar();
	getchar();
	return 0; 
}