package solly.tutorials.calculator.structure;

/*Generated by MPS */

import jetbrains.mps.lang.smodel.LanguageConceptIndex;
import jetbrains.mps.lang.smodel.LanguageConceptIndexBuilder;
import jetbrains.mps.smodel.adapter.ids.SConceptId;
import org.jetbrains.mps.openapi.language.SAbstractConcept;

public final class LanguageConceptSwitch {
  private final LanguageConceptIndex myIndex;
  public static final int Calculator = 0;
  public static final int InputField = 1;
  public static final int InputFieldReference = 2;
  public static final int OutputField = 3;

  public LanguageConceptSwitch() {
    LanguageConceptIndexBuilder builder = new LanguageConceptIndexBuilder(0xb82c1489ef4142a8L, 0xa822be676a783f97L);
    builder.put(0x6edbdfc7873b5b41L, Calculator);
    builder.put(0x6edbdfc7873bfb78L, InputField);
    builder.put(0x6edbdfc7873c90bfL, InputFieldReference);
    builder.put(0x6edbdfc7873c259dL, OutputField);
    myIndex = builder.seal();
  }

  /*package*/ int index(SConceptId cid) {
    return myIndex.index(cid);
  }

  public int index(SAbstractConcept concept) {
    return myIndex.index(concept);
  }
}
