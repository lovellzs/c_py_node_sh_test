#include <iostream>

#include "myconst/pre.cpp"

#include "test1/func1.h"
#include "test1/func.h"

int main() {
    std::cout << "Hello, World!" << std::endl;

    std::cout << AGE * NUM << std::endl;

    std::cout << add( AGE , NUM ) << std::endl;
    std::cout << getDDD() << std::endl;
    std::cout << DDD1 << std::endl;
    return 0;
}
