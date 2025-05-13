class Solution:
    def findMedianSortedArrays(self, nums1: [1,3,4,4], nums2: [2,3,4]) -> float:
        arr = nums1 + nums2
        arr.sort()
        if len(arr) % 2 != 0:
            return float(arr[len(arr)//2])
        else:
            return float((arr[len(arr)//2-1] + arr[len(arr)//2])/2)