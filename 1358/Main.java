package 1358;

import java.util.*;
import java.io.*;

public class Main {
    static int W,H,X,Y,P,R;
    static StringTokenizer st;
    static BufferedReader br;
    public static void main(String[] args) throws IOException{
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());
        Y = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken());
        R = H/2;
        int ans = 0;
        for (int i=0;i<P;i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            if (leftCheck(x, y) || rightCheck(x, y) || midCheck(x, y)) {
                ans += 1;
            }
        }
        System.out.println(ans);

    }
    static boolean leftCheck(int x,int y){
        return Math.pow(x - X, 2) + Math.pow(y - (Y + R), 2) <= R * R;
    }

    static boolean rightCheck(int x,int y){
        return Math.pow(x - W - X, 2) + Math.pow(y - (Y + R), 2) <= R * R;
    }

    static boolean midCheck(int x,int y){
        return X <= x && x <=X+W &&  Y<=y && y <= Y+H;
    }
}