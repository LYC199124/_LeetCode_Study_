#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-5-23 15:18
#!@Author : LYC
#!@File : Leecode_twoSum_function1.PY
class Solution(object):
    def twoSum(self,nums,target):
        """
        :param nums:  list[int]
        :param target: int
        :return: list[int]
        """
        List_Return = []
        for i in range(len(nums)):
            values = target - nums[i]
            for k in range(i+1,len(nums)):
                if nums[k] == values:
                    List_Return.append(i)
                    List_Return.append(k)
        return list(set(List_Return))

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    isins1 = Solution()
    print(isins1.twoSum(nums,target))