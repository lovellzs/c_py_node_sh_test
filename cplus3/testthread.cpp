
#include <iostream>
#include <future>
#include "testthread_new.h"

using namespace std;

void test_thread(){
    std::future<int> f1 = std::async(std::launch::async, [](){
        return 8;
    });

    cout << f1.get() << endl; //output: 8

    std::future<void> f2 = std::async(std::launch::async, [](){
        cout << 8 << endl;
        //return 8;
    });

    f2.wait(); //output: 8

    std::future<int> future = std::async(std::launch::async, [](){
        std::this_thread::sleep_for(std::chrono::seconds(3));
        return 8;
    });

    std::cout << "waiting...\n";
    
    //Test12();
    std::future_status status;
//    Sleep(3000);
    std::this_thread::sleep_for(std::chrono::seconds(3));
    
    do {
        status = future.wait_for(std::chrono::seconds(1));
        if (status == std::future_status::deferred) {
            std::cout << "deferred\n";
        }
        else if (status == std::future_status::timeout) {
            std::cout << "timeout\n";
        }
        else if (status == std::future_status::ready) {
            std::cout << "ready!\n";
        }
    } while (status != std::future_status::ready);

    std::cout << "result is " << future.get() << '\n';
}


void test_thread_for(){
    std::future<int> future = std::async(std::launch::async, [](int tid){
        
        for(int i = 0;i<10;i++){
            std::cout << tid <<"future" << i << std::endl;
            std::this_thread::sleep_for(std::chrono::seconds(1));
            if( i==9 ){
                return i;
            }
        }
    },0);
    
//    std::future_status status;
//    do {
//        status = future.wait_for(std::chrono::seconds(0));
//        if (status == std::future_status::deferred) {
////            std::cout << "deferred\n";
//        }
//        else if (status == std::future_status::timeout) {
////            std::cout << "timeout\n";
//        }
//        else if (status == std::future_status::ready) {
//            std::cout << "ready!\n";
//        }
//    } while (status != std::future_status::ready);
//    
    std::cout << "future result is " << future.get() << '\n';
}

void test_more_threads(){
    
//    for(int tid = 0 ;tid<3;tid++){
//        std::future<int> future = std::async(std::launch::async, [](int tid){
//
//            for(int i = 0;i<10;i++){
//                std::cout << tid <<"future" << i << std::endl;
//                std::this_thread::sleep_for(std::chrono::seconds(1));
//                if( i==9 ){
//                    return i;
//                }
//            }
//        },tid);
//    }
    
    std::future<int> future1 = std::async(std::launch::async, [](int tid){

            for(int i = 0;i<10;i++){
                std::cout << tid <<"future" << i << std::endl;
                std::this_thread::sleep_for(std::chrono::seconds(1));
                if( i==9 ){
                    return i;
                }
            }
        },0);
        
        std::future<int> future2 = std::async(std::launch::async, [](int tid){

            for(int j = 0;j<10;j++){
                std::cout << tid <<"future" << j << std::endl;
                std::this_thread::sleep_for(std::chrono::seconds(1));
                if( j==9 ){
                    return j;
                }
            }
        },1);
        
        std::future<int> future3 = std::async(std::launch::async, [](int tid){

            for(int m = 0;m<10;m++){
                std::cout << tid <<"future" << m << std::endl;
                std::this_thread::sleep_for(std::chrono::seconds(1));
                if( m==9 ){
                    return m;
                }
            }
        },2);
}