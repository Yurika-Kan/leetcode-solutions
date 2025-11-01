// Last updated: 11/1/2025, 4:59:15 PM
class Solution {
    public int countCharacters(String[] words, String chars) {
        // U: validate if word in words can be made from string chars then sum lengths of validated words
        // M: for loop, len(word), letter in string
        // P: 
        // for each word in words, 
        //  for each letter in word, 
        //     if letter not in chars, move on to next word
        //  end of word & no letters not in chars, add to sum 

        // dictionary/ hashmap 
        // map for each word
        // map for chars 
        // check if each key, value is either key, value or key, value < chars key, value

        // create freq map for chars
        Map<Character, Integer> charFreq = new HashMap<>();

        for (char c: chars.toCharArray()) {
            charFreq.put(c, charFreq.getOrDefault(c, 0) + 1);
        }

        //counter for sum
        int totalLen = 0;

        // for each word in words
        for (String word: words) {
            Map<Character, Integer> wordFreq = new HashMap<>(); 
            for (char c: word.toCharArray()) {
                wordFreq.put(c, wordFreq.getOrDefault(c, 0) +1);
            }
            // check if word can be formed by chars
            boolean valid = true;
            for (char c: word.toCharArray()) {
                if (wordFreq.get(c) > charFreq.getOrDefault(c, 0)) {
                    valid = false; 
                    break;
                }
            }
            
            if (valid) {
            totalLen += word.length();
              }
        }
        

        return totalLen;
    }
}