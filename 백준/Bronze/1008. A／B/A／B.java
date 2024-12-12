import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        double value1 = scanner.nextInt();
        double value2 = scanner.nextInt();
        
        System.out.println(value1 / value2);

        scanner.close();
    }
}