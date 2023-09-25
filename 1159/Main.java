import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        HashMap<Character,Integer> d = new HashMap<>();
        for (int i=0; i < n ; i ++){
            String s = br.readLine();
            char t = s.charAt(0);
            if (d.containsKey(t)){
                d.put(t,d.get(t)+1);
            } else{
                d.put(t,1);
            }
        }
        List<Character> ans = new ArrayList<>();
        for (char a : d.keySet()) {
            if(d.get(a) >= 5){
                ans.add(a);
            }
        }
        
        if (ans.size()>0){
            Collections.sort(ans);
            StringBuilder result = new StringBuilder();
            for(char a : ans){
                result.append(a);
            }
            System.out.println(result);
        }else{
            System.out.println("PREDAJA");
        }
     }
    
}
