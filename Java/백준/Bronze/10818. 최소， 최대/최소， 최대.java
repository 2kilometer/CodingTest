import java.util.*;
import java.util.stream.*;

public class Main {
	public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); sc.nextLine();
        IntSummaryStatistics result = Arrays.stream(sc.nextLine().split(" "))
                                .mapToInt(Integer::parseInt)
                                .summaryStatistics(); 
	 
	    System.out.print(result.getMin() + " " + result.getMax());
	    sc.close();
	}
}