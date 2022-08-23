class Solution:
    def fib(self, n: int) -> int:
        if n ==0 :
            return 0
        if n == 1:
            return 1
        return self.fib(n-1)+self.fib(n-2)
            
#     def Recur(self,n):
#         if n == 0: 
#             return 0
#         if n == 1:
#             return 1
#         return self.Recur(n-1)+ self.Recur(n-2)
    
#     def fib(self, n: int) -> int:
#         Answer = self.Recur(n)
#         return Answer
      
    