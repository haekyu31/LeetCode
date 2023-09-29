class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        A=operations.count("++X")
        B=operations.count("X++")
        C=operations.count("--X") 
        D=operations.count("X--")
		
        return A+B-C-D 