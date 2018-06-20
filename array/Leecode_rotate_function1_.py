#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-5-18 15:03
#!@Author : LYC
#!@File : Leecode_rotate_function1_.PY
class Solution(object):
    def rotate(self, nums, key):
        return nums[len(nums) - key:] + nums[:len(nums) - key]
if __name__ == '__main__':
    key = 2
    nums = [-1,-100,3,99]
    inst1 = Solution()
    print(inst1.rotate(nums,key))

