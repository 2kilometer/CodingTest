import java.util.Arrays;
class Solution {
    public int solution(int[] array) {
        Arrays.sort(array);
        int mod = (array.length / 2);
        return array[mod];
    }
}