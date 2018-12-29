%{
#include <cstdio>
#include "cc.tab.h"
%}

%option noyywrap

%%
[ \t\n]         ;
[0-9]+\.[0-9]+  { yylval.float_value = ::std::atof(yytext); return DECIMAL; }
[0-9]+          { yylval.integer_value = ::std::atoi(yytext); return INTEGER; }
[a-zA-Z0-9]+    { yylval.string_value = strdup(yytext); return IDENTIFIER; }
%%