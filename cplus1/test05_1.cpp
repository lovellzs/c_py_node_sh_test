#include <iostream>


int count = 6;
extern void write_extern();
 
int main()
{
   count = 5;
   write_extern();
}