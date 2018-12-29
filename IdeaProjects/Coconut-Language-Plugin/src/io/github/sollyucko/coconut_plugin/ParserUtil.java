package io.github.sollyucko.coconut_plugin;

import com.intellij.lang.PsiBuilder;
import com.intellij.lang.parser.GeneratedParserUtilBase;
import com.intellij.psi.tree.IElementType;
import lombok.Data;

import java.util.Stack;

public class ParserUtil extends GeneratedParserUtilBase {
	private static boolean parseDeeperOperator(PsiBuilder builder, int level, int i, Parser nextLevel,
	                                           IElementType elementType, OperatorPrecedenceGroup... operators) {
		if (operators.length > i + 1) {
			return parseOperator(builder, level + 1, i + 1, nextLevel, elementType, operators);
		} else {
			return nextLevel.parse(builder, level);
		}
	}
	
	private static boolean parseOperator(PsiBuilder builder, int level, int i, Parser nextLevel,
	                                     IElementType elementType, OperatorPrecedenceGroup... operators) {
		if (!recursion_guard_(builder, level, "Operator " + i)) { return false; }
		
		PsiBuilder.Marker marker;
		boolean result;
		
		switch (operators[i].getAssociativity()) {
			case LEFT:
				marker = enter_section_(builder, level, _LEFT_, elementType, "<level " + i + " operator>");
				
				result = parseDeeperOperator(builder, level, i, nextLevel, elementType, operators);
				
				if (!result) {
					return false;
				}
				
				while (result) {
					result = false;
					
					String[] operatorTextsCurrentLevel = operators[i].getOperators();
					for (int j = 0; !result && j < operatorTextsCurrentLevel.length; j++) {
						result = consumeToken(builder, operatorTextsCurrentLevel[j]);
					}
					
					result = result && parseDeeperOperator(builder, level, i, nextLevel, elementType, operators);
					
					if (result) {
						PsiBuilder.Marker newMarker = marker.precede();
						exit_section_(builder, level, marker, result, false, null);
						marker = newMarker;
					}
				}
				
				return true;
			
			case RIGHT:
				Stack<PsiBuilder.Marker> markerStack = new Stack<>();
				markerStack.push(enter_section_(builder, level, _NONE_, elementType, "<level " + i + " operator>"));
				result = parseDeeperOperator(builder, level, i, nextLevel, elementType, operators);
				
				while(result) {
				
				}
			
		}
		
		return false;
	}
	
	public static boolean parseOperator(PsiBuilder builder, int level, Parser nextLevel, IElementType elementType,
	                                    OperatorPrecedenceGroup... operators) {
		return parseOperator(builder, level, 0, nextLevel, elementType, operators);
	}
	
	public enum Associativity {
		LEFT, RIGHT;
	}
	
	@Data
	public static class OperatorPrecedenceGroup {
		private final int arity;
		private final Associativity associativity;
		private final String[] operators;
	}
}
