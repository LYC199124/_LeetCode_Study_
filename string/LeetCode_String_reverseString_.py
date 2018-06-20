#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-6-13 10:33
#!@Author : LYC
#!@File : LeetCode_String_reverseString_.PY
class Solution(object):
    def reverseString(self,s):
        """
        :param s: A str
        :return: Str
        """
        return s[::-1]
if __name__ == '__main__':
    ins1 = Solution()
    s = 'What a Beatiful Girl'
    print(ins1.reverseString(s))
