package Level3;

import java.util.*;

class 몸짱트레이너라이언 {

    public int solution(int n, int m, int[][] timetable) {
        int answer = 0;
        int[] dp = new int[1321];

        fillPeopleArray(timetable, dp);
        answer = findMinDistance(n, dp);

        return answer;
    }

    private void fillPeopleArray(int[][] timetable, int[] dp) {
        for (int[] ints : timetable) {
            for (int cur = ints[0]; cur <= ints[1]; cur++) {
                dp[cur]++;
            }
        }
    }

    private int findMinDistance(int n, int[] dp){
        int max_people = Arrays.stream(dp).max().getAsInt();
        System.out.println(max_people);
        if (max_people <= 1) return 0;
        if (max_people == n*n) return 1;
        if (max_people == n *n /2 + n%2) return 2;

        for (int d = n * n / 2 + n % 2; d > 0; d--){
            for (int i = 0; i < n; i++){
                for (int j = 0; j < n; j++){
                    List<List<Integer>> locker = new ArrayList<>();
                    List<Integer> cur = new ArrayList<>();
                    cur.add(i);
                    cur.add(j);
                    locker.add(cur);

                    for (int y=i; y < n; ++y) {
                        for (int x=0; x<n; ++x) {
                            if (y != i || x > j) {
                                boolean canPush = true;
                                for(List<Integer> lock : locker) {
                                    int dist = Math.abs(lock.get(0) - y) + Math.abs(lock.get(1) - x);
                                    if (dist < d) {
                                        canPush = false;
                                        break;
                                    }
                                }

                                if (canPush) {
                                    List<Integer> next = new ArrayList<>();
                                    next.add(y);
                                    next.add(x);
                                    locker.add(next);

                                    if (max_people == locker.size()) return d;
                                }
                            }
                        }
                    }
                }
            }
        }
        return 0;
    }
}