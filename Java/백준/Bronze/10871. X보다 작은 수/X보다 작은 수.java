import java.util.*;
import java.io.*;

public class Main {
	public static void main (String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt(), x = sc.nextInt();
        String answer = "";
        
        for (int i = 0; i < n; i++){
            int input = sc.nextInt();
            if (input < x) answer += (input + " ");
        }
        
        System.out.println(answer.trim());
	}
}