class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        a = sorted(nums1 + nums2)
        mid = len(a) // 2

        if len(a) % 2 == 0:
            med = (a[mid - 1] + a[mid]) / 2.0
            return med
        else:
            return float(a[mid])
