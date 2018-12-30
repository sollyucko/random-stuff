package com.solly.maze;

import java.util.HashSet;
import java.util.Set;

public class RootedMaze extends Maze {
	
	public RootedMaze(Node node) {
		super(getNodes(node));
	}

	public static Set<Node> getNodes(Node node) {
		Set<Node> nodes = new HashSet<>();
		Set<Node> newNodes = new HashSet<>();
		Set<Node> newNewNodes;
		newNodes.add(node);
		
		while (newNodes.size() > 0) {
			newNewNodes = new HashSet<>();
			
			for(Node newNode : newNodes) {
				for(Node neighbor : newNode.neighbors) {
					if(!nodes.contains(neighbor)) {
						newNewNodes.add(neighbor);
					}
				}
			}
			
			newNodes = newNewNodes;
		}
		
		return nodes;
	}
	
}
