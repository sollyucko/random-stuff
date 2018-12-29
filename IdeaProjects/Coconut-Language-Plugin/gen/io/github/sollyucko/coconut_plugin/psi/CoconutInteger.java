// This is a generated file. Not intended for manual editing.
package io.github.sollyucko.coconut_plugin.psi;

import java.util.List;
import org.jetbrains.annotations.*;
import com.intellij.psi.PsiElement;

public interface CoconutInteger extends PsiElement {

  @Nullable
  CoconutBinaryInteger getBinaryInteger();

  @Nullable
  CoconutDecimalInteger getDecimalInteger();

  @Nullable
  CoconutHexadecimalInteger getHexadecimalInteger();

  @Nullable
  CoconutOctalInteger getOctalInteger();

}
