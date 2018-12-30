

package com.solly.maze;


import java.util.Set;


public class Node {
	
	public Set<Node> neighbors;
	
	public boolean isGoal;
	
	public Node(Set<Node> neighbors) {
		this.neighbors = neighbors;
		this.isGoal = false;
	}
	
	public Node(Set<Node> neighbors, boolean isGoal) {
		this.neighbors = neighbors;
		this.isGoal = isGoal;
	}
	
}
