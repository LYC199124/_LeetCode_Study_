#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-5-23 10:58
#!@Author : LYC
#!@File : Leecode_moveZeroes_function1_.PY
class Solution(object):
    def moveZeroes(self,nums):
        """
        :param nums: A list Contain zero
        :return: A List Zero all end
        """
        if len(nums) <=1:
            return nums
        for p in nums:
            if p == 0:
                nums.remove(p)
                nums.append(0)
                print(p)
            else:
                pass
        return nums
if __name__ == '__main__':
    ins1 = Solution()
    nums = [0,1,0,2,0,3,0,5]
    print(ins1.moveZeroes(nums))