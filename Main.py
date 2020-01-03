import sys 
import os
from Solution import Solution


if __name__ == '__main__':
   s = Solution(False)
   coins = [8, 3, 1]
   goal = 12
   print(s.driver(coins, goal))
   


