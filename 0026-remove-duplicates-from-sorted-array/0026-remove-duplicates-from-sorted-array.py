class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = sorted(set(nums))
        k = len(nums)
        print("{} nums = {}".format(k, nums))

        return k
