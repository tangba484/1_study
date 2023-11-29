import java.io.*;
import java.util.*;

public class Main{

    static String reverse(String s){
        int k  = s.length();
        String[] S = s.split("");
        String res = "";
        for (int i =k-1 ; i >=0 ; i --){
            res += S[i];
        }
        return res;
    }
    public static void main (String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        ArrayList<String> list = new ArrayList<>();
        int n = s.length();
        for(int i =1; i <= n-2;i++){
            for(int j = i+1;j<=n-1;j++){
                String res = reverse(s.substring(0,i)) + reverse(s.substring(i,j)) + reverse(s.substring(j,n));
                list.add(res);
            }
        }
        Collections.sort(list);
        System.out.println(list.get(0));
    }
}