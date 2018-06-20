#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-6-14 10:14
#!@Author : LYC
#!@File : LeetCode_String_firstUniqChar.PY
class Solution(object):
    def firstUniqChar(self, s):
        """
        :param s:str
        :return: int
        """
        l = 'qwertyuiopasdfghjklzxcvbnm'
        index = []
        for i in letters:
            if s.count(i) == 1:
                index.append(s.index(i))
        if len(index) > 0:
            return min(index)
        else:
            return -1

class Solution2(object):
    def firstUniqChar(self, s):
        l = 'qwertyuiopasdfghjklzxcvbnm'
        index = [s.index(i) for i in l if s.count(i) == 1 ]
        return min(index) if len(index) > 0 else -1