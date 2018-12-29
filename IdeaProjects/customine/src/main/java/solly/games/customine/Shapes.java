package solly.games.customine;

import com.sun.j3d.utils.geometry.Sphere;
import com.sun.j3d.utils.image.TextureLoader;
import org.jetbrains.annotations.NotNull;

import javax.media.j3d.Appearance;
import java.awt.*;

import static com.sun.j3d.utils.geometry.Primitive.GENERATE_TEXTURE_COORDS;

public class Shapes {
	@NotNull static Sphere makeSphere(String texturePath, float radius) {
		Appearance ap = new Appearance();
		ap.setTexture((new TextureLoader(texturePath, "RGBA", new Container())).getTexture());
		return new Sphere(radius, GENERATE_TEXTURE_COORDS, ap);
	}
}
