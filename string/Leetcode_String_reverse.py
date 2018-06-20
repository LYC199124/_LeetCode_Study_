#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-6-13 14:53
#!@Author : LYC
#!@File : Leetcode_String_reverse.PY
class Solution(object):
    def reverse(self,x):
        """
        :param x: int
        :return:int
        """
        s = str(x)
        res = int ('-'+s[-1:-len(s):-1]) if s[0] == '-' else int(s[::-1])
        return res if res > -2**31 and res< 2**31-1 else 0