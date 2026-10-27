import java.util.*;

public class Astar {
    static Map<String, Map<String, Double>> graph = new HashMap<>();
    static Map<String, Double> h = new HashMap<>();
    static class Node {
        String name;
        double g, f;
        List<String> path;

        Node(String name, double g, double f, List<String> path) {
            this.name = name;
            this.g = g;
            this.f = f;
            this.path = path;
        }
    }

    static List<String> aStar(String start, String goal) {
        PriorityQueue<Node> open = new PriorityQueue<>((a, b) -> Double.compare(a.f, b.f));
        open.add(new Node(start, 0, h.get(start), new ArrayList<>(Arrays.asList(start))));
        Set<String> visited = new HashSet<>();

        while (!open.isEmpty()) {
            Node current = open.poll();
            if (current.name.equals(goal)) {
                System.out.println("Total cost = " + current.g);
                return current.path;
            }
            if (visited.contains(current.name)) continue;
            visited.add(current.name);
            for (Map.Entry<String, Double> entry : graph.get(current.name).entrySet()) {
                String child = entry.getKey();
                double cost = entry.getValue();
                double newG = current.g + cost;
                double newF = newG + h.get(child);
                List<String> newPath = new ArrayList<>(current.path);
                newPath.add(child);
                open.add(new Node(child, newG, newF, newPath));
            }
        }
        System.out.println("Total cost = 0");
        return null;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Number of nodes: ");
        int n = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < n; i++) {
            System.out.print("Node, h value, then child cost pairs: ");
            String[] line = sc.nextLine().trim().split("\\s+");

            String node = line[0];
            h.put(node, Double.parseDouble(line[1]));
            Map<String, Double> children = new HashMap<>();
            for (int j = 2; j < line.length; j += 2) {
                children.put(line[j],Double.parseDouble(line[j + 1]));
            }
            graph.put(node, children);
        }

        System.out.print("Start node: ");
        String start = sc.nextLine();

        System.out.print("Goal node: ");
        String goal = sc.nextLine();

        List<String> path = aStar(start, goal);
        System.out.println("Path = " + path);

        sc.close();
    }
}

