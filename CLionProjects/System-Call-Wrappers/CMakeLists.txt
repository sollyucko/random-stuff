cmake_minimum_required(VERSION 3.12)
project(System-Call-Wrappers)

set(CMAKE_CXX_STANDARD 17)
set(SCW_SHARED_FILES syscalls.cpp syscalls.hpp)

if(${WINDOWS})
    add_library(System-Call-Wrappers SHARED ${SCW_SHARED_FILES} syscalls_windows.cpp)
elseif(${UNIX})
    add_library(System-Call-Wrappers SHARED ${SCW_SHARED_FILES} syscalls_unix.cpp)
endif()