import java.util.*;

public class Main {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int cost = sc.nextInt();
        int n = sc.nextInt();
        int check = 0;
        sc.nextLine();
        
        for (int i = 0; i < n; i++){
            String[] input = sc.nextLine().split(" ");
            int price = Integer.parseInt(input[0]);
            int num = Integer.parseInt(input[1]);
            check += price * num;
        }
        if (cost == check) System.out.print("Yes"); else System.out.print("No");
    }
}