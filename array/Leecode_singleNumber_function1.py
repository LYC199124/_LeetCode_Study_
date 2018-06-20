#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-5-21 16:57
#!@Author : LYC
#!@File : Leecode_singleNumber_function1.PY
class Solution(object):
    def singleNumber(self,nums):
        """
        :param nums: a not null list
        :return: int
        """
        for p in nums:
            if nums.count(p) == 1:
                return p
if __name__ == '__main__':
    nums = [1,1,2,2,3,3,4,4,5]
    ins1 = Solution()
    print(ins1.singleNumber(nums))