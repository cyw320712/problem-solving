public class Main {
    public static void main(String[] args) {
        int[] arr = new int[]{1, 4, 7, 8, 2, 6, 5, 3};

        Quick m = new Quick(arr);
        int[] result = m.sort();

        for (int i : result){
            System.out.println(i);
        }
    }
}
