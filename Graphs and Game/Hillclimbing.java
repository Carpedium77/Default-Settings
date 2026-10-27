
import java.util.*;

public class Hillclimbing {
    static Map<String, List<String>> graph = new HashMap<>();
    static Map<String, Double> h = new HashMap<>();
    static List<String> hillClimbing(String start, String goal) {
        String current = start;
        List<String> path = new ArrayList<>();
        path.add(current);
        while (!current.equals(goal)) {
            String best = current;
            for (String child : graph.get(current)) {
                if (h.get(child) < h.get(best)) {
                    best = child;
                }
            }
            if (best.equals(current)) {
                System.out.println("Stuck at " + current + " (local minimum)");
                return path;
            }
            current = best;
            path.add(current);
        }
        return path;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Number of nodes: ");
        int n = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < n; i++) {
            System.out.print("Node, h value and its children: ");
            String[] line = sc.nextLine().trim().split("\\s+");

            String node = line[0];
            h.put(node, Double.parseDouble(line[1]));
            List<String> children = new ArrayList<>();
            for (int j = 2; j < line.length; j++) {
                children.add(line[j]);
            }
            graph.put(node, children);
        }

        System.out.print("Start node: ");
        String start = sc.nextLine();

        System.out.print("Goal node: ");
        String goal = sc.nextLine();

        List<String> path = hillClimbing(start, goal);
        System.out.println("Path = " + path);

        sc.close();
    }
}