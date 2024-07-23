class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        x = 1
        while x < n:
            x = x * 2
        return x == n

obj = Solution()
print(obj.isPowerOfTwo(1))  
print(obj.isPowerOfTwo(16)) 
print(obj.isPowerOfTwo(3))  
