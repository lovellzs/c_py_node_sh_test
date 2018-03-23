#include <iostream>
#include "func.h"

using namespace std;
int main()
{
    cout << "Hello, world!" << endl;

    for(int i = 0;i<10;i++){
    		cout << "Hello, world!" << i << endl;
    }
	
	cout << "Hello, world!" <<  getAge() << endl;

    return 0;
}
