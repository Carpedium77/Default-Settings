
import java.util.*;

public class Min_max {
    static int b;
    static double minimax(List<Double> values, boolean isMax) {
        if (values.size() == 1) return values.get(0);
        int size = values.size() / b;
        List<Double> results = new ArrayList<>();
        for (int i = 0; i < b; i++) {
            List<Double> child = new ArrayList<>(values.subList(i * size, (i + 1) * size));
            results.add(minimax(child, !isMax));
        }
        if (isMax) return Collections.max(results);
        return Collections.min(results);
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

        double best = minimax(leaves, isMax);
        System.out.println("Value of root = " + best);

        sc.close();
    }
}