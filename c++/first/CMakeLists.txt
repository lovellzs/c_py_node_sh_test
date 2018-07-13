cmake_minimum_required(VERSION 3.9)
project(first)

set(CMAKE_CXX_STANDARD 11)

add_executable(first main.cpp myconst/pre.cpp test1/func.h test1/func.cpp test1/func1.cpp test1/func1.h)