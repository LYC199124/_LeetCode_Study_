#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-5-21 10:11
#!@Author : LYC
#!@File : Leecode_containsDuplicate_fuction1_.PY
class Solution(object):
    def containsDuplicate(self,nums):
        """
        :param nums: a lis
        :return: bool
        """
        if len(nums)<=1:
            return False
        for i in (range(0,len(nums))):
            for j in (range(i+1,len(nums))):
                if nums[i] == nums[j]:
                    return True
        return False
if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    ins1=Solution()
    print(ins1.containsDuplicate(nums))
