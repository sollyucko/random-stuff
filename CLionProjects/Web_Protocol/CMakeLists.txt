cmake_minimum_required(VERSION 3.12)
project(Web_Protocol)

set(CMAKE_CXX_STANDARD 17)

add_library(Web_Protocol SHARED library.cpp library.h)
add_executable(Web_Protocol_Demo demo.cpp)
target_link_libraries(Web_Protocol_Demo Web_Protocol)