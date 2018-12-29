<?xml version="1.0" encoding="UTF-8"?>
<model ref="r:efdd7577-bd98-4b07-8d64-16d2790952b4(DisFunctional.editor)">
  <persistence version="9" />
  <languages>
    <use id="18bc6592-03a6-4e29-a83a-7ff23bde13ba" name="jetbrains.mps.lang.editor" version="11" />
    <devkit ref="fbc25dd2-5da4-483a-8b19-70928e1b62d7(jetbrains.mps.devkit.general-purpose)" />
  </languages>
  <imports>
    <import index="csqa" ref="r:6760b883-d39e-498a-9d76-7cf99c529a82(DisFunctional.structure)" implicit="true" />
    <import index="tpck" ref="r:00000000-0000-4000-0000-011c89590288(jetbrains.mps.lang.core.structure)" implicit="true" />
  </imports>
  <registry>
    <language id="18bc6592-03a6-4e29-a83a-7ff23bde13ba" name="jetbrains.mps.lang.editor">
      <concept id="1071666914219" name="jetbrains.mps.lang.editor.structure.ConceptEditorDeclaration" flags="ig" index="24kQdi" />
      <concept id="1140524381322" name="jetbrains.mps.lang.editor.structure.CellModel_ListWithRole" flags="ng" index="2czfm3">
        <child id="1140524464360" name="cellLayout" index="2czzBx" />
      </concept>
      <concept id="1237303669825" name="jetbrains.mps.lang.editor.structure.CellLayout_Indent" flags="nn" index="l2Vlx" />
      <concept id="1237307900041" name="jetbrains.mps.lang.editor.structure.IndentLayoutIndentStyleClassItem" flags="ln" index="lj46D" />
      <concept id="1237308012275" name="jetbrains.mps.lang.editor.structure.IndentLayoutNewLineStyleClassItem" flags="ln" index="ljvvj" />
      <concept id="1237375020029" name="jetbrains.mps.lang.editor.structure.IndentLayoutNewLineChildrenStyleClassItem" flags="ln" index="pj6Ft" />
      <concept id="1080736578640" name="jetbrains.mps.lang.editor.structure.BaseEditorComponent" flags="ig" index="2wURMF">
        <child id="1080736633877" name="cellModel" index="2wV5jI" />
      </concept>
      <concept id="1186414536763" name="jetbrains.mps.lang.editor.structure.BooleanStyleSheetItem" flags="ln" index="VOi$J">
        <property id="1186414551515" name="flag" index="VOm3f" />
      </concept>
      <concept id="1088013125922" name="jetbrains.mps.lang.editor.structure.CellModel_RefCell" flags="sg" stub="730538219795941030" index="1iCGBv">
        <child id="1088186146602" name="editorComponent" index="1sWHZn" />
      </concept>
      <concept id="1088185857835" name="jetbrains.mps.lang.editor.structure.InlineEditorComponent" flags="ig" index="1sVBvm" />
      <concept id="1139848536355" name="jetbrains.mps.lang.editor.structure.CellModel_WithRole" flags="ng" index="1$h60E">
        <reference id="1140103550593" name="relationDeclaration" index="1NtTu8" />
      </concept>
      <concept id="1073389446423" name="jetbrains.mps.lang.editor.structure.CellModel_Collection" flags="sn" stub="3013115976261988961" index="3EZMnI">
        <child id="1106270802874" name="cellLayout" index="2iSdaV" />
        <child id="1073389446424" name="childCellModel" index="3EZMnx" />
      </concept>
      <concept id="1073389577006" name="jetbrains.mps.lang.editor.structure.CellModel_Constant" flags="sn" stub="3610246225209162225" index="3F0ifn">
        <property id="1073389577007" name="text" index="3F0ifm" />
      </concept>
      <concept id="1073389658414" name="jetbrains.mps.lang.editor.structure.CellModel_Property" flags="sg" stub="730538219796134133" index="3F0A7n" />
      <concept id="1219418625346" name="jetbrains.mps.lang.editor.structure.IStyleContainer" flags="ng" index="3F0Thp">
        <child id="1219418656006" name="styleItem" index="3F10Kt" />
      </concept>
      <concept id="1073389882823" name="jetbrains.mps.lang.editor.structure.CellModel_RefNode" flags="sg" stub="730538219795960754" index="3F1sOY" />
      <concept id="1073390211982" name="jetbrains.mps.lang.editor.structure.CellModel_RefNodeList" flags="sg" stub="2794558372793454595" index="3F2HdR" />
      <concept id="1166049232041" name="jetbrains.mps.lang.editor.structure.AbstractComponent" flags="ng" index="1XWOmA">
        <reference id="1166049300910" name="conceptDeclaration" index="1XX52x" />
      </concept>
    </language>
  </registry>
  <node concept="24kQdi" id="6VrRWu7j8Wt">
    <ref role="1XX52x" to="csqa:6VrRWu7j8Ws" resolve="Program" />
    <node concept="3EZMnI" id="6VrRWu7joZ6" role="2wV5jI">
      <node concept="l2Vlx" id="6VrRWu7joZ7" role="2iSdaV" />
      <node concept="3F2HdR" id="6VrRWu7joZj" role="3EZMnx">
        <ref role="1NtTu8" to="csqa:6VrRWu7j8WJ" resolve="statements" />
        <node concept="l2Vlx" id="6VrRWu7joZk" role="2czzBx" />
        <node concept="pj6Ft" id="6VrRWu7joZl" role="3F10Kt">
          <property role="VOm3f" value="true" />
        </node>
        <node concept="lj46D" id="6VrRWu7joZm" role="3F10Kt">
          <property role="VOm3f" value="true" />
        </node>
        <node concept="ljvvj" id="6VrRWu7joZn" role="3F10Kt">
          <property role="VOm3f" value="true" />
        </node>
      </node>
    </node>
  </node>
  <node concept="24kQdi" id="6VrRWu7j9Y8">
    <ref role="1XX52x" to="csqa:6VrRWu7j9gh" resolve="RoutineCall" />
    <node concept="3EZMnI" id="6VrRWu7jkXS" role="2wV5jI">
      <node concept="l2Vlx" id="6VrRWu7jkXT" role="2iSdaV" />
      <node concept="3F0ifn" id="6VrRWu7jkXU" role="3EZMnx">
        <property role="3F0ifm" value="call routine" />
      </node>
      <node concept="1iCGBv" id="6VrRWu7jkXW" role="3EZMnx">
        <ref role="1NtTu8" to="csqa:6VrRWu7j9Y_" resolve="routine" />
        <node concept="1sVBvm" id="6VrRWu7jkXZ" role="1sWHZn">
          <node concept="3F0A7n" id="6VrRWu7jkY1" role="2wV5jI">
            <ref role="1NtTu8" to="tpck:h0TrG11" resolve="name" />
          </node>
        </node>
      </node>
    </node>
  </node>
  <node concept="24kQdi" id="6VrRWu7jj4o">
    <ref role="1XX52x" to="csqa:6VrRWu7j9Jv" resolve="RoutineDeclaration" />
    <node concept="3EZMnI" id="6VrRWu7jmIf" role="2wV5jI">
      <node concept="l2Vlx" id="6VrRWu7jmIg" role="2iSdaV" />
      <node concept="3F0ifn" id="6VrRWu7jmIh" role="3EZMnx">
        <property role="3F0ifm" value="routine declaration" />
      </node>
      <node concept="3F0A7n" id="6VrRWu7jmIi" role="3EZMnx">
        <ref role="1NtTu8" to="tpck:h0TrG11" resolve="name" />
      </node>
      <node concept="3EZMnI" id="6VrRWu7jmIm" role="3EZMnx">
        <node concept="l2Vlx" id="6VrRWu7jmIn" role="2iSdaV" />
        <node concept="lj46D" id="6VrRWu7jmIo" role="3F10Kt">
          <property role="VOm3f" value="true" />
        </node>
        <node concept="3F1sOY" id="6VrRWu7jmIt" role="3EZMnx">
          <ref role="1NtTu8" to="csqa:6VrRWu7jj47" resolve="program" />
          <node concept="lj46D" id="6VrRWu7jmIu" role="3F10Kt">
            <property role="VOm3f" value="true" />
          </node>
          <node concept="ljvvj" id="6VrRWu7jmIv" role="3F10Kt">
            <property role="VOm3f" value="true" />
          </node>
        </node>
      </node>
    </node>
  </node>
</model>

