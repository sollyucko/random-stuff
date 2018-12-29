// This is a generated file. Not intended for manual editing.
package io.github.sollyucko.coconut_plugin.parser;

import com.intellij.lang.PsiBuilder;
import com.intellij.lang.PsiBuilder.Marker;
import static io.github.sollyucko.coconut_plugin.psi.CoconutTypes.*;
import static io.github.sollyucko.coconut_plugin.ParserUtil.*;
import com.intellij.psi.tree.IElementType;
import com.intellij.lang.ASTNode;
import com.intellij.psi.tree.TokenSet;
import com.intellij.lang.PsiParser;
import com.intellij.lang.LightPsiParser;

@SuppressWarnings({"SimplifiableIfStatement", "UnusedAssignment"})
public class CoconutParser implements PsiParser, LightPsiParser {

  public ASTNode parse(IElementType t, PsiBuilder b) {
    parseLight(t, b);
    return b.getTreeBuilt();
  }

  public void parseLight(IElementType t, PsiBuilder b) {
    boolean r;
    b = adapt_builder_(t, b, this, null);
    Marker m = enter_section_(b, 0, _COLLAPSE_, null);
    if (t == BINARY_DIGIT) {
      r = binary_digit(b, 0);
    }
    else if (t == BINARY_INTEGER) {
      r = binary_integer(b, 0);
    }
    else if (t == DECIMAL_INTEGER) {
      r = decimal_integer(b, 0);
    }
    else if (t == DECIMAL_REAL) {
      r = decimal_real(b, 0);
    }
    else if (t == DIGIT) {
      r = digit(b, 0);
    }
    else if (t == EXPRESSION) {
      r = expression(b, 0);
    }
    else if (t == HEXADECIMAL_DIGIT) {
      r = hexadecimal_digit(b, 0);
    }
    else if (t == HEXADECIMAL_INTEGER) {
      r = hexadecimal_integer(b, 0);
    }
    else if (t == IDENTIFIER) {
      r = identifier(b, 0);
    }
    else if (t == IMAGINARY_NUMBER) {
      r = imaginary_number(b, 0);
    }
    else if (t == INTEGER) {
      r = integer(b, 0);
    }
    else if (t == LINE) {
      r = line(b, 0);
    }
    else if (t == LITERAL) {
      r = literal(b, 0);
    }
    else if (t == NON_INTEGER_REAL_NUMBER) {
      r = non_integer_real_number(b, 0);
    }
    else if (t == NONZERO_DIGIT) {
      r = nonzero_digit(b, 0);
    }
    else if (t == NUMBER) {
      r = number(b, 0);
    }
    else if (t == OCTAL_DIGIT) {
      r = octal_digit(b, 0);
    }
    else if (t == OCTAL_INTEGER) {
      r = octal_integer(b, 0);
    }
    else if (t == REAL_NUMBER) {
      r = real_number(b, 0);
    }
    else if (t == SCIENTIFIC_REAL) {
      r = scientific_real(b, 0);
    }
    else if (t == SIMPLE_INTEGER) {
      r = simple_integer(b, 0);
    }
    else if (t == STATEMENT) {
      r = statement(b, 0);
    }
    else if (t == STRING) {
      r = string(b, 0);
    }
    else {
      r = parse_root_(t, b, 0);
    }
    exit_section_(b, 0, m, t, r, true, TRUE_CONDITION);
  }

  protected boolean parse_root_(IElementType t, PsiBuilder b, int l) {
    return file(b, l + 1);
  }

  /* ********************************************************** */
  // "0" | "1"
  public static boolean binary_digit(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "binary_digit")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, BINARY_DIGIT, "<binary digit>");
    r = consumeToken(b, "0");
    if (!r) r = consumeToken(b, "1");
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  /* ********************************************************** */
  // "0" ("b" | "B") (["_"] binary_digit)+
  public static boolean binary_integer(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "binary_integer")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, BINARY_INTEGER, "<binary integer>");
    r = consumeToken(b, "0");
    r = r && binary_integer_1(b, l + 1);
    r = r && binary_integer_2(b, l + 1);
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  // "b" | "B"
  private static boolean binary_integer_1(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "binary_integer_1")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = consumeToken(b, "b");
    if (!r) r = consumeToken(b, "B");
    exit_section_(b, m, null, r);
    return r;
  }

  // (["_"] binary_digit)+
  private static boolean binary_integer_2(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "binary_integer_2")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = binary_integer_2_0(b, l + 1);
    while (r) {
      int c = current_position_(b);
      if (!binary_integer_2_0(b, l + 1)) break;
      if (!empty_element_parsed_guard_(b, "binary_integer_2", c)) break;
    }
    exit_section_(b, m, null, r);
    return r;
  }

  // ["_"] binary_digit
  private static boolean binary_integer_2_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "binary_integer_2_0")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = binary_integer_2_0_0(b, l + 1);
    r = r && binary_digit(b, l + 1);
    exit_section_(b, m, null, r);
    return r;
  }

  // ["_"]
  private static boolean binary_integer_2_0_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "binary_integer_2_0_0")) return false;
    consumeToken(b, "_");
    return true;
  }

  /* ********************************************************** */
  // nonzero_digit (["_"] digit)* | "0"+ (["_"] "0")*
  public static boolean decimal_integer(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "decimal_integer")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, DECIMAL_INTEGER, "<decimal integer>");
    r = decimal_integer_0(b, l + 1);
    if (!r) r = decimal_integer_1(b, l + 1);
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  // nonzero_digit (["_"] digit)*
  private static boolean decimal_integer_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "decimal_integer_0")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = nonzero_digit(b, l + 1);
    r = r && decimal_integer_0_1(b, l + 1);
    exit_section_(b, m, null, r);
    return r;
  }

  // (["_"] digit)*
  private static boolean decimal_integer_0_1(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "decimal_integer_0_1")) return false;
    while (true) {
      int c = current_position_(b);
      if (!decimal_integer_0_1_0(b, l + 1)) break;
      if (!empty_element_parsed_guard_(b, "decimal_integer_0_1", c)) break;
    }
    return true;
  }

  // ["_"] digit
  private static boolean decimal_integer_0_1_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "decimal_integer_0_1_0")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = decimal_integer_0_1_0_0(b, l + 1);
    r = r && digit(b, l + 1);
    exit_section_(b, m, null, r);
    return r;
  }

  // ["_"]
  private static boolean decimal_integer_0_1_0_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "decimal_integer_0_1_0_0")) return false;
    consumeToken(b, "_");
    return true;
  }

  // "0"+ (["_"] "0")*
  private static boolean decimal_integer_1(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "decimal_integer_1")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = decimal_integer_1_0(b, l + 1);
    r = r && decimal_integer_1_1(b, l + 1);
    exit_section_(b, m, null, r);
    return r;
  }

  // "0"+
  private static boolean decimal_integer_1_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "decimal_integer_1_0")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = consumeToken(b, "0");
    while (r) {
      int c = current_position_(b);
      if (!consumeToken(b, "0")) break;
      if (!empty_element_parsed_guard_(b, "decimal_integer_1_0", c)) break;
    }
    exit_section_(b, m, null, r);
    return r;
  }

  // (["_"] "0")*
  private static boolean decimal_integer_1_1(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "decimal_integer_1_1")) return false;
    while (true) {
      int c = current_position_(b);
      if (!decimal_integer_1_1_0(b, l + 1)) break;
      if (!empty_element_parsed_guard_(b, "decimal_integer_1_1", c)) break;
    }
    return true;
  }

  // ["_"] "0"
  private static boolean decimal_integer_1_1_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "decimal_integer_1_1_0")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = decimal_integer_1_1_0_0(b, l + 1);
    r = r && consumeToken(b, "0");
    exit_section_(b, m, null, r);
    return r;
  }

  // ["_"]
  private static boolean decimal_integer_1_1_0_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "decimal_integer_1_1_0_0")) return false;
    consumeToken(b, "_");
    return true;
  }

  /* ********************************************************** */
  // (simple_integer)? "." simple_integer | simple_integer "."
  public static boolean decimal_real(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "decimal_real")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, DECIMAL_REAL, "<decimal real>");
    r = decimal_real_0(b, l + 1);
    if (!r) r = decimal_real_1(b, l + 1);
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  // (simple_integer)? "." simple_integer
  private static boolean decimal_real_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "decimal_real_0")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = decimal_real_0_0(b, l + 1);
    r = r && consumeToken(b, ".");
    r = r && simple_integer(b, l + 1);
    exit_section_(b, m, null, r);
    return r;
  }

  // (simple_integer)?
  private static boolean decimal_real_0_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "decimal_real_0_0")) return false;
    decimal_real_0_0_0(b, l + 1);
    return true;
  }

  // (simple_integer)
  private static boolean decimal_real_0_0_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "decimal_real_0_0_0")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = simple_integer(b, l + 1);
    exit_section_(b, m, null, r);
    return r;
  }

  // simple_integer "."
  private static boolean decimal_real_1(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "decimal_real_1")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = simple_integer(b, l + 1);
    r = r && consumeToken(b, ".");
    exit_section_(b, m, null, r);
    return r;
  }

  /* ********************************************************** */
  // "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
  public static boolean digit(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "digit")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, DIGIT, "<digit>");
    r = consumeToken(b, "0");
    if (!r) r = consumeToken(b, "1");
    if (!r) r = consumeToken(b, "2");
    if (!r) r = consumeToken(b, "3");
    if (!r) r = consumeToken(b, "4");
    if (!r) r = consumeToken(b, "5");
    if (!r) r = consumeToken(b, "6");
    if (!r) r = consumeToken(b, "7");
    if (!r) r = consumeToken(b, "8");
    if (!r) r = consumeToken(b, "9");
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  /* ********************************************************** */
  // '(' expression ')' |
  //     << parseOperator operatorless_expression 'EXPRESSION'
  //         'new OperatorPrecedenceGroup(2, Associativity.RIGHT, new String[]{ "**" })'
  //         'new OperatorPrecedenceGroup(2, Associativity.LEFT,  new String[]{ "*", "/" })'
  //         'new OperatorPrecedenceGroup(2, Associativity.LEFT,  new String[]{ "+", "-" })' >>
  public static boolean expression(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "expression")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _COLLAPSE_, EXPRESSION, "<expression>");
    r = expression_0(b, l + 1);
    if (!r) r = parseOperator(b, l + 1, operatorless_expression_parser_, EXPRESSION, new OperatorPrecedenceGroup(2, Associativity.RIGHT, new String[]{ "**" }), new OperatorPrecedenceGroup(2, Associativity.LEFT,  new String[]{ "*", "/" }), new OperatorPrecedenceGroup(2, Associativity.LEFT,  new String[]{ "+", "-" }));
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  // '(' expression ')'
  private static boolean expression_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "expression_0")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = consumeToken(b, "(");
    r = r && expression(b, l + 1);
    r = r && consumeToken(b, ")");
    exit_section_(b, m, null, r);
    return r;
  }

  /* ********************************************************** */
  // line*
  static boolean file(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "file")) return false;
    while (true) {
      int c = current_position_(b);
      if (!line(b, l + 1)) break;
      if (!empty_element_parsed_guard_(b, "file", c)) break;
    }
    return true;
  }

  /* ********************************************************** */
  // "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "a" | "b" | "c" | "d" | "e" | "f" | "A" | "B" | "C" | "D" | "E" | "F"
  public static boolean hexadecimal_digit(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "hexadecimal_digit")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, HEXADECIMAL_DIGIT, "<hexadecimal digit>");
    r = consumeToken(b, "0");
    if (!r) r = consumeToken(b, "1");
    if (!r) r = consumeToken(b, "2");
    if (!r) r = consumeToken(b, "3");
    if (!r) r = consumeToken(b, "4");
    if (!r) r = consumeToken(b, "5");
    if (!r) r = consumeToken(b, "6");
    if (!r) r = consumeToken(b, "7");
    if (!r) r = consumeToken(b, "8");
    if (!r) r = consumeToken(b, "9");
    if (!r) r = consumeToken(b, "a");
    if (!r) r = consumeToken(b, "b");
    if (!r) r = consumeToken(b, "c");
    if (!r) r = consumeToken(b, "d");
    if (!r) r = consumeToken(b, "e");
    if (!r) r = consumeToken(b, "f");
    if (!r) r = consumeToken(b, "A");
    if (!r) r = consumeToken(b, "B");
    if (!r) r = consumeToken(b, "C");
    if (!r) r = consumeToken(b, "D");
    if (!r) r = consumeToken(b, "E");
    if (!r) r = consumeToken(b, "F");
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  /* ********************************************************** */
  // "0" ("x" | "X") (["_"] hexadecimal_digit)+
  public static boolean hexadecimal_integer(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "hexadecimal_integer")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, HEXADECIMAL_INTEGER, "<hexadecimal integer>");
    r = consumeToken(b, "0");
    r = r && hexadecimal_integer_1(b, l + 1);
    r = r && hexadecimal_integer_2(b, l + 1);
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  // "x" | "X"
  private static boolean hexadecimal_integer_1(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "hexadecimal_integer_1")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = consumeToken(b, "x");
    if (!r) r = consumeToken(b, "X");
    exit_section_(b, m, null, r);
    return r;
  }

  // (["_"] hexadecimal_digit)+
  private static boolean hexadecimal_integer_2(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "hexadecimal_integer_2")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = hexadecimal_integer_2_0(b, l + 1);
    while (r) {
      int c = current_position_(b);
      if (!hexadecimal_integer_2_0(b, l + 1)) break;
      if (!empty_element_parsed_guard_(b, "hexadecimal_integer_2", c)) break;
    }
    exit_section_(b, m, null, r);
    return r;
  }

  // ["_"] hexadecimal_digit
  private static boolean hexadecimal_integer_2_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "hexadecimal_integer_2_0")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = hexadecimal_integer_2_0_0(b, l + 1);
    r = r && hexadecimal_digit(b, l + 1);
    exit_section_(b, m, null, r);
    return r;
  }

  // ["_"]
  private static boolean hexadecimal_integer_2_0_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "hexadecimal_integer_2_0_0")) return false;
    consumeToken(b, "_");
    return true;
  }

  /* ********************************************************** */
  // "regexp:[^\\d\\W]\\w*"
  public static boolean identifier(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "identifier")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, IDENTIFIER, "<identifier>");
    r = consumeToken(b, "regexp:[^\\d\\W]\\w*");
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  /* ********************************************************** */
  // real_number ("i" | "I" | "j" | "J")
  public static boolean imaginary_number(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "imaginary_number")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, IMAGINARY_NUMBER, "<imaginary number>");
    r = real_number(b, l + 1);
    r = r && imaginary_number_1(b, l + 1);
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  // "i" | "I" | "j" | "J"
  private static boolean imaginary_number_1(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "imaginary_number_1")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = consumeToken(b, "i");
    if (!r) r = consumeToken(b, "I");
    if (!r) r = consumeToken(b, "j");
    if (!r) r = consumeToken(b, "J");
    exit_section_(b, m, null, r);
    return r;
  }

  /* ********************************************************** */
  // decimal_integer | binary_integer | octal_integer | hexadecimal_integer
  public static boolean integer(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "integer")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, INTEGER, "<integer>");
    r = decimal_integer(b, l + 1);
    if (!r) r = binary_integer(b, l + 1);
    if (!r) r = octal_integer(b, l + 1);
    if (!r) r = hexadecimal_integer(b, l + 1);
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  /* ********************************************************** */
  // NEWLINE | statement
  public static boolean line(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "line")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, LINE, "<line>");
    r = consumeToken(b, NEWLINE);
    if (!r) r = statement(b, l + 1);
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  /* ********************************************************** */
  // number | string
  public static boolean literal(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "literal")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, LITERAL, "<literal>");
    r = number(b, l + 1);
    if (!r) r = string(b, l + 1);
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  /* ********************************************************** */
  // decimal_real | scientific_real
  public static boolean non_integer_real_number(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "non_integer_real_number")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, NON_INTEGER_REAL_NUMBER, "<non integer real number>");
    r = decimal_real(b, l + 1);
    if (!r) r = scientific_real(b, l + 1);
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  /* ********************************************************** */
  // "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
  public static boolean nonzero_digit(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "nonzero_digit")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, NONZERO_DIGIT, "<nonzero digit>");
    r = consumeToken(b, "1");
    if (!r) r = consumeToken(b, "2");
    if (!r) r = consumeToken(b, "3");
    if (!r) r = consumeToken(b, "4");
    if (!r) r = consumeToken(b, "5");
    if (!r) r = consumeToken(b, "6");
    if (!r) r = consumeToken(b, "7");
    if (!r) r = consumeToken(b, "8");
    if (!r) r = consumeToken(b, "9");
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  /* ********************************************************** */
  // real_number | imaginary_number
  public static boolean number(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "number")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, NUMBER, "<number>");
    r = real_number(b, l + 1);
    if (!r) r = imaginary_number(b, l + 1);
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  /* ********************************************************** */
  // "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7"
  public static boolean octal_digit(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "octal_digit")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, OCTAL_DIGIT, "<octal digit>");
    r = consumeToken(b, "0");
    if (!r) r = consumeToken(b, "1");
    if (!r) r = consumeToken(b, "2");
    if (!r) r = consumeToken(b, "3");
    if (!r) r = consumeToken(b, "4");
    if (!r) r = consumeToken(b, "5");
    if (!r) r = consumeToken(b, "6");
    if (!r) r = consumeToken(b, "7");
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  /* ********************************************************** */
  // "0" ("o" | "O") (["_"] octal_digit)+
  public static boolean octal_integer(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "octal_integer")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, OCTAL_INTEGER, "<octal integer>");
    r = consumeToken(b, "0");
    r = r && octal_integer_1(b, l + 1);
    r = r && octal_integer_2(b, l + 1);
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  // "o" | "O"
  private static boolean octal_integer_1(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "octal_integer_1")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = consumeToken(b, "o");
    if (!r) r = consumeToken(b, "O");
    exit_section_(b, m, null, r);
    return r;
  }

  // (["_"] octal_digit)+
  private static boolean octal_integer_2(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "octal_integer_2")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = octal_integer_2_0(b, l + 1);
    while (r) {
      int c = current_position_(b);
      if (!octal_integer_2_0(b, l + 1)) break;
      if (!empty_element_parsed_guard_(b, "octal_integer_2", c)) break;
    }
    exit_section_(b, m, null, r);
    return r;
  }

  // ["_"] octal_digit
  private static boolean octal_integer_2_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "octal_integer_2_0")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = octal_integer_2_0_0(b, l + 1);
    r = r && octal_digit(b, l + 1);
    exit_section_(b, m, null, r);
    return r;
  }

  // ["_"]
  private static boolean octal_integer_2_0_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "octal_integer_2_0_0")) return false;
    consumeToken(b, "_");
    return true;
  }

  /* ********************************************************** */
  // identifier | literal
  static boolean operatorless_expression(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "operatorless_expression")) return false;
    boolean r;
    r = identifier(b, l + 1);
    if (!r) r = literal(b, l + 1);
    return r;
  }

  /* ********************************************************** */
  // integer | non_integer_real_number
  public static boolean real_number(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "real_number")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, REAL_NUMBER, "<real number>");
    r = integer(b, l + 1);
    if (!r) r = non_integer_real_number(b, l + 1);
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  /* ********************************************************** */
  // (simple_integer | decimal_real) ("e" | "E") ("+" | "-")? simple_integer
  public static boolean scientific_real(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "scientific_real")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, SCIENTIFIC_REAL, "<scientific real>");
    r = scientific_real_0(b, l + 1);
    r = r && scientific_real_1(b, l + 1);
    r = r && scientific_real_2(b, l + 1);
    r = r && simple_integer(b, l + 1);
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  // simple_integer | decimal_real
  private static boolean scientific_real_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "scientific_real_0")) return false;
    boolean r;
    r = simple_integer(b, l + 1);
    if (!r) r = decimal_real(b, l + 1);
    return r;
  }

  // "e" | "E"
  private static boolean scientific_real_1(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "scientific_real_1")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = consumeToken(b, "e");
    if (!r) r = consumeToken(b, "E");
    exit_section_(b, m, null, r);
    return r;
  }

  // ("+" | "-")?
  private static boolean scientific_real_2(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "scientific_real_2")) return false;
    scientific_real_2_0(b, l + 1);
    return true;
  }

  // "+" | "-"
  private static boolean scientific_real_2_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "scientific_real_2_0")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = consumeToken(b, "+");
    if (!r) r = consumeToken(b, "-");
    exit_section_(b, m, null, r);
    return r;
  }

  /* ********************************************************** */
  // digit (["_"] digit)*
  public static boolean simple_integer(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "simple_integer")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, SIMPLE_INTEGER, "<simple integer>");
    r = digit(b, l + 1);
    r = r && simple_integer_1(b, l + 1);
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  // (["_"] digit)*
  private static boolean simple_integer_1(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "simple_integer_1")) return false;
    while (true) {
      int c = current_position_(b);
      if (!simple_integer_1_0(b, l + 1)) break;
      if (!empty_element_parsed_guard_(b, "simple_integer_1", c)) break;
    }
    return true;
  }

  // ["_"] digit
  private static boolean simple_integer_1_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "simple_integer_1_0")) return false;
    boolean r;
    Marker m = enter_section_(b);
    r = simple_integer_1_0_0(b, l + 1);
    r = r && digit(b, l + 1);
    exit_section_(b, m, null, r);
    return r;
  }

  // ["_"]
  private static boolean simple_integer_1_0_0(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "simple_integer_1_0_0")) return false;
    consumeToken(b, "_");
    return true;
  }

  /* ********************************************************** */
  // expression | simple_statement | compound_statement
  public static boolean statement(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "statement")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, STATEMENT, "<statement>");
    r = expression(b, l + 1);
    if (!r) r = consumeToken(b, SIMPLE_STATEMENT);
    if (!r) r = consumeToken(b, COMPOUND_STATEMENT);
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  /* ********************************************************** */
  // "regexp:\"[^\"\\\\]*(\\\\.[^\"\\\\]*)*\""
  public static boolean string(PsiBuilder b, int l) {
    if (!recursion_guard_(b, l, "string")) return false;
    boolean r;
    Marker m = enter_section_(b, l, _NONE_, STRING, "<string>");
    r = consumeToken(b, "regexp:\"[^\"\\\\]*(\\\\.[^\"\\\\]*)*\"");
    exit_section_(b, l, m, r, false, null);
    return r;
  }

  final static Parser operatorless_expression_parser_ = new Parser() {
    public boolean parse(PsiBuilder b, int l) {
      return operatorless_expression(b, l + 1);
    }
  };
}
