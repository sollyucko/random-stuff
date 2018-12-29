//
// Created by solly on 8/6/18.
//

#ifndef FUNCTIONAL_C_BLOCK_H
#define FUNCTIONAL_C_BLOCK_H


#include <list>
#include "Statement.h"

class Block : public Node<void> {


	public:
		::std::list<Statement> statements;

		void run() override;
};


#endif //FUNCTIONAL_C_BLOCK_H
