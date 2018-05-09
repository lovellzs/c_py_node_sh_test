# include <iostream>
#include "test_future.h"
#include "testthread_new.h"

int64_t getTime(){
    int64_t now_time = time(nullptr);
    return now_time;
}

int main ()
{
//    test_future();
    
//    test_thread();
//    test_thread_for();

//    test_more_threads();
    
  std::cout << getTime() << std::endl;
    
  return 0;
}
