
import java.util.*;

public class Alpha_beta {
    static int b;

    static double alphaBeta(List<Double> values, boolean isMax,double alpha,double beta) {
        if (values.size() == 1)  return values.get(0);
        int size = values.size() / b;
        if (isMax) {
            double value = -1000;
            for (int i = 0; i < b; i++) {
                List<Double> child = new ArrayList<>(values.subList(i * size, (i + 1) * size));
                value = Math.max(value, alphaBeta(child, false, alpha, beta));
                alpha = Math.max(alpha, value);
                if (alpha >= beta) {
                    System.out.println("Pruned remaining children of MAX node "+ values);
                    break;
                }
            }
            return value;
        } else {
            double value = 1000;
            for (int i = 0; i < b; i++) {
                List<Double> child = new ArrayList<>(values.subList(i * size, (i + 1) * size));
                value = Math.min(value, alphaBeta(child, true, alpha, beta));
                beta = Math.min(beta, value);
                if (alpha >= beta) {
                    System.out.println("Pruned remaining children of MIN node " + values);
                    break;
                }
            }
            return value;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Leaf values: ");
        String[] input = sc.nextLine().trim().split("\\s+");

        List<Double> leaves = new ArrayList<>();
        for (String value : input) {
            leaves.add(Double.parseDouble(value));
        }

        System.out.print("Children per node: ");
        b = Integer.parseInt(sc.nextLine());

        System.out.print("Who plays at the root (max/min): ");
        boolean isMax = sc.nextLine().equals("max");

        double best = alphaBeta(leaves, isMax, -1000, 1000);
        System.out.println("Value of root = " + best);

        sc.close();
    }
}