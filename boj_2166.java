import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj_2166 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[] X = new long[n+1];
        long[] Y = new long[n+1];
        for (int i=0;i<n;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long x = Integer.parseInt(st.nextToken());
            long y = Integer.parseInt(st.nextToken());
            X[i] = x;
            Y[i] = y;
        }
        X[n] = X[0];
        Y[n] = Y[0];
        long Sx = 0,Sy=0;
        for (int i=0;i<n;i++) {
            Sx += X[i]*Y[i+1];
            Sy += Y[i]*X[i+1];
        }
        System.out.println(String.format("%.1f",Math.abs(Sx-Sy)/2.0));
    }
}