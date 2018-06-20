#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-5-22 17:45
#!@Author : LYC
#!@File : Leecode_plusOne_function1_.PY
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        count = len(digits)
        k=0
        for i in (range(0,count)):
            k+= digits[i]*10**(count-i-1)
        return [int (c) for c in str(k+1)]
if __name__ == '__main__':
    isn = Solution()
    nums = [1,2,3]
    print(isn.plusOne(nums))

