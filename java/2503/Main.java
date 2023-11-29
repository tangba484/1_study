import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
    private static int flag;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        ArrayList<Info> L = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String s = sc.nextLine();
            String[] split = s.split(" ");
            L.add(new Info(split[0], Integer.parseInt(split[1]), Integer.parseInt(split[2])));
        }

        int ans = 0;
        for (int i = 123; i <= 999; i++) {
            flag = 1;
            if (!(isThree(i))) {
                continue;
            }
            for (Info info : L) {
                String a = info.getA();
                Integer strikeCnt = info.getStrikeCnt();
                Integer ballCnt = info.getBallCnt();
                int calculateStrike = calculateStrike(a, String.valueOf(i));
                int calculateBall = calculateBall(a, String.valueOf(i));
                if (!(strikeCnt == calculateStrike && ballCnt == calculateBall)) {
                    flag = 0;
                    break;
                }
            }
            if (flag == 1) {
                ans += 1;
            }
        }
        System.out.println(ans);
    }

    private static boolean isThree(int i) {
        HashSet<Character> set = new HashSet<>();
        String s = String.valueOf(i);
        for (int j = 0; j < 3; j++) {
            char c = s.charAt(j);
            if (c == '0') return false;
            set.add(c);
        }
        return set.size() == 3;
    }

    static int calculateStrike(String a, String b) {
        int cnt = (int) IntStream.range(0, 3).filter(i -> a.charAt(i) == b.charAt(i)).count();
        return cnt;
    }

    static int calculateBall(String a, String b) {
        int cnt = 0;
        for (int i = 0; i < 3; i++) {
            char ac = a.charAt(i);
            char bc = b.charAt(i);
            if ((ac != bc) && b.contains(String.valueOf(ac))) {
                cnt += 1;
            }
        }
        return cnt;
    }
}


class Info {
    String a;
    Integer strikeCnt;
    Integer ballCnt;

    public Info(String a, Integer strikeCnt, Integer ballCnt) {
        this.a = a;
        this.strikeCnt = strikeCnt;
        this.ballCnt = ballCnt;
    }

    public String getA() {
        return a;
    }

    public Integer getStrikeCnt() {
        return strikeCnt;
    }

    public Integer getBallCnt() {
        return ballCnt;
    }
}