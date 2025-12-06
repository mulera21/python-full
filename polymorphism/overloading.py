#-----------------method overloading-----------------#

class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c
# Example usage
math_ops = MathOperations()
print(math_ops.add(2, 3))        # Output: 5
print(math_ops.add(2, 3, 4))     # Output: 9