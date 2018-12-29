//
// Created by solly on 8/7/18.
//

#ifndef FUNCTIONAL_C_ADDITIONEXPRESSION_H
#define FUNCTIONAL_C_ADDITIONEXPRESSION_H


#include "Expression.h"

template<typename A, typename B, typename C>
class AdditionExpression : Expression<C> {
	public:
		A a;
		B b;

		C run() {
			return this->a + this->b;
		}
};


#endif //FUNCTIONAL_C_ADDITIONEXPRESSION_H
