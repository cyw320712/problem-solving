package Level3;

import java.util.*;

class Point {
    int x;
    int y;
    char c;

    Point (int x, int y, char c) {
        this.x = x;
        this.y = y;
        this.c = c;
    }
}

class 리틀사천성 {
    private List<String> result;
    private char[][] game;
    private HashMap<Character, List<Point>> tiles;

    public String solution(int m, int n, String[] board) {
        result = new ArrayList<>();
        game = new char[m][n];
        tiles = new HashMap<>();

        for (int i = 0; i < board.length; i++) {
            String line = board[i];
            for (int j = 0; j < line.length(); j++) {
                Point cur = new Point(i, j, line.charAt(j));
                if (line.charAt(j) != '.' && line.charAt(j) != '*'){
                    List<Point> list = new ArrayList<>();
                    if (tiles.containsKey(line.charAt(j)))
                        list = tiles.get(line.charAt(j));
                    list.add(cur);
                    tiles.put(line.charAt(j), list);
                }
                game[i][j] = line.charAt(j);
            }
        }

        StringBuilder s = new StringBuilder();
        List<Character> keyList = new ArrayList<>(tiles.keySet());
        Collections.sort(keyList);
        int dest = keyList.size();
        boolean flag = true;
        while (flag) {
            flag = false;

            for (Character cur : keyList) {
                List<Point> twoPoints = tiles.get(cur);

                if (isValid(twoPoints)) {
                    s.append(cur);
                    keyList.remove(cur);
                    Point p1 = twoPoints.get(0);
                    Point p2 = twoPoints.get(1);
                    game[p1.x][p1.y] = '.';
                    game[p2.x][p2.y] = '.';
                    flag = true;
                    break;
                }
            }

            if (s.length() == dest) return s.toString();
        }

        return "IMPOSSIBLE";
    }

    private boolean isValid(List<Point> twoPoints){
        Point p1 = twoPoints.get(0);
        Point p2 = twoPoints.get(1);

        int x1 = p1.x;
        int x2 = p2.x;
        int y1 = p1.y;
        int y2 = p2.y;

        if (y1 < y2) {
            if(linearColumnCheck(y1, y2, x1, p1.c) && linearRowCheck(x1, x2, y2, p1.c)){
                return true;
            }
            if(linearRowCheck(x1, x2, y1, p1.c) && linearColumnCheck(y1, y2, x2, p1.c)){
                return true;
            }
        }else {
            if (linearRowCheck(x1, x2, y2, p1.c) && linearColumnCheck(y2, y1, x1, p1.c)) {
                return true;
            }
            if (linearColumnCheck(y2, y1, x2, p1.c) && linearRowCheck(x1, x2, y1, p1.c)) {
                return true;
            }
        }

        return false;
    }

    boolean linearRowCheck(int r1, int r2, int c, char a){
        for(int i = r1; i < r2+1; i++){
            if(game[i][c] != '.' && game[i][c] != a)
                return false;
        }
        return true;
    }

    boolean linearColumnCheck(int c1, int c2, int r, char a){
        for(int i = c1; i < c2+1; i++){
            if(game[r][i] != '.' && game[r][i] != a)
                return false;
        }
        return true;
    }
}