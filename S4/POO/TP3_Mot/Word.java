/**
 * Word class : a class to represent word with several usefull functions
 *
 * @author : Léane Texier
 */

public class Word {

    // ATTRIBUTS
    /* contains the string that represents the characters of this word */
    private String value;

    // CONSTRUCTEURS
    /** builds Word defined by its characters
     * @param s the string that contains the characters for this Word object
     */
    public Word(String s) {
	     this.value = s;
    }

    // METHODES
    /**
     * returns <code>true</code> if <code>o</code> is equals to this word object, ie if
     * <code>o</code> is a Word and its value is the same as this word's value
     *
     * @param o the object to be compared with this Word
     * @return <code>true</code> iff <code>o</code> is a Word with the same value as this word.
     */
    public boolean equals(Object o) {
	     if (o instanceof Word) {
	        Word theOther = (Word) o;
	        return this.value.equals(theOther.value);
	     }
       else {
	        return false;
	     }
    }

    /**
     * returns the number of characters (the length) of the word
     *
     * @return the number of characters of the word
     */
    public int nbOfChars() {
	     return this.value.length();
    }

    /**
     * returns the string corresponding to the word
     *
     * @return the string corresponding to the word
     */
    public String toString() {
	     return this.value;
    }

    /**
     * returns the number of occurrences of the character c (param) in the word
     *
     * @param c the character to find his number of occurences
     * @return the number of occurrences of the param c in the word
     */
    public int nbOccurrencesOfChar(char c) {
      int nbOcc;
      int i;
      nbOcc=0;
      i=this.value.indexOf(c);
      while (i!=-1){
        nbOcc++;
        i=this.value.indexOf(c,i+1);
      }
	    return nbOcc;
    }

    /**
     * returns a word which value is the inverse of the initial word value
     *
     * @return a word which value is the inverse of the initial word value
     */
    public Word reverse() {
      int i;
      int j;
      String str_rev;
      i=nbOfChars();
      str_rev="";
      for (j=i-1;j>=0; j--){
        str_rev+=this.value.charAt(j);
      }
      return new Word (str_rev);
    }

    /**
     * returns <code>true</code> if the word is a palindrome, otherwise <code>false</code>
     *
     * @return <code>true</code> iff the word is a palindrome
     */
    public boolean isPalindrome() {
      return (this.reverse().equals(this));
    }

    /**
     * returns <code>true</code> if the parameter word m is a sub-word of the
     * initial word, otherwise <code>false</code>
     *
     * @param m the word to look if it is contain
     * @return <code>true</code> iff the initial word contains m
     */
    public boolean contains(Word m) {
      char beg;
      int i;
      int size;
      String j;
      beg=m.value.charAt(0);
      i=this.value.indexOf(beg);
      size=m.nbOfChars();
      while (i!=-1 && this.value.substring(i).length()>=size){
        j= this.value.substring(i, i+size);
        if (j.equals(m.value)){
          return true;
        }
        i=this.value.indexOf(beg,i+1);
      }
	    return false;
    }

    /**
     * returns <code>true</code> if the initial word and the parameter word m
     * have the same 3 last characters, otherwise <code>false</code>
     *
     * @param m a word to check if it rhymes with the initial word
     * @return <code>true</code> iff the initial word and m have the same 3 last characters
     */
    public boolean rhymesWith(Word m) {
      int size_m;
      int size_th;
      int j;
      boolean verif;
      size_m = m.nbOfChars();
      size_th = this.nbOfChars();
      j=1;
      verif=true;
      if (size_m<3 || size_th<3){
        return !verif;
      }
      else{
        while (verif && j<4){
          if (this.value.charAt(size_th-j)!=m.value.charAt(size_m-j)){
            verif=false;
          }
          j++;
        }
        return verif;
      }
    }

    /**
     * returns <code>true</code> if the initial word is a proper name,
     * otherwise <code>false</code>
     *
     * @return <code>true</code> iff the word is a proper name
     */
    public boolean isProperNoun() {
	    return Character.isUpperCase(this.value.charAt(0));
    }

    /**
     * returns <code>true</code> if the parameter word m is an anagram of the initial word,
     * otherwise <code>false</code>
     *
     * @param m the word to check if it is an anagram
     * @return <code>true</code> iff the parameter word m is an anagram of the initial word
     */
    public boolean isAnagram(Word m) {
      String mot_m;
      String mot_init;
      int i;
      mot_m = m.toString();
      mot_init = this.toString();
      i=0;
      while (mot_m.length()==mot_init.length() && mot_m.length()!=0){
        i=mot_init.indexOf(mot_m.charAt(0));
        if (i!=-1){
          mot_init=mot_init.substring(0,i)+mot_init.substring(i+1);
        }
        mot_m=mot_m.substring(1);
      }
      if (mot_init.length()!=0){
        return false;
      }
      else{
        return true;
      }
    }

    /**
     * returns a table with 2 words
     * if the character c is in the word, the first is the initial word until the first character c
     * and the second is the end of the word
     * otherwise, the first is an empty word and the second is the initial word
     *
     * @param c the character use to separate the word
     * @return a table with 2 words (first: initial word until c (empty if c not in the word), second: the end of the initial word)
     */
    public Word[] extractBefore(char c) {
      Word[] tab;
      int i;
      tab=new Word[2];
      i=this.value.indexOf(c);
      tab[0]=new Word(this.value.substring(0,i+1));
      tab[1]=new Word(this.value.substring(i+1));
      return tab;
    }

}
