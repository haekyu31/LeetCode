class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = []
        for i in range(rowIndex+1):
            row = [0 for _ in range(i+1)]
            row[0] = 1
            row[-1] = 1
            
            for j in range(1, len(row)-1):
                row[j] = arr[i-1][j-1] + arr[i-1][j]
            arr.append(row)
        # print(arr)
        return arr[rowIndex]