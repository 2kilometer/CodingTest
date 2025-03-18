import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String str = "odd";
        if (n % 2 == 0){
            str = "even";
        }
        
        System.out.print(String.format("%d is %s", n, str));
    }
}