//
// Created by solly on 8/6/18.
//

#ifndef FUNCTIONAL_C_PROGRAM_H
#define FUNCTIONAL_C_PROGRAM_H


#include <list>
#include "Statement.h"
#include "Block.h"
#include "Node.h"

class Program : public Node<void> {
	public:
		Block block;

		void run() override;
};


#endif //FUNCTIONAL_C_PROGRAM_H
