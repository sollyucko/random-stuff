cmake_minimum_required(VERSION 3.12)
project(ASTify)

set(CMAKE_CXX_STANDARD 17)

add_library(ASTify SHARED library.cpp library.h)

ADD_SUBDIRECTORY(test/1)
ADD_SUBDIRECTORY(test/2)