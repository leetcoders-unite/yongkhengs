
/**
 * Author: Seah Yong Kheng
 * Leetcode question 412: FizzBuzz
 * 
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> stringList = new ArrayList<>();
        for (int num = 1; num < n + 1; num++) {
            if (num % 3 == 0&& num % 5 == 0) {
                stringList.add("FizzBuzz");
            }
            else if (num % 3 == 0) {
                stringList.add("Fizz");
            }
            else if (num % 5 == 0) {
                stringList.add("Buzz");
            } 
            else {
                stringList.add(String.valueOf(num));
            }
        }
        return stringList;
        
    }
}
