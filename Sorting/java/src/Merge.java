
public class Merge {
    int[] arr;

    public Merge (int[] arr){
        this.arr = arr;
    }

    public int[] sort(){
        divide(0, arr.length-1);

        return arr;
    }

    private void divide(int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            divide(left, mid);
            divide(mid+1, right);
            merge(left, mid, right);
        }
    }

    private void merge(int left, int mid, int right) {
        int[] temporal = new int[right+1];
        int lpoint = left, rpoint = mid+1;
        int i = left;

        while (lpoint <= mid && rpoint <= right) {
            temporal[i++] = arr[lpoint] <= arr[rpoint] ? arr[lpoint++] : arr[rpoint++];
        }

        while (lpoint <= mid){
            temporal[i++] = arr[lpoint++];
        }

        while (rpoint <= right) {
            temporal[i++] = arr[rpoint++];
        }

        for (int l = left; l <= right; l++) {
            arr[l] = temporal[l];
        }
    }
}
