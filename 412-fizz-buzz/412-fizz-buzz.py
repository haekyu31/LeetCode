class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
#         answer = []   
#         for i in range(1, n+1):
#             if i % 3 ==0 and i % 15 !=0:
#                 answer.append("Fizz")
#             elif i % 5 ==0 and i % 15 !=0:
#                 answer.append("Buzz")
#             elif i % 15 ==0:
#                 answer.append("FizzBuzz")
#             else:
#                 answer.append(str(i))
            
            

#         return answer
        
        answer = []
        for i in range(1, n+1):
            if (i % 3 == 0) and (i % 5 == 0) :
                answer.append("FizzBuzz")
            elif (i % 3) == 0 :
                answer.append("Fizz")
            elif (i % 5) == 0 :
                answer.append("Buzz")
            else : 
                answer.append(str(i))
        return answer
             
        