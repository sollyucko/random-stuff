# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.13

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/solly/.local/share/JetBrains/Toolbox/apps/CLion/ch-0/183.4588.63/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/solly/.local/share/JetBrains/Toolbox/apps/CLion/ch-0/183.4588.63/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/solly/CLionProjects/IDE

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/solly/CLionProjects/IDE/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/IDE.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/IDE.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/IDE.dir/flags.make

CMakeFiles/IDE.dir/main.cpp.o: CMakeFiles/IDE.dir/flags.make
CMakeFiles/IDE.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/solly/CLionProjects/IDE/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/IDE.dir/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/IDE.dir/main.cpp.o -c /home/solly/CLionProjects/IDE/main.cpp

CMakeFiles/IDE.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/IDE.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/solly/CLionProjects/IDE/main.cpp > CMakeFiles/IDE.dir/main.cpp.i

CMakeFiles/IDE.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/IDE.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/solly/CLionProjects/IDE/main.cpp -o CMakeFiles/IDE.dir/main.cpp.s

# Object files for target IDE
IDE_OBJECTS = \
"CMakeFiles/IDE.dir/main.cpp.o"

# External object files for target IDE
IDE_EXTERNAL_OBJECTS =

IDE: CMakeFiles/IDE.dir/main.cpp.o
IDE: CMakeFiles/IDE.dir/build.make
IDE: CMakeFiles/IDE.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/solly/CLionProjects/IDE/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable IDE"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/IDE.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/IDE.dir/build: IDE

.PHONY : CMakeFiles/IDE.dir/build

CMakeFiles/IDE.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/IDE.dir/cmake_clean.cmake
.PHONY : CMakeFiles/IDE.dir/clean

CMakeFiles/IDE.dir/depend:
	cd /home/solly/CLionProjects/IDE/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/solly/CLionProjects/IDE /home/solly/CLionProjects/IDE /home/solly/CLionProjects/IDE/cmake-build-debug /home/solly/CLionProjects/IDE/cmake-build-debug /home/solly/CLionProjects/IDE/cmake-build-debug/CMakeFiles/IDE.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/IDE.dir/depend

