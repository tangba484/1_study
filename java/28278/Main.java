import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        Stack<Integer> s = new Stack<>();
        for (int i=0;i<n;i++) {
            st = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            if (a.equals("1")) {
                s.push(Integer.valueOf(st.nextToken()));
            } else if (a.equals("2")) {
                if (s.isEmpty()) {
                    sb.append("-1").append("\n");
                } else {
                    sb.append(s.pop()).append("\n");
                }
            } else if (a.equals("3")) {
                sb.append(s.size()).append("\n");
            } else if (a.equals("4")) {
                if (s.isEmpty()) {
                    sb.append("1").append("\n");
                } else {
                    sb.append("0").append("\n");
                }
            } else {
                if (!s.isEmpty()) {
                    sb.append(s.peek()).append("\n");
                } else {
                    sb.append(-1).append("\n");
                }
            }
        }
        
        System.out.println(sb);
    }
}
