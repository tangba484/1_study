import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int round = 1;
        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) break;
            List<String> name = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                name.add(br.readLine());
            }
            Map<Integer, Integer> countMap = new HashMap<>();
            for (int i = 0; i < 2 * n - 1; i++) {
                int a = Integer.parseInt(br.readLine().split(" ")[0]);
                countMap.put(a, countMap.getOrDefault(a, 0) + 1);
            }
            for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
                if (entry.getValue().equals(1)) {
                    System.out.println(round + " " + name.get(entry.getKey() - 1));
                }
            }
            round++;
        }
    }
}
