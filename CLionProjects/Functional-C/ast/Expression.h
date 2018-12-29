//
// Created by solly on 8/7/18.
//

#ifndef FUNCTIONAL_C_EXPRESSION_H
#define FUNCTIONAL_C_EXPRESSION_H

#include "Node.h"

template<typename T>
class Expression : Node<T> {
		T run() override = 0;
};


#endif //FUNCTIONAL_C_EXPRESSION_H
