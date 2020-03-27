# LintCode 114. Unique Path
[link](https://www.lintcode.com/problem/unique-paths/description)

*Method*: DP

*Time Complexity*: O(mn)

*Space Complexity*: O(mn)

## 4 Steps for DP
### Step1: Define condition
* The last Step:
To get to the place [m-1][n-1], we can only move from [m-2][n-1] or [m-1[n-2].
And the unique path of [m-1][n-1] is equal to the sum of [m-2][n-1] or [m-1[n-2].

* Sub-problem:
So we convert the problem to sum the left and upper node's unique path count.

### Step2: Condition Transfer Equation
   **f(m,n) = f(m-1, n)+f(m, n-1)**

### Step3: Initial Condition and border situation
* count[0][0] = 1
* count[m][0] = 1
* count[0][n] = 1

### Step4: Calculation Order
**Principle: when we try to figure out f(x), the conditions we need to use are already calculated.**

f(1,1) -> f(1,2) -> ... -> f(2,1), f(2,2)....

Finally return the result.

## Code is realized as below:
```python
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        countPath = [[0 for _ in range(n)] for _ in range(m)]
        # initiate value
        countPath[0][0] = 1
        
        # for i in range(n):
        #     countPath[0][i] = 1
        # for i in range(m):
        #     countPath[i][0] = 1 #error1 wrote i as m
            
        # # m =  1, [1][1], [1][2] m = 2...
        # for row in range(1, m):
        #     for col in range(1, n):
        #         countPath[row][col] = countPath[row-1][col] + countPath[row][col-1]
        
        # make initiation in the loop
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    countPath[row][col] = 1
                else:
                    countPath[row][col] = countPath[row-1][col] + countPath[row][col-1]
        
        return countPath[m-1][n-1] # wrote m, n instead of m-1, n-1
```
