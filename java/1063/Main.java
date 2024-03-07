import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static Location stone;
    static int[] now;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Location king = new Location(st.nextToken());
        stone = new Location(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            now = new int[]{king.getRow(), king.getCol()};
            moveKing(king, s);
            if (king.getRow() == stone.getRow() && king.getCol() == stone.getCol()) {
                moveStone(king, stone, s);
            }
        }
        System.out.println(king.toString());
        System.out.println(stone.toString());
    }

    private static void moveStone(Location king, Location stone, String s) {
        int[] dr = {0, 0, 1, 1, 1, -1, -1, -1};
        int[] dc = {-1, 1, -1, 0, 1, -1, 0, 1};
        int nr = stone.getRow() + dr[getDir(s)];
        int nc = stone.getCol() + dc[getDir(s)];
        if (isValid(nr, nc)) {
            stone.setRow(nr);
            stone.setCol(nc);
        } else {
            king.setRow(now[0]);
            king.setCol(now[1]);
        }
    }

    private static void moveKing(Location king, String s) {
        int[] dr = {0, 0, 1, 1, 1, -1, -1, -1};
        int[] dc = {-1, 1, -1, 0, 1, -1, 0, 1};
        int nr = king.getRow() + dr[getDir(s)];
        int nc = king.getCol() + dc[getDir(s)];
        if (isValid(nr, nc)) {
            king.setRow(nr);
            king.setCol(nc);
        }
    }

    private static boolean isValid(int nr, int nc) {
        return (1 <= nr && nr <= 8) && (1 <= nc && nc <= 8);
    }

    private static int getDir(String s) {
        switch (s) {
            case "L":
                return 0;
            case "R":
                return 1;
            case "LT":
                return 2;
            case "T":
                return 3;
            case "RT":
                return 4;
            case "LB":
                return 5;
            case "B":
                return 6;
            case "RB":
                return 7;
            default:
                return 99;
        }
    }
}

class Location {
    private int row;
    private int col;

    Location(String s) {
        this.col = s.charAt(0) - 64;
        this.row = Integer.parseInt(String.valueOf(s.charAt(1)));
    }

    public int getRow() {
        return row;
    }

    public void setRow(int row) {
        this.row = row;
    }

    public int getCol() {
        return col;
    }

    public void setCol(int col) {
        this.col = col;
    }

    @Override
    public String toString() {
        return String.valueOf((char) (col + 64)) + row;
    }
}