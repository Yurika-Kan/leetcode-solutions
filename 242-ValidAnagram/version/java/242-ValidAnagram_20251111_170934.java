// Last updated: 11/11/2025, 5:09:34 PM
class Solution {
    public boolean isAnagram(String s, String t) {
        // sanity check 
        if (s.length() != t.length())
        return false;
        //map 
        Map<Character, Integer> sreakMap = new HashMap<>();
        Map<Character, Integer> treakMap = new HashMap<>();

        for (char charac: s.toCharArray()) {
            sreakMap.put(charac, sreakMap.getOrDefault(charac, 0) + 1);
        }

        for (char charac: t.toCharArray()) {
            treakMap.put(charac, treakMap.getOrDefault(charac, 0) + 1);
        }

        return sreakMap.equals(treakMap);
        //compare
    }
}
                                                                                           