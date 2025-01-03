class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # Split num1 and num2 into real and imaginary parts
        a, b = int(num1[:num1.index("+")]), int(num1[num1.index("+")+1:-1])
        c, d = int(num2[:num2.index("+")]), int(num2[num2.index("+")+1:-1])
        
        # Compute the real and imaginary parts of the product
        real_part = a * c - b * d
        imag_part = a * d + b * c
        
        # Combine the real and imaginary parts to form the result
        result = str(real_part) + "+" + str(imag_part) + "i"
        return result
