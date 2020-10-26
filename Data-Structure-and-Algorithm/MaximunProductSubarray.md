# LintCode 191. Maximun Product Subarray
[link](https://www.lintcode.com/problem/maximum-product-subarray/description)

--------------------below need to be editted---------------------------------
*Method*: DP

*Time Complexity*: O(kn)  (k is the coins' count）

(动态规划的时间复杂度 = 状态数 * 状态转移代价)

(Time Complexity of DP = number of conditions * cost of condition transfer)

*Space Complexity*: O(n)
## 4 Steps for DP
With an Example:

coins = [2,5,7]

amount = 27

### Step1: Define condition
* The last Step:
To get to the least coins we needed to reach total amount 27, we should know the least coins we need to get to 25, 22, 20.

So the least coins we need to get to 27 converts to the least coins we need to get to 25/22/20 and then add 1.

* Sub-problem:
So we convert the problem to count the least coin number we need to get to total amount - coin.

### Step2: Condition Transfer Equation
   **f(amount) = min(f(amount - coin1), f(amount - coin2),..., f(amount - coin2)) + 1**
   
   or **f(amount) = min(f(amount - coin1)+1, f(amount - coin2)+1,..., f(amount - coin2)+1)**

### Step3: Initial Condition and border situation
* count[0] = 0
* negtive amount equals to the positive infinite(as we are counting the minimum).

### Step4: Calculation Order
**Principle: when we try to figure out f(x), the conditions we need to use are already calculated.**

f(1) -> f(2) -> ... -> f(amount)

Finally return the result.

## Code as below:
```python
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
```
