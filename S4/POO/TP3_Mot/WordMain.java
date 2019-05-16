public class WordMain{
 public static void main(String[] args){
   Word word;
   char c;
   Word m;
   word = new Word(args[0]);
   c = args[1].charAt(0);
   m = new Word(args[2]);
   System.out.println("Number of characters: "+word.nbOfChars());
   System.out.println("String corresponding to the word: "+word.toString());
   System.out.println("Number of characters "+c+" in the word: "+word.nbOccurrencesOfChar(c));
   System.out.println("Reverse of the word: "+word.reverse());
   System.out.println("Contains the word "+m.toString()+" in the word: "+word.contains(m));
   System.out.println("Word "+m.toString()+" rhymes with the word: "+word.rhymesWith(m));
   System.out.println("Extract before "+c+": "+word.extractBefore(c));
   System.out.println("Word is a palindrom: "+word.isPalindrome());
   System.out.println("Word "+m.toString()+" is anagram of the word: "+word.isAnagram(m));
   System.out.println("Word is a proper noun: "+word.isProperNoun());
 }
}
