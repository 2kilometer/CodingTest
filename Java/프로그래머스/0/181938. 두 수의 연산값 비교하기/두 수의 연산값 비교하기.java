class Solution {
    public int solution(int a, int b) {
        int ab = Integer.parseInt("" + a + b);
        return Math.max(ab, 2 * a * b);
    }
}