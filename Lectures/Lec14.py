# classes and objects, str revisited

class FirstClass:
    attr_one = 11
    attr_two = 'abc'

    def method_one(self):
        return self.attr_one


x = FirstClass()  # Invoking constructor, x is an instance object
print(x)

print(x.attr_one)
x.attr_one += 1
print(x.attr_one)

print(x.method_one())
# Every method has self as a parameter

# Dot operator: function call

############################################
# Str
# __method__ -> dunder method, magic method
# string methods return new objects, strings are immutable, so they can't be changed

x = 'WORD'
y = x.lower()
print(y)




