class Solution(object):
    def addBinary(self, a, b):
        sum_binary = bin(int(a, 2) + int(b, 2))[2:]
        return sum_binary