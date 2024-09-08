class vector:
    def __init__(self,x,y,z):
        self.x =x
        self.y =y
        self.z = z

    def __add__(self,other):
        result = vector(self.x+other.x ,self.y+other.y, self.z+other.z)
        return result
        
    def __mul__(self,other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"Vector({self.x}i+ {self.y}i+j+ {self.z}k)"
    #if we want to display the vector in the form of 5i+6j+8k then we can modify the str fun(decorsators)

# Test the implementation
v1 = vector(1, 2, 3)
v2 = vector(4, 5, 6)
v3 = vector(7, 8, 9)  # Same dimension vector

print(v1 + v2)  # Output: Vector(5, 7, 9)
print(v1 * v2)  # Output: 32

print(v1 + v3)  # Output: Vector(8, 10, 12)
print(v1 * v3)  # Output: 50