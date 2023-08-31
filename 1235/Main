import java.io.*;
import java.util.*;

public class Main {

    static String Cut(String s,int m){
        int ls = s.length();
        return s.substring(ls-m,ls);
    }

    public static void main (String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<String> l = new ArrayList<>();
        for (int i =0 ; i<n;i++) {
            l.add(br.readLine());
        }
        int k = l.get(0).length();
        for (int i =0 ; i < k ; i ++){
            HashSet<String> set = new HashSet<>();
            for (int j=0 ; j < n ; j++){
               set.add(Cut(l.get(j),i+1));
            }
            if (set.size() == n){
                System.out.println(i+1);
                break;
            }
        }
    }
}
