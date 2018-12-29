%{
#include <iostream>

extern int yylex();
extern int yyparse();
extern FILE* yyin;

void yyerror(const char* message);
%}

%union {
    int int_value;
    float float_value;
    char* string_value;
}

%token <integer_value> INTEGER
%token <float_value> DECIMAL
%token <string_value> STRING
%token <string_value> IDENTIFIER

%%

program:
    program statement   {  }
    | statement         {  }

%%

int main(int argc, char** argv) {
    if(argc > 1) {
        FILE *file = fopen(argv[1], "r");

        if(!file) {
            ::std::cerr << "Can't open file " << argv[1] << ::std::endl;
            return 1;
        }

        yyin = file;
    }

    yyparse();
}

void yyerror(const char* message) {
    ::std::cout << "Parse error! Message: " << message << ::std::endl;
}