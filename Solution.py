
import os 
import sys

class Solution:

    DEBUG = False

    def __init__(self, debugMode:bool):
        if debugMode == True:
            DEBUG = True
        else:
            DEBUG = False
        pass
    

    def getNCoins(self, n)->list:
        coins = self.coins[0:n]
        print(coins)
        coins.sort(reverse=True)
        return coins
    
    def driver(self, coins:[], goal:int):

        ##create the array
        arr = []*len(coins)
        for i in range(0, len(coins)+1):
            temp = []*goal
            arr.append(temp)
        

        ##initialize array with -1
        for i in range(0, len(coins)+1):
            for j in range(0, goal+1):
                arr[i].append(-1)
        
        #reinitialize first row with some max value
        for i in range(0, goal+1):
            arr[0][i] = 50
        
        ##reinitialize first column with 0
        for j in range(1, len(coins)+1):
            arr[j][0] = 0

        ##if value of coin  > value of current sub-goal then put 1000 in that spot b/c sub-goal cannot be made with current coin
        ##else if value of coin <= current goal, decide whether or not to use the current coin to make the current sub-goal
        ##to do so. You do so by looking in the cell of the table at the current row and the current goal - the value of the coin. 
        #This represents the cell which will let you decide if you want to keep the current coin. The other option is to check 
        ##the place where the current goal was made without the current coin which would be in the same column minus 1 row

        ##the rows represent the ith coin vith a value of coins[i-1]
        ##i.e. the first coin has a value of coins[0]
        for i in range(1, len(coins)+1):
            ##j represents the values of the current sub-goals
            ##the sub-goals increment 1 unit at a time
            for j in range(1, goal+1):
                ##if the current sub-goal is less than the value of the current coin, just put a big ass number in the
                ##arr[i][j] representing the current coin and the current subgoal indiciating that the current subgoal cannot
                ##be made by the current coin 
                if j < coins[i-1]:
                    arr[i][j] = 50
                
                ##otherwise we need to know if the current sub-goal can be made by the current coin.
                ##we do so by checking if the current sub goal can be made with less coins by including the current coin or not.
                ##the
                else:
                    arr[i][j] = min(1+arr[i][j-coins[i-1]], arr[i-1][j])

        return arr[len(coins)][goal]
    

    def min(self, a, b):
        if a < b:
            return a 
        else:
            return b

    if DEBUG == True:
        def arrToString(self, arr):
        
            s = ""
            for i in range(0, len(arr)):
                for j in range(0, len(arr[0])):
                    if arr[i][j] >= 10:
                        s+= str(arr[i][j])
                    else:
                        s += " "
                        s+= str(arr[i][j])
                    s+= " "            
                s+="\n"
        
            return s
        

        

