import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int time = sc.nextInt() * 60 + sc.nextInt() + sc.nextInt();
        
        System.out.println((time / 60 % 24) + " " + (time % 60));
        
        sc.close();
    }
}