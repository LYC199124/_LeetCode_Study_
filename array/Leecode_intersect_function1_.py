#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-5-22 11:07
#!@Author : LYC
#!@File : Leecode_intersect_function1_.PY
class Solution(object):
    def intersect(self, nums1, nums2):
        list_interset = []
        for p in nums1:
            for k in nums2:
                if p == k:
                    list_interset.append(p)
                    nums2.remove(k)
                    break
        return list_interset
if __name__ == '__main__':
    ins1 = Solution()
    nums1 =[1,2,2,1]
    nums2 =[2,2]
    print(ins1.intersect(nums1,nums2))