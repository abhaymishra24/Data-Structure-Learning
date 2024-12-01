
// # Merge Sorted Arra - leetcode (easy)

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
    int midx = m - 1;
        int nidx = n - 1;
        int right = m + n - 1;

        while (nidx >= 0) {
            if (midx >= 0 && nums1[midx] > nums2[nidx]) {
                nums1[right] = nums1[midx];
                midx--;
            } else {
                nums1[right] = nums2[nidx];
                nidx--;
            }
            right--;
        }        
    }
}

// This code is written in Python - for same problem -

// class Solution:
//     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
//         """
//         Do not return anything, modify nums1 in-place instead.
//         """
//         if n == 0 :return
//         len1 = len(nums1)
//         end_idx = len1-1
//         while n > 0 and m > 0 :
//             if nums2[n-1] >= nums1[m-1]:
//                 nums1[end_idx] = nums2[n-1]
//                 n-=1
//             else:
//                 nums1[end_idx] = nums1[m-1]
//                 m-=1
//             end_idx-=1
//         while n > 0:
//             nums1[end_idx] = nums2[n-1]
//             n-=1
//             end_idx-=1

// double a = 0.1;
// double b = 0.2;
// System.out.println(a + b == 0.3);

// Correct Answer:

// false

// Explanation:
// The output is false. This is due to the way floating-point numbers are represented in binary. Most decimal fractions cannot be represented exactly as binary fractions, leading to small rounding errors.
// In this case, 0.1 + 0.2 is slightly larger than 0.3 when represented in binary floating-point. For precise decimal calculations, it's recommended to use BigDecimal instead of double.
            
            