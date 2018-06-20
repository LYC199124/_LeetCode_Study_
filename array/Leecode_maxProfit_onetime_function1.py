#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-5-16 16:27
#!@Author : LYC
#!@File : Leecode_maxProfit_onetime_.PY
class Solution(object):
    def maxProfit(self,price):
        """
        :param price: A list
        :return result: Type int
        """
        result = 0
        for i in (range(0,len(price)-1)):
            for j in (range(i+1,len(price))):
                result = max(result,price[j]-price[i])
        return result
if __name__ == '__main__':
    ins1 = Solution()
    price = [7,1,5,3,6,4]
    print(ins1.maxProfit(price))