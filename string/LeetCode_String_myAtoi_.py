#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-6-22 16:58
#!@Author : LYC
#!@File : LeetCode_String_myAtoi_.PY
class Solution(object):
    def myAtoi(self,str):
        """
        :param str:str
        :return: int
        """
        Si = str.strip()
        k = len(Si)
        if k ==0:
            return 0
        if Si[0] != '-' and Si[0] !='+' and not Si[0].isdigit():
            return 0
        elif Si[0] =='-' or Si[0] == '+':
            if len(Si)==1:
                return 0
            elif not Si[1].isdigit():
                return 0
            for i in range(1,len(Si)):
                if not Si[i].isdigit():
                    k = i
                    break
        elif Si[0].isdigit():
            for i in range(0,len(Si)):
                if not Si[i].isdigit():
                    k =i
                    break
        s = Si[0:k]
        if int(s) >= 2147483647:
            return 2147483647
        elif int(s) <=-2147483648:
            return -2147483648
        else:
            return int(s)
if __name__ == '__main__':
    ins1 = Solution()
    str = "+"
    str2 = '-2147483648'
    str3 = "fdsafs"
    str4 = "     738787dfsdsds3343443"
    print(ins1.myAtoi(str),ins1.myAtoi(str2),ins1.myAtoi(str3),ins1.myAtoi(str4))






