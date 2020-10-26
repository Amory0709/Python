# LintCode 116. Jump Game
[link](https://www.lintcode.com/problem/jump-game/description)

*Method*: DP

*Time Complexity*: O(n<sup>2</sup>) 

*Space Complexity*: O(n)
## 4 Steps for DP

### Step1: Define condition
- The last Step: Jumped from stone i, i < n-1
    - Frog can jump to stone i
    - The last step does not exceed the maximum jump distance: n-1 - i <= a<sub>i</sub>

==> Can frog jump to stone i => sub problem

* Sub-problem:
f(i) -> if frog can reach stone i

### Step2: Condition Transfer Equation
   **f(j) = OR<sub>0<=i<j</sub>(f(j) AND i + a[i] >= j)**

### Step3: Initial Condition and border situation
* f[0] = True

### Step4: Calculation Order
**Principle: when we try to figure out f(x), the conditions we need to use are already calculated.**

f(1) -> f(2) -> ... -> f(n-1)

Finally return the result.

## Code as below:
```python
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        n = len(A)
        passed = [False for _ in range(n)]
        
        # initialization
        passed[0] = True
        
        for stone in range(1,n):
            for before in range(stone):
                if passed[before] and A[before] + before >= stone:
                    passed[stone] = True
                    break
        
        return passed[-1]
```
