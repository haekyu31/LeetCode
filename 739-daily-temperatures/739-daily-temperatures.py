class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        Day = [0]*len(temp)
        Stack = []
        for i, v in enumerate(temp):
            while Stack and Stack[-1][1] < temp[i]:
                idx, value = Stack.pop()
                Day[idx] = i - idx
            Stack.append([i,v])
        return Day
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # WaitDay = [0 for i in range(len(temperatures))]
        # Stack = [[-1, temperatures[0]] ]
        # temperatures.pop(0)
        # for i, tem in enumerate(temperatures):
        # # if increasead temperature
        #     while Stack and Stack[-1][1] < tem:
        #         Last_idx, Last_tem = Stack.pop()
        #         WaitDay[Last_idx + 1] = i - Last_idx
        #         print(Stack, temperatures, Last_idx, WaitDay)
        #     else:
        #         Stack.append([i, tem])
        #         print(Stack, temperatures, Last_idx, WaitDay)
        # return WaitDay