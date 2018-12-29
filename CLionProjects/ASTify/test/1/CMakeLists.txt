cmake_minimum_required(VERSION 3.12)
project(ASTify)

set(CMAKE_CXX_STANDARD 17)

add_executable(TEST_1
        ../../library.cpp ../../library.h
        main.cpp)