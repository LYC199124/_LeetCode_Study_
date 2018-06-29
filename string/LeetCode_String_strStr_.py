#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-6-25 10:48
#!@Author : LYC
#!@File : LeetCode_String_strStr_.PY
class Solution(object):
    def strStr(self,haystack,needle):
        """
        :param haystack: str
        :param needle:str
        :return: int
        """
        if len(needle)==0:
            return 0
        for i in range(0,len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] ==needle:
                return i
        return -1
if __name__ == '__main__':
    ins1 = Solution()
    h1 = "hello"
    n1 = "ll"
    h2 = ''
    n2 = ''
    h3 = 'aaaaaaaaaa'
    n3 = 'bbsa'
    print(ins1.strStr(h1,n1),ins1.strStr(h2,n2),ins1.strStr(h3,n3),ins1.strStr(h1,n3))