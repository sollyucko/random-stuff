#include "syscalls.hpp"

#include <iostream>

#ifdef __unix__
	#include "syscalls_unix.cpp"
#elif defined(_WIN32) || defined(WIN32)
	#include "syscalls_windows.cpp"
#endif