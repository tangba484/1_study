import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main{
    public static void main(String[] args) throws IOException{
        int ans = Integer.MAX_VALUE;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<Integer> l = new ArrayList<>();
        for (String s : br.readLine().split(" ")) {
            l.add(Integer.parseInt(s));
        }
        Collections.sort(l);
        if (N%2 == 0) {
            System.out.println(l.get(N/2-1));
        }else{
            System.out.println(l.get(N/2));
        }
    }
}