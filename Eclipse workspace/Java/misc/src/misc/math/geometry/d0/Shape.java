package misc.math.geometry.d0;

import misc.math.geometry.*;

public	abstract	class	Shape {
	public			class	Point {
		public	Label	label;
		
		public	Point(	Label	label) {
			this.label = label;
		}
	}
	
	abstract	Point	reflect(	Point	point);
}
