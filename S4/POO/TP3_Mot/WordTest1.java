import org.junit.*;
import static org.junit.Assert.*;

public class WordTest1 {
    

    @Test
    public void testEquals(){
	Word word1 = new Word("hello");
	Word word2 = new Word("hello");
	Object obj = new Object();

	assertTrue(word1.equals(word2));
	assertFalse(word1.equals(obj));
    }

 


    // ---Pour permettre l'execution des test----------------------
    public static junit.framework.Test suite() {
	return new junit.framework.JUnit4TestAdapter(WordTest1.class);
    }

}

