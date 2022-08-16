class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        WaitDay = [0 for i in range(len(temperatures))]
        Stack = [[-1, temperatures[0]] ]
        temperatures.pop(0)
        for i, tem in enumerate(temperatures):
        # if increasead temperature
            while Stack and Stack[-1][1] < tem:
                Last_idx, Last_tem = Stack.pop()
                WaitDay[Last_idx + 1] = i - Last_idx
            else:
                Stack.append([i, tem])
        return WaitDay