#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-5-21 16:44
#!@Author : LYC
#!@File : Leecode_containsDuplicate_function2_.PY
class Solution(object):
    def containsDuplicate(self,nums):
        """
        :param nums:a list
        :return: bool
        """
        if len(nums) <=1:
            return False
        elif len(nums) == len(set(nums)):
            return False
        else:
            return True
if __name__ == '__main__':
    ins1 = Solution()
    nums1 = [1,2,1,2,3,4,5,6,8]
    nums2 = [1,23,4,5,6,78,9]
    print(ins1.containsDuplicate(nums1),ins1.containsDuplicate(nums2))