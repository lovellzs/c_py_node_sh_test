#include <stdio.h>
#include <strings.h>

struct Person
{
	char name[8];
	int age;
};

int main(void)
{
	
	struct Person p1 = 
	{
		"hello",18
	};

	struct Person p2 = 
	{
		"hello",18
	};

	struct Person *p3 = &p2;
	// struct Person *p3 ;

	printf("age = %d \n", p1.age );


	printf("p1 = %p\n",p1);
	printf("&p1 = %p\n",&p1);
	printf("p1.name = %p\n",p1.name);
	printf("======================\n");
	printf("p2 = %p\n",p2);
	printf("&p2 = %p\n",&p2);
	printf("p2.name = %p\n",p2.name);
	printf("======================\n");
	printf("（*3） = %p\n",(*p3) );
	printf("p3 = %p\n",p3);
	printf("p3.name = %p\n",&(*p3).name);

	printf("======================\n");
	// // strcpy(p2.name ,"aaaaa");
	// strcpy(&p2.name[0] ,"aaaaa");
	// strcpy(p3->name ,"aaaaa");
	p3->age = 11;

	++p3->name ;
	printf("p3.name = %c\n", * (p3->name) );
	printf("p3.name = %d\n",p3->age);
	printf("p3.name = %d\n",  p3->age );
	return 0;
}

