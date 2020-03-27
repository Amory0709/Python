import sys

class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        # Step 1: coinChange(27 - lastcoin) + lastcoin(1)
        # Step 2: f(x) = 1 + min(f(x - coin) for coin in coins)
        # Step 3: init f(0) = 0    x < 0 --> +inf
        # Step 4: for 0 -> amount
        
        countCoins = [sys.maxsize for i in range(amount+1)]
        countCoins[0] = 0
        
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0 and countCoins[i - coin] != sys.maxsize:
                # pay attention that sys.max and sys.max + 1 are not the same
                # and write the condition transfer equation according to your design
                    countCoins[i] = min(countCoins[i], countCoins[i - coin] + 1) 
            
        
        if countCoins[amount] == sys.maxsize:
            return -1
            
        return countCoins[amount]
