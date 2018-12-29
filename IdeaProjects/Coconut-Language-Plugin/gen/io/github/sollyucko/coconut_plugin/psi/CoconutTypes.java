// This is a generated file. Not intended for manual editing.
package io.github.sollyucko.coconut_plugin.psi;

import com.intellij.psi.tree.IElementType;
import com.intellij.psi.PsiElement;
import com.intellij.lang.ASTNode;
import io.github.sollyucko.coconut_plugin.psi.impl.*;

public interface CoconutTypes {

  IElementType BINARY_DIGIT = new CoconutElementType("BINARY_DIGIT");
  IElementType BINARY_INTEGER = new CoconutElementType("BINARY_INTEGER");
  IElementType DECIMAL_INTEGER = new CoconutElementType("DECIMAL_INTEGER");
  IElementType DECIMAL_REAL = new CoconutElementType("DECIMAL_REAL");
  IElementType DIGIT = new CoconutElementType("DIGIT");
  IElementType EXPRESSION = new CoconutElementType("EXPRESSION");
  IElementType HEXADECIMAL_DIGIT = new CoconutElementType("HEXADECIMAL_DIGIT");
  IElementType HEXADECIMAL_INTEGER = new CoconutElementType("HEXADECIMAL_INTEGER");
  IElementType IDENTIFIER = new CoconutElementType("IDENTIFIER");
  IElementType IMAGINARY_NUMBER = new CoconutElementType("IMAGINARY_NUMBER");
  IElementType INTEGER = new CoconutElementType("INTEGER");
  IElementType LINE = new CoconutElementType("LINE");
  IElementType LITERAL = new CoconutElementType("LITERAL");
  IElementType NONZERO_DIGIT = new CoconutElementType("NONZERO_DIGIT");
  IElementType NON_INTEGER_REAL_NUMBER = new CoconutElementType("NON_INTEGER_REAL_NUMBER");
  IElementType NUMBER = new CoconutElementType("NUMBER");
  IElementType OCTAL_DIGIT = new CoconutElementType("OCTAL_DIGIT");
  IElementType OCTAL_INTEGER = new CoconutElementType("OCTAL_INTEGER");
  IElementType REAL_NUMBER = new CoconutElementType("REAL_NUMBER");
  IElementType SCIENTIFIC_REAL = new CoconutElementType("SCIENTIFIC_REAL");
  IElementType SIMPLE_INTEGER = new CoconutElementType("SIMPLE_INTEGER");
  IElementType STATEMENT = new CoconutElementType("STATEMENT");
  IElementType STRING = new CoconutElementType("STRING");

  IElementType COMPOUND_STATEMENT = new CoconutTokenType("compound_statement");
  IElementType NEWLINE = new CoconutTokenType("NEWLINE");
  IElementType SIMPLE_STATEMENT = new CoconutTokenType("simple_statement");

  class Factory {
    public static PsiElement createElement(ASTNode node) {
      IElementType type = node.getElementType();
       if (type == BINARY_DIGIT) {
        return new CoconutBinaryDigitImpl(node);
      }
      else if (type == BINARY_INTEGER) {
        return new CoconutBinaryIntegerImpl(node);
      }
      else if (type == DECIMAL_INTEGER) {
        return new CoconutDecimalIntegerImpl(node);
      }
      else if (type == DECIMAL_REAL) {
        return new CoconutDecimalRealImpl(node);
      }
      else if (type == DIGIT) {
        return new CoconutDigitImpl(node);
      }
      else if (type == EXPRESSION) {
        return new CoconutExpressionImpl(node);
      }
      else if (type == HEXADECIMAL_DIGIT) {
        return new CoconutHexadecimalDigitImpl(node);
      }
      else if (type == HEXADECIMAL_INTEGER) {
        return new CoconutHexadecimalIntegerImpl(node);
      }
      else if (type == IDENTIFIER) {
        return new CoconutIdentifierImpl(node);
      }
      else if (type == IMAGINARY_NUMBER) {
        return new CoconutImaginaryNumberImpl(node);
      }
      else if (type == INTEGER) {
        return new CoconutIntegerImpl(node);
      }
      else if (type == LINE) {
        return new CoconutLineImpl(node);
      }
      else if (type == LITERAL) {
        return new CoconutLiteralImpl(node);
      }
      else if (type == NONZERO_DIGIT) {
        return new CoconutNonzeroDigitImpl(node);
      }
      else if (type == NON_INTEGER_REAL_NUMBER) {
        return new CoconutNonIntegerRealNumberImpl(node);
      }
      else if (type == NUMBER) {
        return new CoconutNumberImpl(node);
      }
      else if (type == OCTAL_DIGIT) {
        return new CoconutOctalDigitImpl(node);
      }
      else if (type == OCTAL_INTEGER) {
        return new CoconutOctalIntegerImpl(node);
      }
      else if (type == REAL_NUMBER) {
        return new CoconutRealNumberImpl(node);
      }
      else if (type == SCIENTIFIC_REAL) {
        return new CoconutScientificRealImpl(node);
      }
      else if (type == SIMPLE_INTEGER) {
        return new CoconutSimpleIntegerImpl(node);
      }
      else if (type == STATEMENT) {
        return new CoconutStatementImpl(node);
      }
      else if (type == STRING) {
        return new CoconutStringImpl(node);
      }
      throw new AssertionError("Unknown element type: " + type);
    }
  }
}
