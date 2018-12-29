// This is a generated file. Not intended for manual editing.
package io.github.sollyucko.coconut_plugin.psi.impl;

import java.util.List;
import org.jetbrains.annotations.*;
import com.intellij.lang.ASTNode;
import com.intellij.psi.PsiElement;
import com.intellij.psi.PsiElementVisitor;
import com.intellij.psi.util.PsiTreeUtil;
import static io.github.sollyucko.coconut_plugin.psi.CoconutTypes.*;
import com.intellij.extapi.psi.ASTWrapperPsiElement;
import io.github.sollyucko.coconut_plugin.psi.*;

public class CoconutBinaryIntegerImpl extends ASTWrapperPsiElement implements CoconutBinaryInteger {

  public CoconutBinaryIntegerImpl(@NotNull ASTNode node) {
    super(node);
  }

  public void accept(@NotNull CoconutVisitor visitor) {
    visitor.visitBinaryInteger(this);
  }

  public void accept(@NotNull PsiElementVisitor visitor) {
    if (visitor instanceof CoconutVisitor) accept((CoconutVisitor)visitor);
    else super.accept(visitor);
  }

  @Override
  @NotNull
  public List<CoconutBinaryDigit> getBinaryDigitList() {
    return PsiTreeUtil.getChildrenOfTypeAsList(this, CoconutBinaryDigit.class);
  }

}
