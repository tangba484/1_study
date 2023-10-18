import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x1 = sc.nextInt();
        int y1 = sc.nextInt();
        int x2 = sc.nextInt();
        int y2 = sc.nextInt();
        int x3 = sc.nextInt();
        int y3 = sc.nextInt();
        sc.close();

        int[] p1 = {x1,y1};
        int[] p2 = {x2,y2};
        int[] p3 = {x3,y3};
        
        ArrayList<Double> result = new ArrayList<>();
        result.add(distance(p1,p2));
        result.add(distance(p2,p3));
        result.add(distance(p1,p3));
        Collections.sort(result);
        
        if((x2-x1)*(y3-y2)==(x3-x2)*(y2-y1)){
            System.out.println(-1.0);
            return;
         }else{
            System.out.println(R(result));
         }

        

    }

    static double distance(int[] point1,int[] point2){
        double x = point1[0];
        double y = point1[1];

        double a = point2[0];
        double b = point2[1];
        
        double res = Math.sqrt(Math.pow(x-a,2) + Math.pow(y-b,2));
        return res;
    }

    static double R(ArrayList<Double> result){
        double a = result.get(0);
        double b = result.get(1);
        double c = result.get(2);

        return 2*c - 2*a;

    }
}