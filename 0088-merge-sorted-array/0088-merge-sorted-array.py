class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Start filling from the end of nums1
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


''''class Solution(object):
    def merge(self, nums1, m, nums2, n):
        a=[]
        nums1 = [1,2,3,0,0,0]
        l=len(nums1)
        o=len(nums2)
        for i in range(l):
          if nums1[i]!=0:
            a.append(nums1[i])
        for j in range(o):
          a.append(nums2[j])
        nums1=sorted(a)
        return nums1
sol = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3

result = sol.merge(nums1, m, nums2, n)
print(result) '''
