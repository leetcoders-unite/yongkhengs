/**
 * Author: Seah Yong Kheng
 * Leetcode question 58: Length of last word
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
class Solution {
    public int lengthOfLastWord(String s) {

        int charCounter = 0;
        boolean shouldBreak = false; // Flag to determine space is after word

        for (int i = s.length() - 1; i > -1; i --) {
            if (s.charAt(i) != ' ') {
                shouldBreak = true;
                charCounter ++;
            } else {
                if (shouldBreak) {
                    return charCounter;
                }
            }
        }
        return charCounter;
        
    }
}