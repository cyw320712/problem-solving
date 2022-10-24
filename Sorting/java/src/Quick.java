public class Quick {
    int[] arr;

    public Quick (int[] arr) {
        this.arr = arr;
    }

    public int[] sort() {
        pivoting(0, arr.length - 1);

        return arr;
    }

    private void pivoting(int start, int end) {
        if (start < end) {
            int pivot = partition(start, end);
            pivoting(start, pivot-1);
            pivoting(pivot + 1, end);
        }
    }


    private int partition(int start, int end) {
        int low = start, high = end;
        int pivot = arr[start];

        while (low < high) {
            while (low <= end && arr[low] < pivot) {
                low ++;
            }
            while (high >= start && arr[high] > pivot) {
                high --;
            }

            if (low < high) {
                swap(low, high);
            }
        }

        return high;
    }

    private void swap(int low, int high) {
        int temp = arr[low];
        arr[low] = arr[high];
        arr[high] = temp;
    }
}
