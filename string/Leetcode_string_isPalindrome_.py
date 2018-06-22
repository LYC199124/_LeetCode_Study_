#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-6-20 16:48
#!@Author : LYC
#!@File : Leetcode_string_isPalindrome_.PY
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) ==0:
            return True
        s = [c for c in s.lower() if c.isalnum()]
        return  s == s[::-1]
if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    ins1 = Solution()
    print(ins1.isPalindrome(s))