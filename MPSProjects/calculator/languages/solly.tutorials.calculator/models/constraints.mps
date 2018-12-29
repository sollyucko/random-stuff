<?xml version="1.0" encoding="UTF-8"?>
<model ref="r:bf65cd28-3126-4b03-9c84-542df0928d5e(solly.tutorials.calculator.constraints)">
  <persistence version="9" />
  <languages>
    <use id="3f4bc5f5-c6c1-4a28-8b10-c83066ffa4a1" name="jetbrains.mps.lang.constraints" version="4" />
    <devkit ref="00000000-0000-4000-0000-5604ebd4f22c(jetbrains.mps.devkit.aspect.constraints)" />
  </languages>
  <imports>
    <import index="xv7z" ref="r:541fa709-e489-498e-8c7b-45b0d1ff3578(solly.tutorials.calculator.structure)" implicit="true" />
  </imports>
  <registry>
    <language id="3f4bc5f5-c6c1-4a28-8b10-c83066ffa4a1" name="jetbrains.mps.lang.constraints">
      <concept id="8401916545537438642" name="jetbrains.mps.lang.constraints.structure.InheritedNodeScopeFactory" flags="ng" index="1dDu$B">
        <reference id="8401916545537438643" name="kind" index="1dDu$A" />
      </concept>
      <concept id="1213093968558" name="jetbrains.mps.lang.constraints.structure.ConceptConstraints" flags="ng" index="1M2fIO">
        <reference id="1213093996982" name="concept" index="1M2myG" />
        <child id="1213100494875" name="referent" index="1Mr941" />
      </concept>
      <concept id="1148687176410" name="jetbrains.mps.lang.constraints.structure.NodeReferentConstraint" flags="ng" index="1N5Pfh">
        <reference id="1148687202698" name="applicableLink" index="1N5Vy1" />
        <child id="1148687345559" name="searchScopeFactory" index="1N6uqs" />
      </concept>
    </language>
  </registry>
  <node concept="1M2fIO" id="6VrRWu7j17O">
    <ref role="1M2myG" to="xv7z:6VrRWu7f92Z" resolve="InputFieldReference" />
    <node concept="1N5Pfh" id="6VrRWu7j18g" role="1Mr941">
      <ref role="1N5Vy1" to="xv7z:6VrRWu7f930" resolve="field" />
      <node concept="1dDu$B" id="6VrRWu7j18i" role="1N6uqs">
        <ref role="1dDu$A" to="xv7z:6VrRWu7eZHS" resolve="InputField" />
      </node>
    </node>
  </node>
</model>

