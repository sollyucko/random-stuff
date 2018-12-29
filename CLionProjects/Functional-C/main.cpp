//
// Created by solly on 8/7/18.
//

#include "AdditionExpression.h"
#include "Program.h"

int main(int argc, char** argv) {
    Program program;
    AdditionExpression expression;
    program.block.statements.push_front(expression);
}