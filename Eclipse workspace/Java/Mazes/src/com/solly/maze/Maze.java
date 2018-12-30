package com.solly.maze;

import java.util.Set;
import java.util.stream.Collectors;

public class Maze {
	
	Set<Node> nodes;
	
	public Maze(Set<Node> nodes) {
		this.nodes = nodes;
	}
	
	public Maze simplify() {		
		return new Maze(this.nodes.stream().filter(node -> node.neighbors.size() > 1).collect(Collectors.toSet()));
	}
	
}
