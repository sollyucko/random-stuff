//
// Created by solly on 8/6/18.
//

#include "Block.h"

void Block::run() {
	for_each(this->statements.begin(), this->statements.end(), [](Statement &statement) { statement.run(); });
}
