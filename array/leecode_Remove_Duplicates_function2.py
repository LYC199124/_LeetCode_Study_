#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-5-16 11:52
#!@Author : LYC
#!@File : leecode_Remove_Duplicates_function2.PY
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if len(nums) <=1:
            return len(nums),nums
        while(i<len(nums)-1):
            if nums[i] ==nums[i+1]:
               nums.remove(nums[i])
            else:
                i+=1
        return i+1,nums
if __name__ == '__main__':
    nums =[1,2,3,3,4,5,6,6]
    isins1 = Solution()
    print(isins1.removeDuplicates(nums))
