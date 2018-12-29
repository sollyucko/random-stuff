cmake_minimum_required(VERSION 3.12)
project(Functional_C)

set(CMAKE_CXX_STANDARD 17)

find_package(BISON)
find_package(FLEX)

BISON_TARGET(Parser parser.bison ${CMAKE_CURRENT_BINARY_DIR}/parser.cpp
        DEFINES_FILE "${CMAKE_CURRENT_SOURCE_DIR}/out/cc.tab.h"
        )
FLEX_TARGET(Lexer lexer.flex ${CMAKE_CURRENT_BINARY_DIR}/lexer.cpp)
ADD_FLEX_BISON_DEPENDENCY(Lexer Parser)

include_directories(${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/out ${CMAKE_CURRENT_SOURCE_DIR}/ast)

add_executable(Functional_C
        ${BISON_Parser_OUTPUTS}
        ${FLEX_Lexer_OUTPUTS}
        ast/AdditionExpression.h ast/Block.cpp ast/Block.h ast/Expression.h
        ast/Node.h ast/Program.cpp ast/Program.h ast/Statement.h main.cpp)
