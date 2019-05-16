package image;
/**
 * Exception UnknownPixel
 *
 * @author Leane Texier
 * @version 1.0
 */
public class UnknownPixelException extends RuntimeException {

	public UnknownPixelException() {
	}
	
	public UnknownPixelException(String msg) {
		super(msg);
	}
}
