import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        StringBuilder sb = new StringBuilder();
        
        for(char x : a.toCharArray()){
            if(Character.isLowerCase(x)){
                sb.append(Character.toUpperCase(x));
            }else{
                sb.append(Character.toLowerCase(x));
            }
        }
        
        System.out.print(sb);
    }
}