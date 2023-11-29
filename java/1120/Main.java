import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int dif(String a,String b){
        int k = a.length();
        int res=0;
        for (int i =0;i<k;i++) {
            if (a.charAt(i) != b.charAt(i)) {
                res += 1;
            }
        }
        return res;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String a = st.nextToken();
        String b = st.nextToken();
        int la = a.length();
        int lb = b.length();
        int ans = 99;
        for (int i =0;i<=lb - la;i++) {
            ans = Math.min(dif(a,b.substring(i,i+la)),ans);
        }
        System.out.println(ans);
    }
}