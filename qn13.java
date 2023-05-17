/**
 * Author: Seah Yong Kheng
 * Leetcode question 13: Roman to Numeral
 * Check if the next letter is greater, if it is then subtract because IV is valid but not IM
 * 
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        
        int result = 0;
        int length = s.length();
        
        for (int i = 0; i < length; i++) {
            int currentVal = map.get(s.charAt(i));
            
            if (i < length - 1 && currentVal < map.get(s.charAt(i + 1))) {
                result -= currentVal;
            } else {
                result += currentVal;
            }
        }
        
        return result;
    }