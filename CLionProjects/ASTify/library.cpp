#include "library.h"

#include <iostream>

::std::string get_greeting() {
	return "Hello, World!";
}

void greet() {
	std::cout << get_greeting() << std::endl;
}