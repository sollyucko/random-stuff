<?xml version="1.0" encoding="UTF-8"?>
<model ref="r:6760b883-d39e-498a-9d76-7cf99c529a82(DisFunctional.structure)">
  <persistence version="9" />
  <languages>
    <use id="c72da2b9-7cce-4447-8389-f407dc1158b7" name="jetbrains.mps.lang.structure" version="6" />
    <devkit ref="78434eb8-b0e5-444b-850d-e7c4ad2da9ab(jetbrains.mps.devkit.aspect.structure)" />
  </languages>
  <imports>
    <import index="tpck" ref="r:00000000-0000-4000-0000-011c89590288(jetbrains.mps.lang.core.structure)" implicit="true" />
  </imports>
  <registry>
    <language id="c72da2b9-7cce-4447-8389-f407dc1158b7" name="jetbrains.mps.lang.structure">
      <concept id="1169125787135" name="jetbrains.mps.lang.structure.structure.AbstractConceptDeclaration" flags="ig" index="PkWjJ">
        <property id="6714410169261853888" name="conceptId" index="EcuMT" />
        <child id="1071489727083" name="linkDeclaration" index="1TKVEi" />
      </concept>
      <concept id="1169127622168" name="jetbrains.mps.lang.structure.structure.InterfaceConceptReference" flags="ig" index="PrWs8">
        <reference id="1169127628841" name="intfc" index="PrY4T" />
      </concept>
      <concept id="1071489090640" name="jetbrains.mps.lang.structure.structure.ConceptDeclaration" flags="ig" index="1TIwiD">
        <property id="1096454100552" name="rootable" index="19KtqR" />
        <reference id="1071489389519" name="extends" index="1TJDcQ" />
        <child id="1169129564478" name="implements" index="PzmwI" />
      </concept>
      <concept id="1071489288298" name="jetbrains.mps.lang.structure.structure.LinkDeclaration" flags="ig" index="1TJgyj">
        <property id="1071599776563" name="role" index="20kJfa" />
        <property id="1071599893252" name="sourceCardinality" index="20lbJX" />
        <property id="1071599937831" name="metaClass" index="20lmBu" />
        <property id="241647608299431140" name="linkId" index="IQ2ns" />
        <reference id="1071599976176" name="target" index="20lvS9" />
      </concept>
    </language>
    <language id="ceab5195-25ea-4f22-9b92-103b95ca8c0c" name="jetbrains.mps.lang.core">
      <concept id="1169194658468" name="jetbrains.mps.lang.core.structure.INamedConcept" flags="ng" index="TrEIO">
        <property id="1169194664001" name="name" index="TrG5h" />
      </concept>
    </language>
  </registry>
  <node concept="1TIwiD" id="6VrRWu7j8Ws">
    <property role="EcuMT" value="7988224412133134108" />
    <property role="TrG5h" value="Program" />
    <property role="19KtqR" value="true" />
    <ref role="1TJDcQ" to="tpck:gw2VY9q" resolve="BaseConcept" />
    <node concept="1TJgyj" id="6VrRWu7j8WJ" role="1TKVEi">
      <property role="IQ2ns" value="7988224412133134127" />
      <property role="20lmBu" value="aggregation" />
      <property role="20kJfa" value="statements" />
      <property role="20lbJX" value="0..n" />
      <ref role="20lvS9" node="6VrRWu7j8Wy" resolve="Statement" />
    </node>
  </node>
  <node concept="1TIwiD" id="6VrRWu7j8Wy">
    <property role="EcuMT" value="7988224412133134114" />
    <property role="TrG5h" value="Statement" />
    <ref role="1TJDcQ" to="tpck:gw2VY9q" resolve="BaseConcept" />
  </node>
  <node concept="1TIwiD" id="6VrRWu7j9gh">
    <property role="EcuMT" value="7988224412133135377" />
    <property role="TrG5h" value="RoutineCall" />
    <ref role="1TJDcQ" node="6VrRWu7j8Wy" resolve="Statement" />
    <node concept="1TJgyj" id="6VrRWu7j9Y_" role="1TKVEi">
      <property role="IQ2ns" value="7988224412133138341" />
      <property role="20lmBu" value="reference" />
      <property role="20kJfa" value="routine" />
      <ref role="20lvS9" node="6VrRWu7j9Jv" resolve="RoutineDeclaration" />
    </node>
  </node>
  <node concept="1TIwiD" id="6VrRWu7j9Jv">
    <property role="EcuMT" value="7988224412133137375" />
    <property role="TrG5h" value="RoutineDeclaration" />
    <ref role="1TJDcQ" node="6VrRWu7j8Wy" resolve="Statement" />
    <node concept="PrWs8" id="6VrRWu7j9JV" role="PzmwI">
      <ref role="PrY4T" to="tpck:h0TrEE$" resolve="INamedConcept" />
    </node>
    <node concept="1TJgyj" id="6VrRWu7jj47" role="1TKVEi">
      <property role="IQ2ns" value="7988224412133175559" />
      <property role="20lmBu" value="aggregation" />
      <property role="20kJfa" value="program" />
      <property role="20lbJX" value="1" />
      <ref role="20lvS9" node="6VrRWu7j8Ws" resolve="Program" />
    </node>
  </node>
</model>

