<?xml version="1.0" encoding="UTF-8"?>
<model ref="r:3d600235-0db5-4bac-b42b-b2b05d7ee4a8(solly.tutorials.calculator.sandbox)">
  <persistence version="9" />
  <languages>
    <use id="b82c1489-ef41-42a8-a822-be676a783f97" name="solly.tutorials.calculator" version="0" />
    <use id="ceab5195-25ea-4f22-9b92-103b95ca8c0c" name="jetbrains.mps.lang.core" version="1" />
    <use id="f3061a53-9226-4cc5-a443-f952ceaf5816" name="jetbrains.mps.baseLanguage" version="6" />
  </languages>
  <imports />
  <registry>
    <language id="f3061a53-9226-4cc5-a443-f952ceaf5816" name="jetbrains.mps.baseLanguage">
      <concept id="1092119917967" name="jetbrains.mps.baseLanguage.structure.MulExpression" flags="nn" index="17qRlL" />
      <concept id="1068580320020" name="jetbrains.mps.baseLanguage.structure.IntegerConstant" flags="nn" index="3cmrfG">
        <property id="1068580320021" name="value" index="3cmrfH" />
      </concept>
      <concept id="1068581242869" name="jetbrains.mps.baseLanguage.structure.MinusExpression" flags="nn" index="3cpWsd" />
      <concept id="1079359253375" name="jetbrains.mps.baseLanguage.structure.ParenthesizedExpression" flags="nn" index="1eOMI4">
        <child id="1079359253376" name="expression" index="1eOMHV" />
      </concept>
      <concept id="1081773326031" name="jetbrains.mps.baseLanguage.structure.BinaryOperation" flags="nn" index="3uHJSO">
        <child id="1081773367579" name="rightExpression" index="3uHU7w" />
        <child id="1081773367580" name="leftExpression" index="3uHU7B" />
      </concept>
      <concept id="1073239437375" name="jetbrains.mps.baseLanguage.structure.NotEqualsExpression" flags="nn" index="3y3z36" />
      <concept id="1163668896201" name="jetbrains.mps.baseLanguage.structure.TernaryOperatorExpression" flags="nn" index="3K4zz7">
        <child id="1163668914799" name="condition" index="3K4Cdx" />
        <child id="1163668922816" name="ifTrue" index="3K4E3e" />
        <child id="1163668934364" name="ifFalse" index="3K4GZi" />
      </concept>
    </language>
    <language id="b82c1489-ef41-42a8-a822-be676a783f97" name="solly.tutorials.calculator">
      <concept id="7988224412132047736" name="solly.tutorials.calculator.structure.InputField" flags="ng" index="3DS2iZ" />
      <concept id="7988224412132006721" name="solly.tutorials.calculator.structure.Calculator" flags="ng" index="3DS8i6">
        <child id="7988224412132047757" name="inputField" index="3DS2ha" />
        <child id="7988224412132058546" name="outputField" index="3DTZDP" />
      </concept>
      <concept id="7988224412132085951" name="solly.tutorials.calculator.structure.InputFieldReference" flags="ng" index="3DTOXS">
        <reference id="7988224412132085952" name="field" index="3DTOW7" />
      </concept>
      <concept id="7988224412132058525" name="solly.tutorials.calculator.structure.OutputField" flags="ng" index="3DTZDq">
        <child id="7988224412132065827" name="expression" index="3DTTR$" />
      </concept>
    </language>
    <language id="ceab5195-25ea-4f22-9b92-103b95ca8c0c" name="jetbrains.mps.lang.core">
      <concept id="1169194658468" name="jetbrains.mps.lang.core.structure.INamedConcept" flags="ng" index="TrEIO">
        <property id="1169194664001" name="name" index="TrG5h" />
      </concept>
    </language>
  </registry>
  <node concept="3DS8i6" id="6VrRWu7eZHR">
    <property role="TrG5h" value="test_calculator" />
    <node concept="3DS2iZ" id="6VrRWu7f2mk" role="3DS2ha">
      <property role="TrG5h" value="width" />
    </node>
    <node concept="3DS2iZ" id="6VrRWu7f2mm" role="3DS2ha">
      <property role="TrG5h" value="height" />
    </node>
    <node concept="3DS2iZ" id="6VrRWu7f2mp" role="3DS2ha">
      <property role="TrG5h" value="depth" />
    </node>
    <node concept="3DTZDq" id="6VrRWu7f47I" role="3DTZDP">
      <node concept="3cpWsd" id="6VrRWu7f8IR" role="3DTTR$">
        <node concept="3cmrfG" id="6VrRWu7j6o9" role="3uHU7B">
          <property role="3cmrfH" value="3" />
        </node>
        <node concept="17qRlL" id="6VrRWu7fnKF" role="3uHU7w">
          <node concept="3cmrfG" id="6VrRWu7f8vv" role="3uHU7B">
            <property role="3cmrfH" value="3" />
          </node>
          <node concept="1eOMI4" id="6VrRWu7j78l" role="3uHU7w">
            <node concept="3K4zz7" id="6VrRWu7j4dU" role="1eOMHV">
              <node concept="3cmrfG" id="6VrRWu7j4ty" role="3K4E3e">
                <property role="3cmrfH" value="1" />
              </node>
              <node concept="3cmrfG" id="6VrRWu7j4GT" role="3K4GZi">
                <property role="3cmrfH" value="2" />
              </node>
              <node concept="3y3z36" id="6VrRWu7j8vz" role="3K4Cdx">
                <node concept="3cmrfG" id="6VrRWu7j8AK" role="3uHU7w">
                  <property role="3cmrfH" value="0" />
                </node>
                <node concept="3DTOXS" id="6VrRWu7fnZX" role="3uHU7B">
                  <ref role="3DTOW7" node="6VrRWu7f2mk" resolve="width" />
                </node>
              </node>
            </node>
          </node>
        </node>
      </node>
    </node>
  </node>
  <node concept="3DS8i6" id="6VrRWu7j3C3">
    <property role="TrG5h" value="test_2" />
    <node concept="3DTZDq" id="6VrRWu7j3Cv" role="3DTZDP">
      <node concept="3cmrfG" id="6VrRWu7j4dI" role="3DTTR$">
        <property role="3cmrfH" value="1" />
      </node>
    </node>
  </node>
</model>

