class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        if (ineq.equals(">")){
            int temp = n;
            n = m;
            m = temp;
        }
        
        if (eq.equals("!")){
            return (n < m ? 1 : 0);
        } 
        return (n <= m ? 1 : 0);
    }
}