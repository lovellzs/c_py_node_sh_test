#include <iostream>
using namespace std;
enum time 
{ 
    first,second,
    third,forth,fifth
};

int main()
{
    enum time a=fifth;
    if (a==fifth) 
    {
        cout << a << endl;
    }
    return 0;
}