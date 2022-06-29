import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static int white = 0;
    public static int blue = 0;
    public static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int size = Integer.parseInt(br.readLine());
        board = new int[size][size];

        for (int i = 0; i < size; i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");

            for(int j = 0; j < size; j++){
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        partition(0, 0, size);

        System.out.println(white);
        System.out.println(blue);
    }

    private static void partition(int row, int col, int size) {
        int flag = board[row][col];

        for (int i=row; i < row + size; i++){
            for (int j=col; j < col + size; j++){
                if (board[i][j] != flag){
                    flag = -1;
                    break;
                }
            }
        }

        if (flag == 0) {
            white++;
        }
        else if (flag == 1) {
            blue++;
        }
        else {
            partition(row, col, size/2);
            partition(row + size/2, col, size/2);
            partition(row, col + size/2, size/2);
            partition(row + size/2, col + size/2, size/2);
        }
    }
}
