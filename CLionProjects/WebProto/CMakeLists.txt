cmake_minimum_required(VERSION 3.12)
project(Web-Protocol)

set(CMAKE_CXX_STANDARD 17)

add_library(Web-Protocol SHARED library.cpp library.h)
add_executable(Web-Protocol-Demo demo.cpp)
target_link_libraries(Web-Protocol-Demo Web-Protocol)