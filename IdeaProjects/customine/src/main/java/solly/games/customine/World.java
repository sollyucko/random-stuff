package solly.games.customine;

import com.sun.j3d.utils.universe.SimpleUniverse;

import javax.media.j3d.BranchGroup;

import static solly.games.customine.Shapes.makeSphere;

public class World {
	public World() {
		// Create the universe
		SimpleUniverse universe = new SimpleUniverse();

		// Create a structure to contain objects
		BranchGroup group = new BranchGroup();

		group.addChild(makeSphere("/home/solly/Pictures/Screenshot_2017-10-14_21-29-04.png", 0.5f));

		// look towards the ball
		universe.getViewingPlatform().setNominalViewingTransform();

		// add the group of objects to the Universe
		universe.addBranchGraph(group);
	}

	public static void main(String[] args) {
		System.setProperty("sun.awt.noerasebackground", "true");
		new World();
	}
}
