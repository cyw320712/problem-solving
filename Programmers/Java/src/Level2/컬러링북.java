package Level2;

import java.util.LinkedList;
import java.util.Queue;

import static java.lang.Math.max;

class Point {
    int x;
    int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Solution {
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        boolean[][] visited = new boolean[m][n];
        int[] dx = new int[]{-1, 0, 1, 0};
        int[] dy = new int[]{0, -1, 0, 1};

        Queue<Point> q = new LinkedList<>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if(!visited[i][j] && picture[i][j] != 0) {
                    numberOfArea += 1;
                    q.add(new Point(i, j));
                    visited[i][j] = true;

                    int curSum = 0;
                    int color = picture[i][j];

                    while (!q.isEmpty()) {
                        Point cur = q.peek();
                        q.remove(cur);
                        curSum += 1;

                        for (int k=0; k< 4; k++){
                            int nx = cur.x + dx[k];
                            int ny = cur.y + dy[k];

                            if (nx < m && nx >= 0 && ny < n && ny >= 0){
                                if (!visited[nx][ny] && picture[nx][ny] == color){
                                    visited[nx][ny] = true;
                                    q.add(new Point(nx, ny));
                                }
                            }
                        }
                    }

                    maxSizeOfOneArea = max(maxSizeOfOneArea, curSum);
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}
