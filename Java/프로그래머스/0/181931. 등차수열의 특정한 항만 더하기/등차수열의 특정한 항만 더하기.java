class Solution {
    public int solution(int a, int d, boolean[] included) {
        int sum = 0;
        for (int i = 0; i < included.length; i++){
            if (included[i])
                sum += a + d * i;
        }
        return sum;
    }
}