import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static List<Gear> gearList;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 4; i++) {
            sb.append(sc.nextLine() + "\n");
        }
        gearList = getGearList(sb);
        int k = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < k; i++) {
            String[] split = sc.nextLine().split(" ");
            int idx = Integer.parseInt(split[0]) - 1;
            int dir = Integer.parseInt(split[1]);
            f(idx, dir);
        }

        System.out.println(result(gearList));
    }

    private static int result(List<Gear> gearList) {
        int i = 1;
        int ans = 0;
        for (Gear gear : gearList) {
            Integer n = gear.getValue().get(0);
            if (n.equals(1)) {
                ans += i;
            }
            i *= 2;
        }
        return ans;
    }

    private static void f(int idx, int dir) {
        ArrayList<Integer> right = new ArrayList<>();
        ArrayList<Integer> rightDir = new ArrayList<>();
        int rDir = dir;
        for (int i = idx + 1; i <= 3; i++) {
            if (rightCheck(i)) {
                right.add(i);
                if (rDir == -1) {
                    rightDir.add(1);
                    rDir *= -1;
                } else if (rDir == 1) {
                    rightDir.add(-1);
                    rDir *= -1;
                }
            } else {
                break;
            }
        }

        ArrayList<Integer> left = new ArrayList<>();
        ArrayList<Integer> leftDir = new ArrayList<>();
        int lDir = dir;
        for (int i = idx - 1; i >= 0; i--) {
            if (leftCheck(i)) {
                left.add(i);
                if (lDir == -1) {
                    leftDir.add(1);
                    lDir *= -1;
                } else if (lDir == 1) {
                    leftDir.add(-1);
                    lDir *= -1;
                }
            } else {
                break;
            }
        }

        if (dir == 1) {
            gearList.get(idx).rotateClockWise();
        } else {
            gearList.get(idx).rotateCounterClockWise();
        }

        for (int i = 0; i < right.size(); i++) {
            Integer i1 = right.get(i);
            Integer i2 = rightDir.get(i);
            if (i2.equals(1)) {
                gearList.get(i1).rotateClockWise();
            } else {
                gearList.get(i1).rotateCounterClockWise();
            }
        }

        for (int i = 0; i < left.size(); i++) {
            Integer i1 = left.get(i);
            Integer i2 = leftDir.get(i);
            if (i2.equals(1)) {
                gearList.get(i1).rotateClockWise();
            } else {
                gearList.get(i1).rotateCounterClockWise();
            }
        }
    }

    private static boolean leftCheck(int i) {
        Gear gear1 = gearList.get(i + 1);
        Gear gear2 = gearList.get(i);
        return !gear1.getValue().get(6).equals(gear2.getValue().get(2));
    }

    private static boolean rightCheck(int i) {
        Gear gear1 = gearList.get(i - 1);
        Gear gear2 = gearList.get(i);
        return !gear1.getValue().get(2).equals(gear2.getValue().get(6));
    }

    private static List<Gear> getGearList(StringBuilder sb) {
        List<Gear> gearList = new ArrayList<>();
        String[] lines = sb.toString().split("\n");
        for (String line : lines) {
            gearList.add(new Gear(line));
        }
        return gearList;
    }
}

class Gear {
    private List<Integer> value;

    public Gear(String line) {
        String[] split = line.split("");
        this.value = Arrays.stream(split).map(i -> Integer.parseInt(i)).collect(Collectors.toList());
    }

    @Override
    public String toString() {
        return "Gear{" +
                "value=" + value +
                '}';
    }

    public List<Integer> getValue() {
        return value;
    }

    public void rotateClockWise() {
        int size = value.size();
        ArrayList<Integer> newValue = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            newValue.add(value.get((i + 7) % 8));
        }
        this.value = newValue;
    }

    public void rotateCounterClockWise() {
        int size = value.size();
        ArrayList<Integer> newValue = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            newValue.add(value.get((i + 1) % 8));
        }
        this.value = newValue;
    }
}