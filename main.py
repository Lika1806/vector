import vector

def test(expression):
    print(f"{expression} --> {eval(expression)}")
if __name__=="__main__":
    vector1 = vector.Vector(-1,2)
    vector2 = vector.Vector(6,7)
    test('-vector1')
    test('+vector1')
    test("abs(vector1)")
    test("vector1+vector2")
    test("vector1-vector2")
    test("vector1*vector2")
    test("vector1*3")
    test("3*vector1")
    test("vector2/3")
    test("vector2//3")
    test("vector2%3")
    test('vector1==vector2')
    test('vector1>vector2')
    test('vector1<=vector2')