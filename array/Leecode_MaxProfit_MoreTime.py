#!/usr/bin/env python3.0
#!-*coding:utf-8 -*-
#!@Time :2018-5-16 17:42
#!@Author : LYC
#!@File : Leecode_MaxProfit_MoreTime.PY
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0
        result = 0
        StartPrices = prices[0]
        for p in  prices:
            if p>StartPrices:
                result += p-StartPrices
                StartPrices = p
            else:
                StartPrices = min(StartPrices,p)
        return result
if __name__ == '__main__':
    ins1 = Solution()
    prices = [1,2,3,4,5,8,14,16]
    print(ins1.maxProfit(prices))
