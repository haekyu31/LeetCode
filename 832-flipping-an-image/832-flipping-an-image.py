class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for Answer in image:
            i,j = 0, len(image)-1
            while i <= j:
                Answer[i], Answer[j] = Answer[j]^1, Answer[i]^1
                i += 1
                j -= 1
        return image