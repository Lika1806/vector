import math
from typing import Any, Union

class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


    def __neg__(self)-> None:
        '''returns new Vector object with negated coordinates'''
        return Vector(-self.x, -self.y)

    def __abs__(self) -> None:
        '''returns new Vector object whith the same length and positive coordinates'''
        return Vector(abs(self.x), abs(self.y))

    def __pos__(self) -> None:
        '''returns new Vector object with the same coordinates'''
        return Vector(self.x, self.y)        

    def __eq__(self, other: Any) -> bool:
        '''returns true if vectors are equal'''
        try:
            angle1 = self.x/self.y
        except ZeroDivisionError:
            angle1 = 0
        try:
            angle2 = other.x/other.y
        except ZeroDivisionError:
            angle2 = 0
        if isinstance(other, Vector):
            return self.length()==other.length() and angle1 == angle2
        if isinstance(other, (int,float)):
            return self.length() == other
        return NotImplemented
    
    def __lt__(self, other: Any) -> bool:
        '''returns true if length of fisrt is lower then length of second'''
        if isinstance(other, Vector):
            return self.length()<other.length()
        return NotImplemented
    
    def __le__(self, other: Any) -> bool:
        '''returns True if vectors are equal or length of fisrt is lower then length of second'''
        return self == other or self < other

    def __repr__(self)->str:
        '''returns a string representation of Vector object'''
        return f"({self.x}, {self.y})"
    
    def __add__(self, other: Any) -> 'Vector':
        '''returns an addition of given two Vectors'''
        if isinstance(other, Vector):
            return Vector(self.x+other.x, self.y+other.y)
        return NotImplemented
    


    def __sub__ (self, other: Any)-> 'Vector':
        '''returns a substruction of given two Vectors'''        
        return self + (-other)
        

    def __mul__(self, other: Any):
        '''In case of two Vector objects returns scalar multiplication, 
        in case of Vector object and number retruns Vector with coordinates multiplied with a given number'''
        if isinstance(other, (int, float)):
            return Vector(self.x*other, self.y*other)
        if isinstance(other, Vector):
            return self.x * other.y - other.x - self.y
        return NotImplemented
    
    def __rmul__(self, other: Any):
        return self*other

    def __truediv__(self, other: Union[int,float]) -> 'Vector':
        '''returns Vector with coordinates divided my given number'''
        if isinstance(other, (int, float)):
            return Vector(self.x/other, self.y/other)
        return NotImplemented

    def __floordiv__(self, other: Union[int,float]) -> 'Vector':
        '''returns Vector with coordinates floor-divided my given number'''        
        if isinstance(other, (int, float)):
            return Vector(self.x//other, self.y//other)
        return NotImplemented
        

    def __mod__(self, other: Union[int, float])-> 'Vector':
        '''returns a new Vector with coordinates modulo the given number.'''
        if isinstance(other, (int, float)):
            return self - self//other * other
        return NotImplemented

    def length(self):
        '''returns the length of a given vector'''
        return math.sqrt((self.x**2+self.y**2))


if __name__ == '__main__':
    vector1 = Vector(1,2)
    vector2 = Vector(3,4)

    print(vector1)
    print(vector2)
    vector2-=vector1
    print(vector2)
    vector2*=2
    vector1+=vector2
    print(vector2)