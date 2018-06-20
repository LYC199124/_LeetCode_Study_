#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-5-22 10:59
#!@Author : LYC
#!@File : Leecode_singleNumber_function2_.PY
class Solution(object):
    """
    :type nums :list[int]
    :rtype : int
    """
    def singleNumber(self,nums):
        num = 0
        for p in nums:
            num ^= p
        return num
if __name__ == '__main__':
    ins1 = Solution()
    nums1 = [1,1,2,2,3,3,4,5,5,4,6]
    nums2 = [1,2,2,3,3,4,4,5,5,]
    print(ins1.singleNumber(nums1),ins1.singleNumber(nums2))