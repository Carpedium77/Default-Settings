
import java.util.*;

public class DFID {
    static HashMap<String, List<String>> graph = new HashMap<>();

    public static boolean dls(String node, String goal, int limit, List<String> path) {
        path.add(node);
        if (node.equals(goal)) return true;
        if (limit == 0) {
            path.remove(path.size() - 1);
            return false;
        }
        for (String child : graph.get(node)) if (dls(child, goal, limit - 1, path)) return true;
        path.remove(path.size() - 1);
        return false;
    }

    public static List<String> dfid(String start, String goal,int maxDepth) {
        for (int limit = 0; limit <= maxDepth; limit++) {
            List<String> path = new ArrayList<>();
            System.out.println("Trying limit " + limit);
            if (dls(start, goal, limit, path)) return path;
        }
        return null;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Number of nodes: ");
        int n = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < n; i++) {
            System.out.print("Node and its children: ");
            String[] line = sc.nextLine().trim().split("\\s+");
            List<String> children = new ArrayList<>();
            for (int j = 1; j < line.length; j++) children.add(line[j]);
            graph.put(line[0], children);
        }

        System.out.print("Start node: ");
        String start = sc.nextLine();

        System.out.print("Goal node: ");
        String goal = sc.nextLine();

        System.out.print("Maximum depth: ");
        int maxDepth = Integer.parseInt(sc.nextLine());

        List<String> result = dfid(start, goal, maxDepth);

        if (result != null) {
            System.out.println("Goal found, path = " + result);
        } else {
            System.out.println("Goal not found");
        }

        sc.close();
    }
}
