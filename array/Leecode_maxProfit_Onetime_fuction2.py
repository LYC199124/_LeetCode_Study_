#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-5-16 17:16
#!@Author : LYC
#!@File : Leecode_maxProfit_Moretime.PY
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        StartPrice = prices[0]
        if len(prices)<=1:
            return result
        for p in prices:
            result = max(result,p-StartPrice)
            StartPrice = min(StartPrice,p)
        return result
if __name__ == '__main__':
    ins1 = Solution()
    prices = [7,1,5,3,6,4]
    print(ins1.maxProfit(prices))






