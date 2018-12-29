<?xml version="1.0" encoding="UTF-8"?>
<model ref="r:df74f1ed-a0af-4470-b3ed-9c0b7e5607c5(SemiFunctional)">
  <persistence version="9" />
  <languages>
    <use id="61a56757-112c-4d88-842c-1121d52928c2" name="Functional" version="-1" />
    <use id="f6ffa208-e997-4a9e-8095-9550ead5b5af" name="DisFunctional" version="0" />
  </languages>
  <imports />
  <registry>
    <language id="ceab5195-25ea-4f22-9b92-103b95ca8c0c" name="jetbrains.mps.lang.core">
      <concept id="1169194658468" name="jetbrains.mps.lang.core.structure.INamedConcept" flags="ng" index="TrEIO">
        <property id="1169194664001" name="name" index="TrG5h" />
      </concept>
    </language>
    <language id="f6ffa208-e997-4a9e-8095-9550ead5b5af" name="DisFunctional">
      <concept id="7988224412133137375" name="DisFunctional.structure.RoutineDeclaration" flags="ng" index="3D_Ogo">
        <child id="7988224412133175559" name="program" index="3D_IV0" />
      </concept>
      <concept id="7988224412133135377" name="DisFunctional.structure.RoutineCall" flags="ng" index="3D_OJm">
        <reference id="7988224412133138341" name="routine" index="3D_O1y" />
      </concept>
      <concept id="7988224412133134108" name="DisFunctional.structure.Program" flags="ng" index="3D_P3r">
        <child id="7988224412133134127" name="statements" index="3D_P3C" />
      </concept>
      <concept id="7988224412133134114" name="DisFunctional.structure.Statement" flags="ng" index="3D_P3_" />
    </language>
  </registry>
  <node concept="3D_P3r" id="6VrRWu7jbX9">
    <node concept="3D_Ogo" id="6VrRWu7jrs4" role="3D_P3C">
      <property role="TrG5h" value="routine" />
      <node concept="3D_P3r" id="6VrRWu7jrs5" role="3D_IV0">
        <node concept="3D_OJm" id="6VrRWu7jrsa" role="3D_P3C">
          <ref role="3D_O1y" node="6VrRWu7jrs4" resolve="routine" />
        </node>
      </node>
    </node>
    <node concept="3D_P3_" id="6VrRWu7jrsm" role="3D_P3C" />
  </node>
</model>

