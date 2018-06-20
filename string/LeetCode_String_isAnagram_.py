#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-6-20 16:24
#!@Author : LYC
#!@File : LeetCode_String_isAnagram_.PY
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls = list(s)
        ls.sort()
        lt = list(t)
        lt.sort()
        return ls == lt