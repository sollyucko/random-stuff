<?xml version="1.0" encoding="UTF-8"?>
<model ref="r:ceb8c77b-6cb1-4d00-b466-32ac82fbb054(main@generator)">
  <persistence version="9" />
  <languages>
    <devkit ref="a2eb3a43-fcc2-4200-80dc-c60110c4862d(jetbrains.mps.devkit.templates)" />
  </languages>
  <imports>
    <import index="xv7z" ref="r:541fa709-e489-498e-8c7b-45b0d1ff3578(solly.tutorials.calculator.structure)" />
    <import index="dxuu" ref="6354ebe7-c22a-4a0f-ac54-50b52ab9b065/java:javax.swing(JDK/)" />
    <import index="gsia" ref="6354ebe7-c22a-4a0f-ac54-50b52ab9b065/java:javax.swing.event(JDK/)" />
    <import index="z60i" ref="6354ebe7-c22a-4a0f-ac54-50b52ab9b065/java:java.awt(JDK/)" />
    <import index="r791" ref="6354ebe7-c22a-4a0f-ac54-50b52ab9b065/java:javax.swing.text(JDK/)" />
    <import index="tpee" ref="r:00000000-0000-4000-0000-011c895902ca(jetbrains.mps.baseLanguage.structure)" implicit="true" />
    <import index="wyt6" ref="6354ebe7-c22a-4a0f-ac54-50b52ab9b065/java:java.lang(JDK/)" implicit="true" />
    <import index="tpck" ref="r:00000000-0000-4000-0000-011c89590288(jetbrains.mps.lang.core.structure)" implicit="true" />
  </imports>
  <registry>
    <language id="f3061a53-9226-4cc5-a443-f952ceaf5816" name="jetbrains.mps.baseLanguage">
      <concept id="1082485599095" name="jetbrains.mps.baseLanguage.structure.BlockStatement" flags="nn" index="9aQIb">
        <child id="1082485599096" name="statements" index="9aQI4" />
      </concept>
      <concept id="1215693861676" name="jetbrains.mps.baseLanguage.structure.BaseAssignmentExpression" flags="nn" index="d038R">
        <child id="1068498886297" name="rValue" index="37vLTx" />
        <child id="1068498886295" name="lValue" index="37vLTJ" />
      </concept>
      <concept id="1202948039474" name="jetbrains.mps.baseLanguage.structure.InstanceMethodCallOperation" flags="nn" index="liA8E" />
      <concept id="1465982738277781862" name="jetbrains.mps.baseLanguage.structure.PlaceholderMember" flags="ng" index="2tJIrI" />
      <concept id="2820489544401957797" name="jetbrains.mps.baseLanguage.structure.DefaultClassCreator" flags="nn" index="HV5vD">
        <reference id="2820489544401957798" name="classifier" index="HV5vE" />
      </concept>
      <concept id="1197027756228" name="jetbrains.mps.baseLanguage.structure.DotExpression" flags="nn" index="2OqwBi">
        <child id="1197027771414" name="operand" index="2Oq$k0" />
        <child id="1197027833540" name="operation" index="2OqNvi" />
      </concept>
      <concept id="1164879751025" name="jetbrains.mps.baseLanguage.structure.TryCatchStatement" flags="nn" index="SfApY">
        <child id="1164879758292" name="body" index="SfCbr" />
        <child id="1164903496223" name="catchClause" index="TEbGg" />
      </concept>
      <concept id="1145552977093" name="jetbrains.mps.baseLanguage.structure.GenericNewExpression" flags="nn" index="2ShNRf">
        <child id="1145553007750" name="creator" index="2ShVmc" />
      </concept>
      <concept id="1164903280175" name="jetbrains.mps.baseLanguage.structure.CatchClause" flags="nn" index="TDmWw">
        <child id="1164903359218" name="catchBody" index="TDEfX" />
        <child id="1164903359217" name="throwable" index="TDEfY" />
      </concept>
      <concept id="1137021947720" name="jetbrains.mps.baseLanguage.structure.ConceptFunction" flags="in" index="2VMwT0">
        <child id="1137022507850" name="body" index="2VODD2" />
      </concept>
      <concept id="1070475926800" name="jetbrains.mps.baseLanguage.structure.StringLiteral" flags="nn" index="Xl_RD">
        <property id="1070475926801" name="value" index="Xl_RC" />
      </concept>
      <concept id="1182160077978" name="jetbrains.mps.baseLanguage.structure.AnonymousClassCreator" flags="nn" index="YeOm9">
        <child id="1182160096073" name="cls" index="YeSDq" />
      </concept>
      <concept id="1081236700938" name="jetbrains.mps.baseLanguage.structure.StaticMethodDeclaration" flags="ig" index="2YIFZL" />
      <concept id="1081236700937" name="jetbrains.mps.baseLanguage.structure.StaticMethodCall" flags="nn" index="2YIFZM">
        <reference id="1144433194310" name="classConcept" index="1Pybhc" />
      </concept>
      <concept id="1070533707846" name="jetbrains.mps.baseLanguage.structure.StaticFieldReference" flags="nn" index="10M0yZ">
        <reference id="1144433057691" name="classifier" index="1PxDUh" />
      </concept>
      <concept id="1070534058343" name="jetbrains.mps.baseLanguage.structure.NullLiteral" flags="nn" index="10Nm6u" />
      <concept id="1070534370425" name="jetbrains.mps.baseLanguage.structure.IntegerType" flags="in" index="10Oyi0" />
      <concept id="1070534760951" name="jetbrains.mps.baseLanguage.structure.ArrayType" flags="in" index="10Q1$e">
        <child id="1070534760952" name="componentType" index="10Q1$1" />
      </concept>
      <concept id="1068390468200" name="jetbrains.mps.baseLanguage.structure.FieldDeclaration" flags="ig" index="312cEg">
        <property id="8606350594693632173" name="isTransient" index="eg7rD" />
        <property id="1240249534625" name="isVolatile" index="34CwA1" />
      </concept>
      <concept id="1068390468198" name="jetbrains.mps.baseLanguage.structure.ClassConcept" flags="ig" index="312cEu">
        <child id="1165602531693" name="superclass" index="1zkMxy" />
      </concept>
      <concept id="1068431474542" name="jetbrains.mps.baseLanguage.structure.VariableDeclaration" flags="ng" index="33uBYm">
        <property id="1176718929932" name="isFinal" index="3TUv4t" />
        <child id="1068431790190" name="initializer" index="33vP2m" />
      </concept>
      <concept id="1068498886296" name="jetbrains.mps.baseLanguage.structure.VariableReference" flags="nn" index="37vLTw">
        <reference id="1068581517664" name="variableDeclaration" index="3cqZAo" />
      </concept>
      <concept id="1068498886292" name="jetbrains.mps.baseLanguage.structure.ParameterDeclaration" flags="ir" index="37vLTG" />
      <concept id="1068498886294" name="jetbrains.mps.baseLanguage.structure.AssignmentExpression" flags="nn" index="37vLTI" />
      <concept id="1225271177708" name="jetbrains.mps.baseLanguage.structure.StringType" flags="in" index="17QB3L" />
      <concept id="4972933694980447171" name="jetbrains.mps.baseLanguage.structure.BaseVariableDeclaration" flags="ng" index="19Szcq">
        <child id="5680397130376446158" name="type" index="1tU5fm" />
      </concept>
      <concept id="1068580123132" name="jetbrains.mps.baseLanguage.structure.BaseMethodDeclaration" flags="ng" index="3clF44">
        <property id="4276006055363816570" name="isSynchronized" index="od$2w" />
        <property id="1181808852946" name="isFinal" index="DiZV1" />
        <child id="1068580123133" name="returnType" index="3clF45" />
        <child id="1068580123134" name="parameter" index="3clF46" />
        <child id="1068580123135" name="body" index="3clF47" />
      </concept>
      <concept id="1068580123165" name="jetbrains.mps.baseLanguage.structure.InstanceMethodDeclaration" flags="ig" index="3clFb_">
        <property id="1178608670077" name="isAbstract" index="1EzhhJ" />
      </concept>
      <concept id="1068580123155" name="jetbrains.mps.baseLanguage.structure.ExpressionStatement" flags="nn" index="3clFbF">
        <child id="1068580123156" name="expression" index="3clFbG" />
      </concept>
      <concept id="1068580123136" name="jetbrains.mps.baseLanguage.structure.StatementList" flags="sn" stub="5293379017992965193" index="3clFbS">
        <child id="1068581517665" name="statement" index="3cqZAp" />
      </concept>
      <concept id="1068580123137" name="jetbrains.mps.baseLanguage.structure.BooleanConstant" flags="nn" index="3clFbT">
        <property id="1068580123138" name="value" index="3clFbU" />
      </concept>
      <concept id="1068580123140" name="jetbrains.mps.baseLanguage.structure.ConstructorDeclaration" flags="ig" index="3clFbW" />
      <concept id="1068580320020" name="jetbrains.mps.baseLanguage.structure.IntegerConstant" flags="nn" index="3cmrfG">
        <property id="1068580320021" name="value" index="3cmrfH" />
      </concept>
      <concept id="1068581242875" name="jetbrains.mps.baseLanguage.structure.PlusExpression" flags="nn" index="3cpWs3" />
      <concept id="1068581242864" name="jetbrains.mps.baseLanguage.structure.LocalVariableDeclarationStatement" flags="nn" index="3cpWs8">
        <child id="1068581242865" name="localVariableDeclaration" index="3cpWs9" />
      </concept>
      <concept id="1068581242863" name="jetbrains.mps.baseLanguage.structure.LocalVariableDeclaration" flags="nr" index="3cpWsn" />
      <concept id="1068581517677" name="jetbrains.mps.baseLanguage.structure.VoidType" flags="in" index="3cqZAl" />
      <concept id="1079359253375" name="jetbrains.mps.baseLanguage.structure.ParenthesizedExpression" flags="nn" index="1eOMI4">
        <child id="1079359253376" name="expression" index="1eOMHV" />
      </concept>
      <concept id="1204053956946" name="jetbrains.mps.baseLanguage.structure.IMethodCall" flags="ng" index="1ndlxa">
        <reference id="1068499141037" name="baseMethodDeclaration" index="37wK5l" />
        <child id="1068499141038" name="actualArgument" index="37wK5m" />
      </concept>
      <concept id="1212685548494" name="jetbrains.mps.baseLanguage.structure.ClassCreator" flags="nn" index="1pGfFk" />
      <concept id="1107461130800" name="jetbrains.mps.baseLanguage.structure.Classifier" flags="ng" index="3pOWGL">
        <property id="521412098689998745" name="nonStatic" index="2bfB8j" />
        <child id="5375687026011219971" name="member" index="jymVt" unordered="true" />
      </concept>
      <concept id="7812454656619025416" name="jetbrains.mps.baseLanguage.structure.MethodDeclaration" flags="ng" index="1rXfSm">
        <property id="8355037393041754995" name="isNative" index="2aFKle" />
      </concept>
      <concept id="7812454656619025412" name="jetbrains.mps.baseLanguage.structure.LocalMethodCall" flags="nn" index="1rXfSq" />
      <concept id="1107535904670" name="jetbrains.mps.baseLanguage.structure.ClassifierType" flags="in" index="3uibUv">
        <reference id="1107535924139" name="classifier" index="3uigEE" />
      </concept>
      <concept id="1081773326031" name="jetbrains.mps.baseLanguage.structure.BinaryOperation" flags="nn" index="3uHJSO">
        <child id="1081773367579" name="rightExpression" index="3uHU7w" />
        <child id="1081773367580" name="leftExpression" index="3uHU7B" />
      </concept>
      <concept id="1178549954367" name="jetbrains.mps.baseLanguage.structure.IVisible" flags="ng" index="1B3ioH">
        <child id="1178549979242" name="visibility" index="1B3o_S" />
      </concept>
      <concept id="1146644602865" name="jetbrains.mps.baseLanguage.structure.PublicVisibility" flags="nn" index="3Tm1VV" />
      <concept id="1146644623116" name="jetbrains.mps.baseLanguage.structure.PrivateVisibility" flags="nn" index="3Tm6S6" />
      <concept id="1170345865475" name="jetbrains.mps.baseLanguage.structure.AnonymousClass" flags="ig" index="1Y3b0j">
        <reference id="1170346070688" name="classifier" index="1Y3XeK" />
      </concept>
    </language>
    <language id="b401a680-8325-4110-8fd3-84331ff25bef" name="jetbrains.mps.lang.generator">
      <concept id="1114706874351" name="jetbrains.mps.lang.generator.structure.CopySrcNodeMacro" flags="ln" index="29HgVG">
        <child id="1168024447342" name="sourceNodeQuery" index="3NFExx" />
      </concept>
      <concept id="1095416546421" name="jetbrains.mps.lang.generator.structure.MappingConfiguration" flags="ig" index="bUwia">
        <child id="1200911492601" name="mappingLabel" index="2rTMjI" />
        <child id="1167328349397" name="reductionMappingRule" index="3acgRq" />
        <child id="1167514678247" name="rootMappingRule" index="3lj3bC" />
      </concept>
      <concept id="1168619357332" name="jetbrains.mps.lang.generator.structure.RootTemplateAnnotation" flags="lg" index="n94m4">
        <reference id="1168619429071" name="applicableConcept" index="n9lRv" />
      </concept>
      <concept id="1095672379244" name="jetbrains.mps.lang.generator.structure.TemplateFragment" flags="ng" index="raruj" />
      <concept id="1200911316486" name="jetbrains.mps.lang.generator.structure.MappingLabelDeclaration" flags="lg" index="2rT7sh">
        <reference id="1200911342686" name="sourceConcept" index="2rTdP9" />
        <reference id="1200913004646" name="targetConcept" index="2rZz_L" />
      </concept>
      <concept id="1167169188348" name="jetbrains.mps.lang.generator.structure.TemplateFunctionParameter_sourceNode" flags="nn" index="30H73N" />
      <concept id="1167169308231" name="jetbrains.mps.lang.generator.structure.BaseMappingRule" flags="ng" index="30H$t8">
        <reference id="1167169349424" name="applicableConcept" index="30HIoZ" />
      </concept>
      <concept id="1087833241328" name="jetbrains.mps.lang.generator.structure.PropertyMacro" flags="ln" index="17Uvod">
        <child id="1167756362303" name="propertyValueFunction" index="3zH0cK" />
      </concept>
      <concept id="1087833466690" name="jetbrains.mps.lang.generator.structure.NodeMacro" flags="lg" index="17VmuZ">
        <reference id="1200912223215" name="mappingLabel" index="2rW$FS" />
      </concept>
      <concept id="1167327847730" name="jetbrains.mps.lang.generator.structure.Reduction_MappingRule" flags="lg" index="3aamgX">
        <child id="1169672767469" name="ruleConsequence" index="1lVwrX" />
      </concept>
      <concept id="1167514355419" name="jetbrains.mps.lang.generator.structure.Root_MappingRule" flags="lg" index="3lhOvk">
        <reference id="1167514355421" name="template" index="3lhOvi" />
      </concept>
      <concept id="1131073187192" name="jetbrains.mps.lang.generator.structure.MapSrcNodeMacro" flags="ln" index="1pdMLZ" />
      <concept id="1167756080639" name="jetbrains.mps.lang.generator.structure.PropertyMacro_GetPropertyValue" flags="in" index="3zFVjK" />
      <concept id="1167770111131" name="jetbrains.mps.lang.generator.structure.ReferenceMacro_GetReferent" flags="in" index="3$xsQk" />
      <concept id="1167951910403" name="jetbrains.mps.lang.generator.structure.SourceSubstituteMacro_SourceNodesQuery" flags="in" index="3JmXsc" />
      <concept id="8900764248744213868" name="jetbrains.mps.lang.generator.structure.InlineTemplateWithContext_RuleConsequence" flags="lg" index="1Koe21">
        <child id="8900764248744213871" name="contentNode" index="1Koe22" />
      </concept>
      <concept id="1168024337012" name="jetbrains.mps.lang.generator.structure.SourceSubstituteMacro_SourceNodeQuery" flags="in" index="3NFfHV" />
      <concept id="1118786554307" name="jetbrains.mps.lang.generator.structure.LoopMacro" flags="ln" index="1WS0z7">
        <child id="1167952069335" name="sourceNodesQuery" index="3Jn$fo" />
      </concept>
      <concept id="1088761943574" name="jetbrains.mps.lang.generator.structure.ReferenceMacro" flags="ln" index="1ZhdrF">
        <child id="1167770376702" name="referentFunction" index="3$ytzL" />
      </concept>
    </language>
    <language id="d7706f63-9be2-479c-a3da-ae92af1e64d5" name="jetbrains.mps.lang.generator.generationContext">
      <concept id="1218047638031" name="jetbrains.mps.lang.generator.generationContext.structure.GenerationContextOp_CreateUniqueName" flags="nn" index="2piZGk">
        <child id="1218047638032" name="baseName" index="2piZGb" />
      </concept>
      <concept id="1216860049627" name="jetbrains.mps.lang.generator.generationContext.structure.GenerationContextOp_GetOutputByLabelAndInput" flags="nn" index="1iwH70">
        <reference id="1216860049628" name="label" index="1iwH77" />
        <child id="1216860049632" name="inputNode" index="1iwH7V" />
      </concept>
      <concept id="1216860049635" name="jetbrains.mps.lang.generator.generationContext.structure.TemplateFunctionParameter_generationContext" flags="nn" index="1iwH7S" />
    </language>
    <language id="7866978e-a0f0-4cc7-81bc-4d213d9375e1" name="jetbrains.mps.lang.smodel">
      <concept id="1138056022639" name="jetbrains.mps.lang.smodel.structure.SPropertyAccess" flags="nn" index="3TrcHB">
        <reference id="1138056395725" name="property" index="3TsBF5" />
      </concept>
      <concept id="1138056143562" name="jetbrains.mps.lang.smodel.structure.SLinkAccess" flags="nn" index="3TrEf2">
        <reference id="1138056516764" name="link" index="3Tt5mk" />
      </concept>
      <concept id="1138056282393" name="jetbrains.mps.lang.smodel.structure.SLinkListAccess" flags="nn" index="3Tsc0h">
        <reference id="1138056546658" name="link" index="3TtcxE" />
      </concept>
    </language>
    <language id="ceab5195-25ea-4f22-9b92-103b95ca8c0c" name="jetbrains.mps.lang.core">
      <concept id="1133920641626" name="jetbrains.mps.lang.core.structure.BaseConcept" flags="ng" index="2VYdi">
        <child id="5169995583184591170" name="smodelAttribute" index="lGtFl" />
      </concept>
      <concept id="3364660638048049750" name="jetbrains.mps.lang.core.structure.PropertyAttribute" flags="ng" index="A9Btg">
        <property id="1757699476691236117" name="propertyName" index="2qtEX9" />
        <property id="1341860900487648621" name="propertyId" index="P4ACc" />
      </concept>
      <concept id="3364660638048049745" name="jetbrains.mps.lang.core.structure.LinkAttribute" flags="ng" index="A9Btn">
        <property id="1757699476691236116" name="linkRole" index="2qtEX8" />
        <property id="1341860900488019036" name="linkId" index="P3scX" />
      </concept>
      <concept id="1169194658468" name="jetbrains.mps.lang.core.structure.INamedConcept" flags="ng" index="TrEIO">
        <property id="1169194664001" name="name" index="TrG5h" />
      </concept>
    </language>
  </registry>
  <node concept="bUwia" id="6VrRWu7ePGT">
    <property role="TrG5h" value="main" />
    <node concept="3lhOvk" id="6VrRWu7fogp" role="3lj3bC">
      <ref role="30HIoZ" to="xv7z:6VrRWu7ePH1" resolve="Calculator" />
      <ref role="3lhOvi" node="6VrRWu7fofb" resolve="CalculatorImpl" />
    </node>
    <node concept="2rT7sh" id="6VrRWu7hfZj" role="2rTMjI">
      <property role="TrG5h" value="InputFieldDeclaration" />
      <ref role="2rTdP9" to="xv7z:6VrRWu7eZHS" resolve="InputField" />
      <ref role="2rZz_L" to="tpee:fz12cDC" resolve="FieldDeclaration" />
    </node>
    <node concept="2rT7sh" id="6VrRWu7hUHF" role="2rTMjI">
      <property role="TrG5h" value="OutputFieldDeclaration" />
      <ref role="2rTdP9" to="xv7z:6VrRWu7f2mt" resolve="OutputField" />
      <ref role="2rZz_L" to="tpee:fz12cDC" resolve="FieldDeclaration" />
    </node>
    <node concept="2rT7sh" id="6VrRWu7hUHI" role="2rTMjI">
      <property role="TrG5h" value="LocalVar" />
      <ref role="2rTdP9" to="xv7z:6VrRWu7eZHS" resolve="InputField" />
      <ref role="2rZz_L" to="tpee:fzcpWvJ" resolve="LocalVariableDeclaration" />
    </node>
    <node concept="3aamgX" id="6VrRWu7iIwP" role="3acgRq">
      <ref role="30HIoZ" to="xv7z:6VrRWu7f92Z" resolve="InputFieldReference" />
      <node concept="1Koe21" id="6VrRWu7iIwT" role="1lVwrX">
        <node concept="9aQIb" id="6VrRWu7iIwX" role="1Koe22">
          <node concept="3clFbS" id="6VrRWu7iIx5" role="9aQI4">
            <node concept="3cpWs8" id="6VrRWu7iIx0" role="3cqZAp">
              <node concept="3cpWsn" id="6VrRWu7iIx3" role="3cpWs9">
                <property role="TrG5h" value="i" />
                <node concept="10Oyi0" id="6VrRWu7iIwZ" role="1tU5fm" />
              </node>
            </node>
            <node concept="3clFbF" id="6VrRWu7iIxz" role="3cqZAp">
              <node concept="37vLTI" id="6VrRWu7iJRl" role="3clFbG">
                <node concept="3cpWs3" id="6VrRWu7iKyE" role="37vLTx">
                  <node concept="37vLTw" id="6VrRWu7iKyH" role="3uHU7w">
                    <ref role="3cqZAo" node="6VrRWu7iIx3" resolve="i" />
                    <node concept="raruj" id="6VrRWu7iKUy" role="lGtFl" />
                    <node concept="1ZhdrF" id="6VrRWu7iLqP" role="lGtFl">
                      <property role="P3scX" value="f3061a53-9226-4cc5-a443-f952ceaf5816/1068498886296/1068581517664" />
                      <property role="2qtEX8" value="variableDeclaration" />
                      <node concept="3$xsQk" id="6VrRWu7iLqQ" role="3$ytzL">
                        <node concept="3clFbS" id="6VrRWu7iLqR" role="2VODD2">
                          <node concept="3clFbF" id="6VrRWu7iMbk" role="3cqZAp">
                            <node concept="2OqwBi" id="6VrRWu7iMns" role="3clFbG">
                              <node concept="1iwH7S" id="6VrRWu7iMbj" role="2Oq$k0" />
                              <node concept="1iwH70" id="6VrRWu7iMt3" role="2OqNvi">
                                <ref role="1iwH77" node="6VrRWu7hUHI" resolve="LocalVar" />
                                <node concept="2OqwBi" id="6VrRWu7iMU4" role="1iwH7V">
                                  <node concept="30H73N" id="6VrRWu7iMHY" role="2Oq$k0" />
                                  <node concept="3TrEf2" id="6VrRWu7iNeE" role="2OqNvi">
                                    <ref role="3Tt5mk" to="xv7z:6VrRWu7f930" resolve="field" />
                                  </node>
                                </node>
                              </node>
                            </node>
                          </node>
                        </node>
                      </node>
                    </node>
                  </node>
                  <node concept="3cmrfG" id="6VrRWu7iJRx" role="3uHU7B">
                    <property role="3cmrfH" value="1" />
                  </node>
                </node>
                <node concept="37vLTw" id="6VrRWu7iIxx" role="37vLTJ">
                  <ref role="3cqZAo" node="6VrRWu7iIx3" resolve="i" />
                </node>
              </node>
            </node>
          </node>
        </node>
      </node>
    </node>
  </node>
  <node concept="312cEu" id="6VrRWu7fofb">
    <property role="TrG5h" value="CalculatorImpl" />
    <node concept="312cEg" id="6VrRWu7fGdQ" role="jymVt">
      <property role="34CwA1" value="false" />
      <property role="eg7rD" value="false" />
      <property role="TrG5h" value="listener" />
      <property role="3TUv4t" value="false" />
      <node concept="3Tm6S6" id="6VrRWu7fFi1" role="1B3o_S" />
      <node concept="3uibUv" id="6VrRWu7fFRO" role="1tU5fm">
        <ref role="3uigEE" to="gsia:~DocumentListener" resolve="DocumentListener" />
      </node>
      <node concept="2ShNRf" id="6VrRWu7fH0I" role="33vP2m">
        <node concept="YeOm9" id="6VrRWu7fMJ_" role="2ShVmc">
          <node concept="1Y3b0j" id="6VrRWu7fMJC" role="YeSDq">
            <property role="2bfB8j" value="true" />
            <ref role="1Y3XeK" to="gsia:~DocumentListener" resolve="DocumentListener" />
            <ref role="37wK5l" to="wyt6:~Object.&lt;init&gt;()" resolve="Object" />
            <node concept="3Tm1VV" id="6VrRWu7fMJD" role="1B3o_S" />
            <node concept="3clFb_" id="6VrRWu7fMJE" role="jymVt">
              <property role="1EzhhJ" value="false" />
              <property role="TrG5h" value="insertUpdate" />
              <property role="DiZV1" value="false" />
              <property role="od$2w" value="false" />
              <node concept="3Tm1VV" id="6VrRWu7fMJF" role="1B3o_S" />
              <node concept="3cqZAl" id="6VrRWu7fMJH" role="3clF45" />
              <node concept="37vLTG" id="6VrRWu7fMJI" role="3clF46">
                <property role="TrG5h" value="p0" />
                <node concept="3uibUv" id="6VrRWu7fMJJ" role="1tU5fm">
                  <ref role="3uigEE" to="gsia:~DocumentEvent" resolve="DocumentEvent" />
                </node>
              </node>
              <node concept="3clFbS" id="6VrRWu7fMJK" role="3clF47">
                <node concept="3clFbF" id="6VrRWu7fQ6P" role="3cqZAp">
                  <node concept="1rXfSq" id="6VrRWu7fQ6O" role="3clFbG">
                    <ref role="37wK5l" node="6VrRWu7fNKC" resolve="update" />
                  </node>
                </node>
              </node>
            </node>
            <node concept="3clFb_" id="6VrRWu7fMJM" role="jymVt">
              <property role="1EzhhJ" value="false" />
              <property role="TrG5h" value="removeUpdate" />
              <property role="DiZV1" value="false" />
              <property role="od$2w" value="false" />
              <node concept="3Tm1VV" id="6VrRWu7fMJN" role="1B3o_S" />
              <node concept="3cqZAl" id="6VrRWu7fMJP" role="3clF45" />
              <node concept="37vLTG" id="6VrRWu7fMJQ" role="3clF46">
                <property role="TrG5h" value="p0" />
                <node concept="3uibUv" id="6VrRWu7fMJR" role="1tU5fm">
                  <ref role="3uigEE" to="gsia:~DocumentEvent" resolve="DocumentEvent" />
                </node>
              </node>
              <node concept="3clFbS" id="6VrRWu7fMJS" role="3clF47">
                <node concept="3clFbF" id="6VrRWu7fQ92" role="3cqZAp">
                  <node concept="1rXfSq" id="6VrRWu7fQ93" role="3clFbG">
                    <ref role="37wK5l" node="6VrRWu7fNKC" resolve="update" />
                  </node>
                </node>
              </node>
            </node>
            <node concept="3clFb_" id="6VrRWu7fMJU" role="jymVt">
              <property role="1EzhhJ" value="false" />
              <property role="TrG5h" value="changedUpdate" />
              <property role="DiZV1" value="false" />
              <property role="od$2w" value="false" />
              <node concept="3Tm1VV" id="6VrRWu7fMJV" role="1B3o_S" />
              <node concept="3cqZAl" id="6VrRWu7fMJX" role="3clF45" />
              <node concept="37vLTG" id="6VrRWu7fMJY" role="3clF46">
                <property role="TrG5h" value="p0" />
                <node concept="3uibUv" id="6VrRWu7fMJZ" role="1tU5fm">
                  <ref role="3uigEE" to="gsia:~DocumentEvent" resolve="DocumentEvent" />
                </node>
              </node>
              <node concept="3clFbS" id="6VrRWu7fMK0" role="3clF47">
                <node concept="3clFbF" id="6VrRWu7fQa2" role="3cqZAp">
                  <node concept="1rXfSq" id="6VrRWu7fQa3" role="3clFbG">
                    <ref role="37wK5l" node="6VrRWu7fNKC" resolve="update" />
                  </node>
                </node>
              </node>
            </node>
          </node>
        </node>
      </node>
    </node>
    <node concept="2tJIrI" id="6VrRWu7grPF" role="jymVt" />
    <node concept="312cEg" id="6VrRWu7gDvY" role="jymVt">
      <property role="34CwA1" value="false" />
      <property role="eg7rD" value="false" />
      <property role="TrG5h" value="inputField" />
      <property role="3TUv4t" value="false" />
      <node concept="3Tm6S6" id="6VrRWu7gDvZ" role="1B3o_S" />
      <node concept="3uibUv" id="6VrRWu7gDw0" role="1tU5fm">
        <ref role="3uigEE" to="dxuu:~JTextField" resolve="JTextField" />
      </node>
      <node concept="2ShNRf" id="6VrRWu7gDw1" role="33vP2m">
        <node concept="1pGfFk" id="6VrRWu7gDw2" role="2ShVmc">
          <ref role="37wK5l" to="dxuu:~JTextField.&lt;init&gt;()" resolve="JTextField" />
        </node>
      </node>
      <node concept="1WS0z7" id="6VrRWu7gDw3" role="lGtFl">
        <ref role="2rW$FS" node="6VrRWu7hfZj" resolve="InputFieldDeclaration" />
        <node concept="3JmXsc" id="6VrRWu7gDw4" role="3Jn$fo">
          <node concept="3clFbS" id="6VrRWu7gDw5" role="2VODD2">
            <node concept="3clFbF" id="6VrRWu7gDw6" role="3cqZAp">
              <node concept="2OqwBi" id="6VrRWu7gDw7" role="3clFbG">
                <node concept="30H73N" id="6VrRWu7gDw8" role="2Oq$k0" />
                <node concept="3Tsc0h" id="6VrRWu7gDw9" role="2OqNvi">
                  <ref role="3TtcxE" to="xv7z:6VrRWu7eZId" resolve="inputFields" />
                </node>
              </node>
            </node>
          </node>
        </node>
      </node>
      <node concept="17Uvod" id="6VrRWu7gDwa" role="lGtFl">
        <property role="P4ACc" value="ceab5195-25ea-4f22-9b92-103b95ca8c0c/1169194658468/1169194664001" />
        <property role="2qtEX9" value="name" />
        <node concept="3zFVjK" id="6VrRWu7gDwb" role="3zH0cK">
          <node concept="3clFbS" id="6VrRWu7gDwc" role="2VODD2">
            <node concept="3clFbF" id="6VrRWu7gDwd" role="3cqZAp">
              <node concept="2OqwBi" id="6VrRWu7gDwe" role="3clFbG">
                <node concept="1iwH7S" id="6VrRWu7gDwf" role="2Oq$k0" />
                <node concept="2piZGk" id="6VrRWu7gDwg" role="2OqNvi">
                  <node concept="Xl_RD" id="6VrRWu7gDwh" role="2piZGb">
                    <property role="Xl_RC" value="inputField" />
                  </node>
                </node>
              </node>
            </node>
          </node>
        </node>
      </node>
    </node>
    <node concept="312cEg" id="6VrRWu7gJyN" role="jymVt">
      <property role="34CwA1" value="false" />
      <property role="eg7rD" value="false" />
      <property role="TrG5h" value="outputField" />
      <property role="3TUv4t" value="false" />
      <node concept="3Tm6S6" id="6VrRWu7gHpv" role="1B3o_S" />
      <node concept="3uibUv" id="6VrRWu7gJl5" role="1tU5fm">
        <ref role="3uigEE" to="dxuu:~JTextField" resolve="JTextField" />
      </node>
      <node concept="2ShNRf" id="6VrRWu7gKGr" role="33vP2m">
        <node concept="1pGfFk" id="6VrRWu7gMyM" role="2ShVmc">
          <ref role="37wK5l" to="dxuu:~JTextField.&lt;init&gt;()" resolve="JTextField" />
        </node>
      </node>
      <node concept="1WS0z7" id="6VrRWu7gMGG" role="lGtFl">
        <ref role="2rW$FS" node="6VrRWu7hUHF" resolve="OutputFieldDeclaration" />
        <node concept="3JmXsc" id="6VrRWu7gMGJ" role="3Jn$fo">
          <node concept="3clFbS" id="6VrRWu7gMGK" role="2VODD2">
            <node concept="3clFbF" id="6VrRWu7gMGQ" role="3cqZAp">
              <node concept="2OqwBi" id="6VrRWu7gMGL" role="3clFbG">
                <node concept="3Tsc0h" id="6VrRWu7gMGO" role="2OqNvi">
                  <ref role="3TtcxE" to="xv7z:6VrRWu7f2mM" resolve="outputFields" />
                </node>
                <node concept="30H73N" id="6VrRWu7gMGP" role="2Oq$k0" />
              </node>
            </node>
          </node>
        </node>
      </node>
      <node concept="17Uvod" id="6VrRWu7gMXa" role="lGtFl">
        <property role="P4ACc" value="ceab5195-25ea-4f22-9b92-103b95ca8c0c/1169194658468/1169194664001" />
        <property role="2qtEX9" value="name" />
        <node concept="3zFVjK" id="6VrRWu7gMXb" role="3zH0cK">
          <node concept="3clFbS" id="6VrRWu7gMXc" role="2VODD2">
            <node concept="3clFbF" id="6VrRWu7gNCk" role="3cqZAp">
              <node concept="2OqwBi" id="6VrRWu7gNCl" role="3clFbG">
                <node concept="1iwH7S" id="6VrRWu7gNCm" role="2Oq$k0" />
                <node concept="2piZGk" id="6VrRWu7gNCn" role="2OqNvi">
                  <node concept="Xl_RD" id="6VrRWu7gNCo" role="2piZGb">
                    <property role="Xl_RC" value="outputField" />
                  </node>
                </node>
              </node>
            </node>
          </node>
        </node>
      </node>
    </node>
    <node concept="3clFbW" id="6VrRWu7g5xK" role="jymVt">
      <node concept="3cqZAl" id="6VrRWu7g5xL" role="3clF45" />
      <node concept="3clFbS" id="6VrRWu7g5xN" role="3clF47">
        <node concept="3clFbF" id="6VrRWu7g7wx" role="3cqZAp">
          <node concept="1rXfSq" id="6VrRWu7g7ww" role="3clFbG">
            <ref role="37wK5l" to="z60i:~Frame.setTitle(java.lang.String):void" resolve="setTitle" />
            <node concept="Xl_RD" id="6VrRWu7g8am" role="37wK5m">
              <property role="Xl_RC" value="Calculator" />
              <node concept="17Uvod" id="6VrRWu7gpLX" role="lGtFl">
                <property role="P4ACc" value="f3061a53-9226-4cc5-a443-f952ceaf5816/1070475926800/1070475926801" />
                <property role="2qtEX9" value="value" />
                <node concept="3zFVjK" id="6VrRWu7gpLY" role="3zH0cK">
                  <node concept="3clFbS" id="6VrRWu7gpLZ" role="2VODD2">
                    <node concept="3clFbF" id="6VrRWu7gqUI" role="3cqZAp">
                      <node concept="2OqwBi" id="6VrRWu7gr8_" role="3clFbG">
                        <node concept="30H73N" id="6VrRWu7gqUH" role="2Oq$k0" />
                        <node concept="3TrcHB" id="6VrRWu7grpE" role="2OqNvi">
                          <ref role="3TsBF5" to="tpck:h0TrG11" resolve="name" />
                        </node>
                      </node>
                    </node>
                  </node>
                </node>
              </node>
            </node>
          </node>
        </node>
        <node concept="3clFbF" id="6VrRWu7g9QU" role="3cqZAp">
          <node concept="1rXfSq" id="6VrRWu7g9QS" role="3clFbG">
            <ref role="37wK5l" to="dxuu:~JFrame.setLayout(java.awt.LayoutManager):void" resolve="setLayout" />
            <node concept="2ShNRf" id="6VrRWu7gawZ" role="37wK5m">
              <node concept="1pGfFk" id="6VrRWu7gcmL" role="2ShVmc">
                <ref role="37wK5l" to="z60i:~GridLayout.&lt;init&gt;(int,int)" resolve="GridLayout" />
                <node concept="3cmrfG" id="6VrRWu7gd0_" role="37wK5m">
                  <property role="3cmrfH" value="0" />
                </node>
                <node concept="3cmrfG" id="6VrRWu7gfJf" role="37wK5m">
                  <property role="3cmrfH" value="2" />
                </node>
              </node>
            </node>
          </node>
        </node>
        <node concept="9aQIb" id="6VrRWu7gVZ4" role="3cqZAp">
          <node concept="3clFbS" id="6VrRWu7gVZ6" role="9aQI4">
            <node concept="3clFbF" id="6VrRWu7gXPt" role="3cqZAp">
              <node concept="2OqwBi" id="6VrRWu7h1$E" role="3clFbG">
                <node concept="2OqwBi" id="6VrRWu7gZ5A" role="2Oq$k0">
                  <node concept="37vLTw" id="6VrRWu7gXPr" role="2Oq$k0">
                    <ref role="3cqZAo" node="6VrRWu7gDvY" resolve="inputField" />
                    <node concept="1ZhdrF" id="6VrRWu7hh47" role="lGtFl">
                      <property role="P3scX" value="f3061a53-9226-4cc5-a443-f952ceaf5816/1068498886296/1068581517664" />
                      <property role="2qtEX8" value="variableDeclaration" />
                      <node concept="3$xsQk" id="6VrRWu7hh48" role="3$ytzL">
                        <node concept="3clFbS" id="6VrRWu7hh49" role="2VODD2">
                          <node concept="3clFbF" id="6VrRWu7hjqa" role="3cqZAp">
                            <node concept="2OqwBi" id="6VrRWu7hkqD" role="3clFbG">
                              <node concept="1iwH7S" id="6VrRWu7hjq9" role="2Oq$k0" />
                              <node concept="1iwH70" id="6VrRWu7hk$$" role="2OqNvi">
                                <ref role="1iwH77" node="6VrRWu7hfZj" resolve="InputFieldDeclaration" />
                                <node concept="30H73N" id="6VrRWu7hmaM" role="1iwH7V" />
                              </node>
                            </node>
                          </node>
                        </node>
                      </node>
                    </node>
                  </node>
                  <node concept="liA8E" id="6VrRWu7h1il" role="2OqNvi">
                    <ref role="37wK5l" to="r791:~JTextComponent.getDocument():javax.swing.text.Document" resolve="getDocument" />
                  </node>
                </node>
                <node concept="liA8E" id="6VrRWu7h2mG" role="2OqNvi">
                  <ref role="37wK5l" to="r791:~Document.addDocumentListener(javax.swing.event.DocumentListener):void" resolve="addDocumentListener" />
                  <node concept="37vLTw" id="6VrRWu7h3Og" role="37wK5m">
                    <ref role="3cqZAo" node="6VrRWu7fGdQ" resolve="listener" />
                  </node>
                </node>
              </node>
            </node>
            <node concept="3clFbF" id="6VrRWu7h4YB" role="3cqZAp">
              <node concept="1rXfSq" id="6VrRWu7h4Y_" role="3clFbG">
                <ref role="37wK5l" to="z60i:~Container.add(java.awt.Component):java.awt.Component" resolve="add" />
                <node concept="2ShNRf" id="6VrRWu7h5Hb" role="37wK5m">
                  <node concept="1pGfFk" id="6VrRWu7h7Bd" role="2ShVmc">
                    <ref role="37wK5l" to="dxuu:~JLabel.&lt;init&gt;(java.lang.String)" resolve="JLabel" />
                    <node concept="Xl_RD" id="6VrRWu7h8kZ" role="37wK5m">
                      <property role="Xl_RC" value="Title" />
                      <node concept="17Uvod" id="6VrRWu7hfH9" role="lGtFl">
                        <property role="P4ACc" value="f3061a53-9226-4cc5-a443-f952ceaf5816/1070475926800/1070475926801" />
                        <property role="2qtEX9" value="value" />
                        <node concept="3zFVjK" id="6VrRWu7hfHc" role="3zH0cK">
                          <node concept="3clFbS" id="6VrRWu7hfHd" role="2VODD2">
                            <node concept="3clFbF" id="6VrRWu7hfHj" role="3cqZAp">
                              <node concept="2OqwBi" id="6VrRWu7hfHe" role="3clFbG">
                                <node concept="3TrcHB" id="6VrRWu7hfHh" role="2OqNvi">
                                  <ref role="3TsBF5" to="tpck:h0TrG11" resolve="name" />
                                </node>
                                <node concept="30H73N" id="6VrRWu7hfHi" role="2Oq$k0" />
                              </node>
                            </node>
                          </node>
                        </node>
                      </node>
                    </node>
                  </node>
                </node>
              </node>
            </node>
            <node concept="3clFbF" id="6VrRWu7h9FY" role="3cqZAp">
              <node concept="1rXfSq" id="6VrRWu7h9FW" role="3clFbG">
                <ref role="37wK5l" to="z60i:~Container.add(java.awt.Component):java.awt.Component" resolve="add" />
                <node concept="37vLTw" id="6VrRWu7hb7U" role="37wK5m">
                  <ref role="3cqZAo" node="6VrRWu7gDvY" resolve="inputField" />
                  <node concept="1ZhdrF" id="6VrRWu7hmKr" role="lGtFl">
                    <property role="P3scX" value="f3061a53-9226-4cc5-a443-f952ceaf5816/1068498886296/1068581517664" />
                    <property role="2qtEX8" value="variableDeclaration" />
                    <node concept="3$xsQk" id="6VrRWu7hmKs" role="3$ytzL">
                      <node concept="3clFbS" id="6VrRWu7hmKt" role="2VODD2">
                        <node concept="3clFbF" id="6VrRWu7hoPp" role="3cqZAp">
                          <node concept="2OqwBi" id="6VrRWu7hpDo" role="3clFbG">
                            <node concept="1iwH7S" id="6VrRWu7hoPo" role="2Oq$k0" />
                            <node concept="1iwH70" id="6VrRWu7hEMP" role="2OqNvi">
                              <ref role="1iwH77" node="6VrRWu7hfZj" resolve="InputFieldDeclaration" />
                              <node concept="30H73N" id="6VrRWu7hG4Y" role="1iwH7V" />
                            </node>
                          </node>
                        </node>
                      </node>
                    </node>
                  </node>
                </node>
              </node>
            </node>
          </node>
          <node concept="1WS0z7" id="6VrRWu7hbSh" role="lGtFl">
            <node concept="3JmXsc" id="6VrRWu7hbSj" role="3Jn$fo">
              <node concept="3clFbS" id="6VrRWu7hbSl" role="2VODD2">
                <node concept="3clFbF" id="6VrRWu7hdhC" role="3cqZAp">
                  <node concept="2OqwBi" id="6VrRWu7hdtM" role="3clFbG">
                    <node concept="30H73N" id="6VrRWu7hdhB" role="2Oq$k0" />
                    <node concept="3Tsc0h" id="6VrRWu7henl" role="2OqNvi">
                      <ref role="3TtcxE" to="xv7z:6VrRWu7eZId" resolve="inputFields" />
                    </node>
                  </node>
                </node>
              </node>
            </node>
          </node>
        </node>
        <node concept="3clFbF" id="6VrRWu7ghrW" role="3cqZAp">
          <node concept="1rXfSq" id="6VrRWu7ghrU" role="3clFbG">
            <ref role="37wK5l" node="6VrRWu7fNKC" resolve="update" />
          </node>
        </node>
        <node concept="3clFbF" id="6VrRWu7gjbm" role="3cqZAp">
          <node concept="1rXfSq" id="6VrRWu7gjbk" role="3clFbG">
            <ref role="37wK5l" to="dxuu:~JFrame.setDefaultCloseOperation(int):void" resolve="setDefaultCloseOperation" />
            <node concept="10M0yZ" id="6VrRWu7glAK" role="37wK5m">
              <ref role="3cqZAo" to="dxuu:~JFrame.EXIT_ON_CLOSE" resolve="EXIT_ON_CLOSE" />
              <ref role="1PxDUh" to="dxuu:~JFrame" resolve="JFrame" />
            </node>
          </node>
        </node>
        <node concept="3clFbF" id="6VrRWu7gnk0" role="3cqZAp">
          <node concept="1rXfSq" id="6VrRWu7gnjY" role="3clFbG">
            <ref role="37wK5l" to="z60i:~Window.pack():void" resolve="pack" />
          </node>
        </node>
        <node concept="3clFbF" id="6VrRWu7gp3B" role="3cqZAp">
          <node concept="1rXfSq" id="6VrRWu7gp3_" role="3clFbG">
            <ref role="37wK5l" to="z60i:~Window.setVisible(boolean):void" resolve="setVisible" />
            <node concept="3clFbT" id="6VrRWu7gpJZ" role="37wK5m">
              <property role="3clFbU" value="true" />
            </node>
          </node>
        </node>
      </node>
      <node concept="3Tm1VV" id="6VrRWu7g4EL" role="1B3o_S" />
    </node>
    <node concept="3clFb_" id="6VrRWu7fNKC" role="jymVt">
      <property role="1EzhhJ" value="false" />
      <property role="TrG5h" value="update" />
      <property role="od$2w" value="false" />
      <property role="DiZV1" value="false" />
      <property role="2aFKle" value="false" />
      <node concept="3clFbS" id="6VrRWu7fNKF" role="3clF47">
        <node concept="3cpWs8" id="6VrRWu7hNsg" role="3cqZAp">
          <node concept="3cpWsn" id="6VrRWu7hNsj" role="3cpWs9">
            <property role="TrG5h" value="i" />
            <node concept="10Oyi0" id="6VrRWu7hNsf" role="1tU5fm" />
            <node concept="3cmrfG" id="6VrRWu7hO4X" role="33vP2m">
              <property role="3cmrfH" value="0" />
            </node>
            <node concept="17Uvod" id="6VrRWu7hPdq" role="lGtFl">
              <property role="P4ACc" value="ceab5195-25ea-4f22-9b92-103b95ca8c0c/1169194658468/1169194664001" />
              <property role="2qtEX9" value="name" />
              <node concept="3zFVjK" id="6VrRWu7hPdr" role="3zH0cK">
                <node concept="3clFbS" id="6VrRWu7hPds" role="2VODD2">
                  <node concept="3clFbF" id="6VrRWu7hQX8" role="3cqZAp">
                    <node concept="2OqwBi" id="6VrRWu7hRPH" role="3clFbG">
                      <node concept="1iwH7S" id="6VrRWu7hQX7" role="2Oq$k0" />
                      <node concept="2piZGk" id="6VrRWu7hTqg" role="2OqNvi">
                        <node concept="Xl_RD" id="6VrRWu7hUaZ" role="2piZGb">
                          <property role="Xl_RC" value="i" />
                        </node>
                      </node>
                    </node>
                  </node>
                </node>
              </node>
            </node>
            <node concept="1pdMLZ" id="6VrRWu7hV5N" role="lGtFl">
              <ref role="2rW$FS" node="6VrRWu7hUHI" resolve="LocalVar" />
            </node>
          </node>
          <node concept="1WS0z7" id="6VrRWu7hOPS" role="lGtFl">
            <node concept="3JmXsc" id="6VrRWu7hOPV" role="3Jn$fo">
              <node concept="3clFbS" id="6VrRWu7hOPW" role="2VODD2">
                <node concept="3clFbF" id="6VrRWu7hOQ2" role="3cqZAp">
                  <node concept="2OqwBi" id="6VrRWu7hOPX" role="3clFbG">
                    <node concept="3Tsc0h" id="6VrRWu7hOQ0" role="2OqNvi">
                      <ref role="3TtcxE" to="xv7z:6VrRWu7eZId" resolve="inputFields" />
                    </node>
                    <node concept="30H73N" id="6VrRWu7hOQ1" role="2Oq$k0" />
                  </node>
                </node>
              </node>
            </node>
          </node>
        </node>
        <node concept="SfApY" id="6VrRWu7hXEe" role="3cqZAp">
          <node concept="3clFbS" id="6VrRWu7hXEg" role="SfCbr">
            <node concept="3clFbF" id="6VrRWu7i5Pz" role="3cqZAp">
              <node concept="37vLTI" id="6VrRWu7i79Z" role="3clFbG">
                <node concept="2YIFZM" id="6VrRWu7i8uM" role="37vLTx">
                  <ref role="37wK5l" to="wyt6:~Integer.parseInt(java.lang.String):int" resolve="parseInt" />
                  <ref role="1Pybhc" to="wyt6:~Integer" resolve="Integer" />
                  <node concept="2OqwBi" id="6VrRWu7ib2x" role="37wK5m">
                    <node concept="37vLTw" id="6VrRWu7i9Kw" role="2Oq$k0">
                      <ref role="3cqZAo" node="6VrRWu7gDvY" resolve="inputField" />
                      <node concept="1ZhdrF" id="6VrRWu7ilUF" role="lGtFl">
                        <property role="P3scX" value="f3061a53-9226-4cc5-a443-f952ceaf5816/1068498886296/1068581517664" />
                        <property role="2qtEX8" value="variableDeclaration" />
                        <node concept="3$xsQk" id="6VrRWu7ilUG" role="3$ytzL">
                          <node concept="3clFbS" id="6VrRWu7ilUH" role="2VODD2">
                            <node concept="3clFbF" id="6VrRWu7io3F" role="3cqZAp">
                              <node concept="2OqwBi" id="6VrRWu7ioTy" role="3clFbG">
                                <node concept="1iwH7S" id="6VrRWu7io3E" role="2Oq$k0" />
                                <node concept="1iwH70" id="6VrRWu7ip4R" role="2OqNvi">
                                  <ref role="1iwH77" node="6VrRWu7hfZj" resolve="InputFieldDeclaration" />
                                  <node concept="30H73N" id="6VrRWu7iqCk" role="1iwH7V" />
                                </node>
                              </node>
                            </node>
                          </node>
                        </node>
                      </node>
                    </node>
                    <node concept="liA8E" id="6VrRWu7idh6" role="2OqNvi">
                      <ref role="37wK5l" to="r791:~JTextComponent.getText():java.lang.String" resolve="getText" />
                    </node>
                  </node>
                </node>
                <node concept="37vLTw" id="6VrRWu7i5Py" role="37vLTJ">
                  <ref role="3cqZAo" node="6VrRWu7hNsj" resolve="i" />
                  <node concept="1ZhdrF" id="6VrRWu7ifC1" role="lGtFl">
                    <property role="P3scX" value="f3061a53-9226-4cc5-a443-f952ceaf5816/1068498886296/1068581517664" />
                    <property role="2qtEX8" value="variableDeclaration" />
                    <node concept="3$xsQk" id="6VrRWu7ifC2" role="3$ytzL">
                      <node concept="3clFbS" id="6VrRWu7ifC3" role="2VODD2">
                        <node concept="3clFbF" id="6VrRWu7iilp" role="3cqZAp">
                          <node concept="2OqwBi" id="6VrRWu7ijgK" role="3clFbG">
                            <node concept="1iwH7S" id="6VrRWu7iilo" role="2Oq$k0" />
                            <node concept="1iwH70" id="6VrRWu7ijTL" role="2OqNvi">
                              <ref role="1iwH77" node="6VrRWu7hUHI" resolve="LocalVar" />
                              <node concept="30H73N" id="6VrRWu7ilth" role="1iwH7V" />
                            </node>
                          </node>
                        </node>
                      </node>
                    </node>
                  </node>
                </node>
              </node>
              <node concept="1WS0z7" id="6VrRWu7if9g" role="lGtFl">
                <node concept="3JmXsc" id="6VrRWu7if9j" role="3Jn$fo">
                  <node concept="3clFbS" id="6VrRWu7if9k" role="2VODD2">
                    <node concept="3clFbF" id="6VrRWu7if9q" role="3cqZAp">
                      <node concept="2OqwBi" id="6VrRWu7if9l" role="3clFbG">
                        <node concept="3Tsc0h" id="6VrRWu7if9o" role="2OqNvi">
                          <ref role="3TtcxE" to="xv7z:6VrRWu7eZId" resolve="inputFields" />
                        </node>
                        <node concept="30H73N" id="6VrRWu7if9p" role="2Oq$k0" />
                      </node>
                    </node>
                  </node>
                </node>
              </node>
            </node>
          </node>
          <node concept="TDmWw" id="6VrRWu7hXEh" role="TEbGg">
            <node concept="3cpWsn" id="6VrRWu7hXEj" role="TDEfY">
              <property role="TrG5h" value="e" />
              <node concept="3uibUv" id="6VrRWu7hYaM" role="1tU5fm">
                <ref role="3uigEE" to="wyt6:~NumberFormatException" resolve="NumberFormatException" />
              </node>
            </node>
            <node concept="3clFbS" id="6VrRWu7hXEn" role="TDEfX" />
          </node>
        </node>
        <node concept="3clFbF" id="6VrRWu7is0v" role="3cqZAp">
          <node concept="2OqwBi" id="6VrRWu7ityA" role="3clFbG">
            <node concept="37vLTw" id="6VrRWu7is0t" role="2Oq$k0">
              <ref role="3cqZAo" node="6VrRWu7gJyN" resolve="outputField" />
              <node concept="1ZhdrF" id="6VrRWu7ixW9" role="lGtFl">
                <property role="P3scX" value="f3061a53-9226-4cc5-a443-f952ceaf5816/1068498886296/1068581517664" />
                <property role="2qtEX8" value="variableDeclaration" />
                <node concept="3$xsQk" id="6VrRWu7ixWa" role="3$ytzL">
                  <node concept="3clFbS" id="6VrRWu7ixWb" role="2VODD2">
                    <node concept="3clFbF" id="6VrRWu7i$2_" role="3cqZAp">
                      <node concept="2OqwBi" id="6VrRWu7i$PV" role="3clFbG">
                        <node concept="1iwH7S" id="6VrRWu7i$2$" role="2Oq$k0" />
                        <node concept="1iwH70" id="6VrRWu7i_7r" role="2OqNvi">
                          <ref role="1iwH77" node="6VrRWu7hUHF" resolve="OutputFieldDeclaration" />
                          <node concept="30H73N" id="6VrRWu7iBkl" role="1iwH7V" />
                        </node>
                      </node>
                    </node>
                  </node>
                </node>
              </node>
            </node>
            <node concept="liA8E" id="6VrRWu7iuN9" role="2OqNvi">
              <ref role="37wK5l" to="r791:~JTextComponent.setText(java.lang.String):void" resolve="setText" />
              <node concept="3cpWs3" id="6VrRWu7iEGA" role="37wK5m">
                <node concept="Xl_RD" id="6VrRWu7iG6$" role="3uHU7B">
                  <property role="Xl_RC" value="" />
                </node>
                <node concept="1eOMI4" id="6VrRWu7iHLi" role="3uHU7w">
                  <node concept="10Nm6u" id="6VrRWu7iwhs" role="1eOMHV">
                    <node concept="29HgVG" id="6VrRWu7iIcs" role="lGtFl">
                      <node concept="3NFfHV" id="6VrRWu7iIct" role="3NFExx">
                        <node concept="3clFbS" id="6VrRWu7iIcu" role="2VODD2">
                          <node concept="3clFbF" id="6VrRWu7iIc$" role="3cqZAp">
                            <node concept="2OqwBi" id="6VrRWu7iIcv" role="3clFbG">
                              <node concept="3TrEf2" id="6VrRWu7iIcy" role="2OqNvi">
                                <ref role="3Tt5mk" to="xv7z:6VrRWu7f48z" resolve="expression" />
                              </node>
                              <node concept="30H73N" id="6VrRWu7iIcz" role="2Oq$k0" />
                            </node>
                          </node>
                        </node>
                      </node>
                    </node>
                  </node>
                </node>
              </node>
            </node>
          </node>
          <node concept="1WS0z7" id="6VrRWu7iw_x" role="lGtFl">
            <node concept="3JmXsc" id="6VrRWu7iw_$" role="3Jn$fo">
              <node concept="3clFbS" id="6VrRWu7iw__" role="2VODD2">
                <node concept="3clFbF" id="6VrRWu7iw_F" role="3cqZAp">
                  <node concept="2OqwBi" id="6VrRWu7iw_A" role="3clFbG">
                    <node concept="3Tsc0h" id="6VrRWu7iw_D" role="2OqNvi">
                      <ref role="3TtcxE" to="xv7z:6VrRWu7f2mM" resolve="outputFields" />
                    </node>
                    <node concept="30H73N" id="6VrRWu7iw_E" role="2Oq$k0" />
                  </node>
                </node>
              </node>
            </node>
          </node>
        </node>
      </node>
      <node concept="3Tm1VV" id="6VrRWu7fNk5" role="1B3o_S" />
      <node concept="3cqZAl" id="6VrRWu7fNHN" role="3clF45" />
    </node>
    <node concept="2YIFZL" id="6VrRWu7fRkE" role="jymVt">
      <property role="TrG5h" value="main" />
      <property role="od$2w" value="false" />
      <property role="DiZV1" value="false" />
      <property role="2aFKle" value="false" />
      <node concept="3clFbS" id="6VrRWu7fRkH" role="3clF47">
        <node concept="3clFbF" id="6VrRWu7fTXb" role="3cqZAp">
          <node concept="2YIFZM" id="6VrRWu7fUAT" role="3clFbG">
            <ref role="37wK5l" to="dxuu:~SwingUtilities.invokeLater(java.lang.Runnable):void" resolve="invokeLater" />
            <ref role="1Pybhc" to="dxuu:~SwingUtilities" resolve="SwingUtilities" />
            <node concept="2ShNRf" id="6VrRWu7fVfc" role="37wK5m">
              <node concept="YeOm9" id="6VrRWu7fX4Q" role="2ShVmc">
                <node concept="1Y3b0j" id="6VrRWu7fX4T" role="YeSDq">
                  <property role="2bfB8j" value="true" />
                  <ref role="1Y3XeK" to="wyt6:~Runnable" resolve="Runnable" />
                  <ref role="37wK5l" to="wyt6:~Object.&lt;init&gt;()" resolve="Object" />
                  <node concept="3Tm1VV" id="6VrRWu7fX4U" role="1B3o_S" />
                  <node concept="3clFb_" id="6VrRWu7fX4V" role="jymVt">
                    <property role="1EzhhJ" value="false" />
                    <property role="TrG5h" value="run" />
                    <property role="DiZV1" value="false" />
                    <property role="od$2w" value="false" />
                    <node concept="3Tm1VV" id="6VrRWu7fX4W" role="1B3o_S" />
                    <node concept="3cqZAl" id="6VrRWu7fX4Y" role="3clF45" />
                    <node concept="3clFbS" id="6VrRWu7fX4Z" role="3clF47">
                      <node concept="3clFbF" id="6VrRWu7fY5_" role="3cqZAp">
                        <node concept="2ShNRf" id="6VrRWu7fY5z" role="3clFbG">
                          <node concept="HV5vD" id="6VrRWu7fZea" role="2ShVmc">
                            <ref role="HV5vE" node="6VrRWu7fofb" resolve="CalculatorImpl" />
                          </node>
                        </node>
                      </node>
                    </node>
                  </node>
                </node>
              </node>
            </node>
          </node>
        </node>
      </node>
      <node concept="3Tm1VV" id="6VrRWu7fQFe" role="1B3o_S" />
      <node concept="3cqZAl" id="6VrRWu7fRkw" role="3clF45" />
      <node concept="37vLTG" id="6VrRWu7fRY0" role="3clF46">
        <property role="TrG5h" value="args" />
        <node concept="10Q1$e" id="6VrRWu7fSep" role="1tU5fm">
          <node concept="17QB3L" id="6VrRWu7fRXZ" role="10Q1$1" />
        </node>
      </node>
    </node>
    <node concept="3Tm1VV" id="6VrRWu7fofc" role="1B3o_S" />
    <node concept="n94m4" id="6VrRWu7fofd" role="lGtFl">
      <ref role="n9lRv" to="xv7z:6VrRWu7ePH1" resolve="Calculator" />
    </node>
    <node concept="17Uvod" id="6VrRWu7fuJj" role="lGtFl">
      <property role="P4ACc" value="ceab5195-25ea-4f22-9b92-103b95ca8c0c/1169194658468/1169194664001" />
      <property role="2qtEX9" value="name" />
      <node concept="3zFVjK" id="6VrRWu7fuJk" role="3zH0cK">
        <node concept="3clFbS" id="6VrRWu7fuJl" role="2VODD2">
          <node concept="3clFbF" id="6VrRWu7fuS5" role="3cqZAp">
            <node concept="2OqwBi" id="6VrRWu7fv5W" role="3clFbG">
              <node concept="30H73N" id="6VrRWu7fuS4" role="2Oq$k0" />
              <node concept="3TrcHB" id="6VrRWu7fvmT" role="2OqNvi">
                <ref role="3TsBF5" to="tpck:h0TrG11" resolve="name" />
              </node>
            </node>
          </node>
        </node>
      </node>
    </node>
    <node concept="3uibUv" id="6VrRWu7fCN$" role="1zkMxy">
      <ref role="3uigEE" to="dxuu:~JFrame" resolve="JFrame" />
    </node>
  </node>
</model>

