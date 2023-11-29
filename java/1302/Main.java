import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.*;

public class Main {
    static Integer MAX_NUM = 1;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        HashMap<String, Integer> map = new HashMap<>();
        ArrayList<String> ans = new ArrayList<>();

        for (int i =0;i<n;i++) {
            String s = br.readLine();
            if (!map.containsKey(s)) {
                map.put(s, 1);
            } else {
                Integer val = map.get(s);
                map.put(s,val+1);
                if (val+1 > MAX_NUM) {
                    MAX_NUM = val + 1;
                }
            }
        }
        for (Map.Entry<String,Integer> entry : map.entrySet()) {
            if (entry.getValue() == MAX_NUM) {
                ans.add(entry.getKey());
            }
        }
        Collections.sort(ans);
        System.out.println(ans.get(0));
    }
}
