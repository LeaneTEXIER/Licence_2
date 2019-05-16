import org.junit.*;
import static org.junit.Assert.*;

public class WordTest {

    @Test
    public void testEquals(){
	Word word1 = new Word("hello");
	Word word2 = new Word("hello");
	Word word3 = new Word("another");
	Object obj = new Object();

	assertTrue(word1.equals(word2));
	assertFalse(word1.equals(word3));
	assertFalse(word1.equals(obj));
    }

    @Test
    public void testNbOfChars() {
	Word word1 = new Word("bonjour");
	Word word2 = new Word("timoleon");
	assertEquals(7, word1.nbOfChars());
	assertEquals(8, word2.nbOfChars());
    }

    @Test
    public void testNbOccurrencesOfChar() {
	Word word1 = new Word("abracadabra");
	assertEquals(5, word1.nbOccurrencesOfChar('a'));
	assertEquals(0, word1.nbOccurrencesOfChar('z'));
    }

    @Test
    public void testReverse() {
	Word word1 = new Word("abcde");
	Word word2 = new Word("edcba");
	assertEquals(word2, word1.reverse());
    }

    @Test
    public void testContains() {
	Word word1 = new Word("timoleon");
	Word word2 = new Word("tim");
	Word word3 = new Word("mole");
	Word word4 = new Word("leon");
	Word word5 = new Word("truc");
	Word word6 = new Word("molee");

	assertTrue(word1.contains(word2));
	assertTrue(word1.contains(word3));
	assertTrue(word1.contains(word4));
	assertFalse(word1.contains(word5));
	assertFalse(word1.contains(word6));
    }

    @Test
    public void testRhymesWith() {
	Word word1 = new Word("timoleon");
	Word word2 = new Word("tim");
	Word word3 = new Word("neon");
	Word word4 = new Word("on");

	assertTrue(word1.rhymesWith(word3));
	assertFalse(word1.rhymesWith(word2));
	assertFalse(word1.rhymesWith(word4));
    }

    @Test
    public void testExtractBeforeWhenCharInWord() {
	Word word1 = new Word("timoleon");

	Word[] extract1 = word1.extractBefore('o');
	Word[] extract2 = word1.extractBefore('t');
	Word[] extract3 = word1.extractBefore('n');

	assertEquals(new Word("timo"), extract1[0]);
	assertEquals(new Word("leon"), extract1[1]);

	assertEquals(new Word("t"), extract2[0]);
	assertEquals(new Word("imoleon"), extract2[1]);

	assertEquals(new Word("timoleon"), extract3[0]);
	assertEquals(new Word(""), extract3[1]);
    }

    @Test
    public void testExtractBeforeWhenCharNotInWord() {
	Word word1 = new Word("timoleon");

	Word[] extract4 = word1.extractBefore('z');

	assertEquals(new Word(""), extract4[0]);
	assertEquals(new Word("timoleon"), extract4[1]);
    }


    @Test
    public void testIsPalindrome() {
	Word word1 = new Word("radar");
	Word word2 = new Word("raddar");
	Word word3 = new Word("probleme");

	assertTrue(word1.isPalindrome());
	assertTrue(word2.isPalindrome());
	assertFalse(word3.isPalindrome());
    }

    @Test
    public void testIsAnagram() {
	Word word1 = new Word("timoleon");
	Word word2 = new Word("letomion");
	Word word3 = new Word("letmion");
	Word word4 = new Word("letmionoo");
	Word word5 = new Word("lettmion");
  Word word6 = new Word("timoleont");


	assertTrue(word1.isAnagram(word2));
	assertFalse(word1.isAnagram(word3));
	assertFalse(word1.isAnagram(word4));
	assertFalse(word1.isAnagram(word5));
	assertFalse(word1.isAnagram(word6));
	assertFalse(word6.isAnagram(word1));

    }

    @Test
    public void testIsProperNoun() {
	Word word1 = new Word("Timoleon");
	Word word2 = new Word("timoleon");

	assertTrue(word1.isProperNoun());
	assertFalse(word2.isProperNoun());
    }

    // ---Pour permettre l'exécution des test----------------------
    public static junit.framework.Test suite() {
	return new junit.framework.JUnit4TestAdapter(WordTest.class);
    }

    public static void main(String[] args) {
	org.junit.runner.JUnitCore.main("WordTest");
    }
}
