#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-5-16 10:40
#!@Author : LYC
#!@File : Leecode_Remove_Duplicates.PY
class Solution(object):
    def RemoveDuplicates(self,nums):
        list1 = [nums[0]]
        if len(nums)<=1:
            return  len(nums),list1
        i = 0
        list1 = [nums[0]]
        for j in (range(1,len(nums))):
            if nums[i] != nums[j]:
                list1.append(nums[j])
                i+=1
                nums[i] = nums[j]
        return  list1,i+1
if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    s1 = Solution()
    print(s1.RemoveDuplicates(nums))
    nums2 =[1,2,3,4,5,6,6,7,7,8,9]
    print(s1.RemoveDuplicates(nums2))