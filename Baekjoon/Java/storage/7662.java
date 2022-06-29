import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeMap;

public class Main {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());

            // 양방향 PQ는 TreeMap
            TreeMap<Integer, Integer> doublePQ = new TreeMap<>();

            for (int j = 0; j < N; j++) {
                String[] input = br.readLine().split(" ");
                char cmd = input[0].charAt(0);
                int n = Integer.parseInt(input[1]);

                if (cmd == 'I') {
                    doublePQ.put(n, doublePQ.getOrDefault(n, 0)+1);
                }
                else {
                    if (doublePQ.size() == 0)
                        continue;

                    int num = n == 1 ? doublePQ.lastKey() : doublePQ.firstKey();
                    if (doublePQ.put(num, doublePQ.get(num) - 1) == 1) {
                        doublePQ.remove(num);
                    }
                }
            }

            System.out.println(doublePQ.size()==0 ? "EMPTY" : doublePQ.lastKey() + " " + doublePQ.firstKey());
        }
    }
}
