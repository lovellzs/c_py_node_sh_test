#include <stdio.h>

struct stuff{  
        char job[20];  
        int age;  
        float height;  
};  

int main()  
{  
        struct stuff Huqinwei;  
  
        struct stuff &ref = Huqinwei;  
        ref.age = 100;  
        printf("Huqinwei.age is %d\n",Huqinwei.age);  
        printf("ref.age is %d\n",ref.age);  
  
        struct stuff *ptr = &Huqinwei;  
        ptr->age = 200;  
        printf("Huqinwei.age is %d\n",Huqinwei.age);  
        printf("ptr->age is %d\n",Huqinwei.age);  
//既然都写了，把指针引用也加上吧  
        struct stuff *&refToPtr = ptr;  
        refToPtr->age = 300;  
        printf("Huqinwei.age is %d\n",Huqinwei.age);  
        printf("refToPtr->age is %d\n",refToPtr->age);  
  
  
} 