package Hard;

public class median_of_two_sorted_arrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int total = nums1.length + nums2.length;
        int[] nums = new int[total];

        int index1 = 0, index2 = 0, index = 0;

        while (index1 < nums1.length && index2 < nums2.length) {
            nums[index++] = nums1[index1] < nums2[index2] ? nums1[index1++] : nums2[index2++];
        }

        while (index1 != nums1.length)
            nums[index++] = nums1[index1++];

        while (index2 != nums2.length)
            nums[index++] = nums2[index2++];


        return total % 2 == 0 ? (double)(nums[total / 2 - 1] + nums[total / 2]) / 2: nums[total / 2];
    }
}