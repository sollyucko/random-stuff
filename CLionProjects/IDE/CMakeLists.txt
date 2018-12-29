cmake_minimum_required(VERSION 3.13)
project(IDE)

set(CMAKE_CXX_STANDARD 17)

if(MSCV)
    add_compile_options(/W4)
else(MSVC)
    add_compile_options(-Wall -Wextra -pedantic)
endif(MSVC)

set(wxWidgets_ROOT_DIR </usr/include/wx-3.0-unofficial>)
set(wxWidgets_CONFIGURATION mswu)
find_package(wxWidgets COMPONENTS core base REQUIRED)
include(${wxWidgets_USE_FILE})

set(SOURCE_FILES main.cpp)
add_executable(IDE main.cpp)

target_link_libraries(IDE ${wxWidgets_LIBRARIES})
