#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-6-25 14:28
#!@Author : LYC
#!@File : LeetCode_String_countAndSay.PY
class Solution(object):
    def countAndSay(self,n):
        """
        :param n: int
        :return: str
        """
        s = '1'
        for _ in range(n - 1):
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count) + let
                    let = l
                    count = 1
            temp += str(count) + let
            s = temp
        return s