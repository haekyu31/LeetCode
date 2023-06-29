class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        """ """
        out = []
        i =0
        while i < (len(S) -1):#iteration for non repeating elements
            j = i
            while j < (len(S) -1) and S[j] == S[j+1]: #iteration for repeating elements
                j += 1
            if (j - i + 1) >= 3: #Checking condition for length 3 or more.  
                out.append([i,j])
            i = j
            i+=1
        return out