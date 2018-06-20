#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-5-23 15:10
#!@Author : LYC
#!@File : leecode_moveZeroes_function.PY
class Solution(object):
    def moveZeroes(self,nums):
        """
        :param nums: A list Contain zero
        :return: A List Zero all end
        """
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
        return nums
if __name__ == '__main__':
    ins1 = Solution()
    nums = [0, 1, 0, 2, 0, 3, 0, 5]
    print(ins1.moveZeroes(nums))