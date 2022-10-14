package Level2;

public class 단체사진찍기 {
    private static String[] name = new String[]{"A", "C", "F", "J", "M", "N", "R", "T"};
    private String[] relation;
    private int answer = 0;
    boolean[] visited;

    public int solution(int n, String[] data) {
        visited = new boolean[8];
        relation = data;

        backtrack("");

        return answer;
    }

    private void backtrack(String seq) {
        if (seq.length() == 8) {
            if (isValid(seq)) answer ++;
            return;
        }

        for (int i = 0; i < 8; i++){
            if (!visited[i]){
                visited[i] = true;
                String s = seq + name[i];
                backtrack(s);
                visited[i] = false;
            }
        }
    }

    private boolean isValid(String seq) {
        for (String s : relation) {
            System.out.println(s);
            int px = seq.indexOf(s.charAt(0));
            int py = seq.indexOf(s.charAt(2));
            char op = s.charAt(3);
            int dist = s.charAt(4) - '0' + 1;

            switch (op) {
                case '=':
                    if (!(Math.abs(px - py) == dist))
                        return false;
                    break;
                case '>':
                    if (!(Math.abs(px - py) > dist))
                        return false;
                    break;
                case '<':
                    if (!(Math.abs(px - py) < dist))
                        return false;
                    break;
            }
        }
        
        // relation이 없는 경우
        return true;
    }
}
