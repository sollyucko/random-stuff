package misc.math.geometry.d1;

import misc.math.geometry.d0.Shape.*;

public	abstract	class	Shape {
	abstract	Point	reflect(	Point		point);
	abstract	Point	translate(	Direction	direction);
	abstract	Point	dilate(		Point		point,	float	factor);
}
