import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        int now = m;
        if (M - m < T) {
            System.out.println(-1);
        } else {
            int cnt = 0;
            int minute=0;
            while (true) {
                minute += 1;
                if (now + T > M) {
                    now = now - R;
                    if (now < m) {
                        now = m;
                    }
                } else if (now + T <= M) {
                    cnt += 1;
                    now = now + T;
                }
                if (cnt == N) {
                    System.out.println(minute);
                    break;
                }
            }
        }
    }
}
