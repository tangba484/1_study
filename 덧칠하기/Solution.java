package 덧칠하기;

class Solution {
    public int solution(int n, int m, int[] section) {
        int idx = section[0] - 1;
        int cnt = 0;
        for (int a : section) {
            if (idx < a) {
                cnt += 1;
                idx = a - 1 + m;
            }
        }
        return cnt;
    }
}
