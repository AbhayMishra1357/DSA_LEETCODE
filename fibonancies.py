# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 0:
#             return 0
#         elif n==1:
#             return 1
#         else:
#             return int(self.fib(n-1) + self.fib(n-2))

# a=Solution()
# a.fib(2)

class Solution:
    def fib(self, n: int) -> int:
        if n >=2 :
            return int(self.fib(n-1) + self.fib(n-2))
        else:
            return n 

a=Solution()
a.fib(2)