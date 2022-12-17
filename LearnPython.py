# HELLO WORLD
print("Hello World")

# VARIABLES
# Numbers
a = 3
b = 2

type(a)  # Output: int

# Boolean
a = True
b = False

type(a)  # Output: bool

# Strings
a = " is a sTring "
b = "1"
c = """Hello
World"""
d = "Hello,World"
e = ["a", "a", "a"]
f = ""

type(a)  # Output: str

# Check if a char or some char are in the string
if "a" in a:
    print("Yes")
else:
    print("No")
# Output: "Yes"

# Access at chars of a string
firstChar = a[0]  # Output: " "
secondChar = a[1]  # Output: "i"
lastChar = a[-1]  # Output: " "
fromSecondToSeventhChar = a[1:7]  # Output: "is a s"
fromFirstToSeventhChar = a[:7]  # Output: " is a s"
fromTenthToLastChar = a[9:]  # Output: "ing "
allChars = a[:]  # Output: " is a sTring "

# String Methods
lowerCase = a.lower()  # Output: " is a string "
upperCase = a.upper()  # Output: " IS A STRING "
whitoutSpaceAtStartAndAtTheEnd = a.strip()  # Output: "is a sTring"
everyWordStartWithUpper = a.title()  # Output: " Is A String "
replaceAChar = a.replace("i", "w")  # Output: " ws a sTrwng "
find = a.find("i")  # Output: 1
count = a.count("i")  # Output: 2
a.split(" ")  # Output: [" ", "is", "a", "sTring", " "]
d.split(" ")  # Output: ["Hello,World"]
d.split(",")  # Output: ["Hello", "World"]
f.join(e)  # Output: "aaa"
aIsANumber = a.isnumeric()  # Output: False
bIsANumber = b.isnumeric()  # Output: True
startWith = a.startswith("i")  # Output: False
startWith = a.startswith(" ")  # Output: True
endWith = a.endswith("g")  # Output: False
endWith = a.endswith(" ")  # Output: True
# Variables casting
a = "1"
b = 2

Output = a + b #Output: Error
Output = int(a) + b  # Output: 3

# TEXT FORMATTING
a = "3"
b = 3
c = 3.1234567

print("I have %s cookies" % c) #Output: "I have 3 cookies"
print("I have %d cookies" % b) #Output: "I have 3 cookies"
print("I have %f cookies" % c) #Output: "I have 3.123457 cookies"
print("I have %.2f cookies" % c) #Output: "I have 3.12 cookies"
print("I have", a, "cookies")  # Output: "I have 3 cookies"
print("I have {} cookies".format(a))  # Output: "I have 3 cookies"
print(f"I have {a} cookies")  # Output: "I have 3 cookies"
print("Hello\nHow are you?")  # Output: "Hello
#                                      How are you?"
print("Hello\tHow are you?")  # Output: "Hello    How are you?"
print("Hello")
print("How are you?")  # Output: Hello
#                              How are you?
print("Hello", end=" ")
print("How are you?")  # Output: Hello How are you
print("Hello", end=" | ")
print("How are you?")  # Output: Hello | How are you

# INPUT
a = input("Enter a number: ")  # A take the value entered from the user
input("Press enter to start...")  # The program rest stopped until the user press enter

# OPERATORS
a = 3
b = 2

# Arithmetic operators
addition = a + b  # Output: 5
subtraction = a - b  # Output: 1
multiplication = a * b  # Output: 6
exponentiation = a ** b  # Output: 9
division = a / b  # Output: 1.5
florrDivision = a // b  # Output: 1
modulus = a % b  # Output: 1

# Comparison operators
a = 10

equal = a == 10  # Output: True
notEqual = a != 10  # Output: False
greaterThan = a > 10  # Output: False
greaterThanOrEqualTo = a >= 10  # Output: True
lessThan = a < 10  # Output: False
lessThanOrEqualTo = a <= 10  # Output: True

# Logical operators
a = True
b = False

And = a and b  # Output: False
Or = a or b  # Output: True
Not = not a  # Output: False

# Bitwise operators
a = 10  # (0000 1010 in binary)
b = 4  # (0000 0100 in binary)

bitwiseAnd = a & b  # Output: 0(0000 0000 in binary)
bitwiseOr = a | b  # Output: 14(0000 1110 in binary)
bitwiseNot = ~a  # Output: -11(1111 0101 in binary)
bitwiseXor = a ^ b  # Output: 14(0000 1110 in binary)
bitwiseRightShift = a >> 2  # Output: 2(0000 0010 in binary)
bitwiseLeftShift = a << 2  # Output: 40(0010 1000 in binary)

# Assignment operators
a = 10
b = 4

a &= b  # Equivalent to: a = a & b
a |= b  # Equivalent to: a = a | b
a >>= b  # Equivalent to: a = a >> b
a <<= b  # Equivalent to: a = a << b
a += b  # Equivalent to: a = a + b
a -= b  # Equivalent to: a = a - b
a *= b  # Equivalent to: a = a * b
a **= b  # Equivalent to: a = a ** b
a /= b  # Equivalent to: a = a / b
a //= b  # Equivalent to: a = a // b
a %= b  # Equivalent to: a = a % b

# CONTROL FLOW
# Condition If, Elif, Else
a = 15
b = 10
c = 5

if a > 10:
    print("a is greater than 10")
elif a == 10:
    print("a is equal to 10")
else:
    print("a is less than 10")
# Output: "a is greater than 10"

if b > 10:
    print("b is greater than 10")
elif b == 10:
    print("b is equal to 10")
else:
    print("b is less than 10")
# Output: "a is equal to 10"

if c > 10:
    print("c is greater than 10")
elif c == 10:
    print("c is equal to 10")
else:
    print("c is less than 10")
# Output: "a is less than 10"

# While loop
a = 0

while a <= 5:
    print(a, end=" ")

    a += 1
# Output: 0 1 2 3 4 5

while True:
    print(a, end=" ")
# Output: 6 6 6 6 6 6 6 6 endlessly

# For loop
a = 4

for i in range(a):
    print(i, end=" ")
# Output: 0 1 2 3

# Break and Continue
a = 4

for i in range(a):
    if i == 2:
        break
    else:
        print(i, end="\n")
# Output: 0 1

for i in range(a):
    if i == 2:
        continue
    else:
        print(i, end="\n")
# Output: 0 1 3

# Pass
while True:

# Output: Error
while True:
    pass
# Output:

# Match
a = 3

match a:
    case 1:
        print("Failed")
    case 2:
        print("Sufficent")
    case 3:
        print("Passed")
# Output: "Passed"

# DATA COLLECTIONS
# List
a = [1, 3, 3, 4, 5]
b = ["c", "b", "a", "d"]

type(a)  # Output: list

#Chek if an item is in a list
if 1 in a:
    print("Yes")
else:
    print("No")
#Output: "Yes"

# Access at elements of list
firstElement = a[0]  # Output: [1]
secondElement = a[1]  # Output: [3]
lastElement = a[-1]  # Output: [5]
fromSecondToFourthElement = a[1:4]  # Output: [3, 3, 4]
fromFirstToFourthElement = a[:4]  # Output: [1, 3, 3, 4]
fromSecondToLastElement = a[1:]  # Output: [3, 3, 4, 5]
allElements = a[:]  # Output: [1, 3, 3, 4, 5]
a[0] = 2 #Output: [2, 3, 3, 4, 5]

# List methods
Append = a.append(6)  # Output: [1, 3, 3, 4, 5, 6]
Clear = a.clear()  # Output: []
Index = a.index(1)  # Output: [0]
Insert = a.insert(1, 12)  # Output: [1, 12, 3, 3, 4, 5]
Pop = a.pop(0)  # Output: [3, 3, 4, 5]; pop = 1
Remove = a.remove(1)  # Output: [3, 3, 4, 5]
Reverse = a.reverse()  # Output: [5, 4, 3, 3, 1]
Sorted = b.sorted()  # Output: ["a", "b", "c", "d"] (temporarily)
Sort = b.sort()  # Output: ["a", "b", "c", "d"] (permanently)

# Display list
for num in a:
    print(num, end=" ")
# Output: 1 3 3 4 5

for i in range(len(a)):
    print(a[i], end=" ")
# Output: 1 3 3 4 5

# List comprehensions
a = [1, 2, 3, 4, 5]

b = [x * x for x in a]  # Output: [1, 4, 9, 16, 25]

c = ["Failed" if i <3 else "Passed" for i in a] #Output: ["Failed", "Failed", "Passed", "Passed", "Passed"]

#Tuple
a = (1, 2, 3, 4, 5)
b = ("c", "b", "a", "d")

type(a)  # Output: tuple

#Chek if an item is in a Tuple
if 1 in a:
    print("Yes")
else:
    print("No")
#Output: "Yes"

# Access at elements of tuple
firstElement = a[0]  # Output: [1]
secondElement = a[1]  # Output: [2]
lastElement = a[-1]  # Output: [5]
fromSecondToFourthElement = a[1:4]  # Output: [2, 3, 4]
fromFirstToFourthElement = a[:4]  # Output: [1, 2, 3, 4]
fromSecondToLastElement = a[1:]  # Output: [2, 3, 4, 5]
allElements = a[:]  # Output: [1, 2, 3, 4, 5]
a[0] = 2 #Output: Error

# Tuple methods
Count = a.count(1)  # Output: 1
Index = a.index(1)  # Output: 0

# Display tuple
for num in a:
    print(num, end=" ")
# Output: 1 2 3 4 5

for i in range(len(a)):
    print(a[i], end=" ")
# Output: 1 2 3 4 5

# Tuple comprehensions
a = (1, 2, 3, 4, 5)

b = (x * x for x in a)  # Output: (1, 4, 9, 16, 25)

c = ("Failed" if i <3 else "Passed" for i in a) #Output: ("Failed", "Failed", "Passed", "Passed", "Passed")

#Dictionary
a = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

type(a)  # Output: dict

#Chek if an item is in a Dictionary
if "a" in a:
    print("Yes")
else:
    print("No")
#Output: "Yes"

# Access at elements of Dictionary
one = a["a"]  # Output: [1]
two = a["b"]  # Output: [2]
a["f"] = 6 #Output: {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}

# Dictionary methods
Clear = a.clear()  # Output: {}
Copy = a.copy()  # Output: {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
Fromkeys = a.fromkeys("a", 1)  # Output: {"a": 1}
Get = a.get("a")  # Output: 1
Items = a.items()  # Output: dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
Keys = a.keys()  # Output: dict_keys(['a', 'b', 'c', 'd', 'e'])
Pop = a.pop("a")  # Output: 1; {"b": 2, "c": 3, "d": 4, "e": 5}
Popitem = a.popitem()  # Output: ("e", 5); {"b": 2, "c": 3, "d": 4}
Setdefault = a.setdefault("a", 1)  # Output: 1
Update = a.update({"f": 6})  # Output: {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
Values = a.values()  # Output: dict_values([1, 2, 3, 4, 5])

# Display Dictionary
for num in a:
    print(num, end=" ")
# Output: a b c d e

for num in a.values():
    print(num, end=" ")
# Output: 1 2 3 4 5

for num in a.items():
    print(num, end=" ")
# Output: ('a', 1) ('b', 2) ('c', 3) ('d', 4) ('e', 5)

for key, value in a.items():
    print(key, value, end=" ")
# Output: a 1 b 2 c 3 d 4 e 5

# Dictionary comprehensions
a = {num: num * num for num in range(1, 6)}  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#Set
a = {1, 2, 3, 4, 5}

type(a)  # Output: set

#Chek if an item is in a Set
if 1 in a:
    print("Yes")
else:
    print("No")
#Output: "Yes"

# Access at elements of Set
one = a[0]  # Output: Error
two = a[1]  # Output: Error
a.add(6) #Output: {1, 2, 3, 4, 5, 6}

# Set methods
Add = a.add(6)  # Output: {1, 2, 3, 4, 5, 6}
Clear = a.clear()  # Output: {}
Copy = a.copy()  # Output: {1, 2, 3, 4, 5}
Difference = a.difference({1, 2, 3})  # Output: {4, 5}
Difference_update = a.difference_update({1, 2, 3})  # Output: {4, 5}
Discard = a.discard(1)  # Output: {2, 3, 4, 5}
Intersection = a.intersection({1, 2, 3})  # Output: {1, 2, 3}
Intersection_update = a.intersection_update({1, 2, 3})  # Output: {1, 2, 3}
Isdisjoint = a.isdisjoint({1, 2, 3})  # Output: False
Isequal = a.isequal({1, 2, 3})  # Output: False
Issubset = a.issubset({1, 2, 3})  # Output: False
Issuperset = a.issuperset({1, 2, 3})  # Output: False
Pop = a.pop()  # Output: 1; {2, 3, 4, 5}
Remove = a.remove(1)  # Output: {2, 3, 4, 5}
Symmetric_difference = a.symmetric_difference({1, 2, 3})  # Output: {1, 2, 3, 4, 5}
Symmetric_difference_update = a.symmetric_difference_update({1, 2, 3})  # Output: {1, 2, 3, 4, 5}
Union = a.union({1, 2, 3})  # Output: {1, 2, 3, 4, 5}
Update = a.update({1, 2, 3})  # Output: {1, 2, 3, 4, 5}

# Display Set
for num in a:
    print(num, end=" ")
# Output: 1 2 3 4 5

#COLLECTIONS
#Counter
from collections import Counter

a = "aaaaaaabbbbbbccc"
b = Counter(a) #Output: ({"a": 7, "b": 6, "c": 3})
c = b.most_common(1) #Output: ("a", 5)
c = b.most_common(2) #Output: [("a", 7), ("b", 6)]

#Namedtuple
from collections import namedtuple

a = namedtuple("a", "x,y")

b = a(3, 4) #Output: (x=3, y=4)
x = b.x #Output: 3

#OrderedDict
from collections import OrderedDict

a = OrderedDict()

a["a"] = 1
a["b"] = 2
a["c"] = 3
a["d"] = 4
a #Output: ([("a", 1), ("b", 2), ("c", 3), ("d", 4)])

#Defaultdict
from collections import defaultdict

a = defaultdict(int)

a["a"] = 1
a["b"] = 2
a["c"] #Output: 0

a = defaultdict(float)

a["a"] = 1
a["b"] = 2
a["c"] #Output: 0.0

#Deque
from collections import deque

a = deque()

append = a.append(1) #Output: ([1])
append = a.append(2) #Output: ([1, 2])
appendLeft = a.appendleft(3) #Output: ([3, 1, 2])
pop = a.pop() #Output: ([3, 1])
popLeft = a.popleft() #Output: ([1])
extend = a.extend([2, 3, 4]) #Output: ([1, 2, 3, 4])
extendLeft = a.extendleft([2, 3, 4]) #Output: ([4, 3, 2, 1, 2, 3, 4])
rotateOne = a.rotate(1) #Output: [(4, 4, 3, 2, 1, 2, 3)]
rotateTwo = a.rotate(2) #Output: [(2, 3, 4, 4, 3, 2, 1)]
rotateMinesOne = a.rotate(-1) #Output: [(3, 4, 4, 3, 2, 1, 2)]
clear = a.clear() #Output: ([])

#Functions
def function(a):
    print(a)
function(9) #Output: 9
function(9) + 1 #Output: Error

def function(a):
    return(a)
function(9) #Output:
print(function(9)) #Output: 9
print(function(9) + 1) #Output: 10
print(function(9, 10)) #Output: Error

def function(*a):
    return(a)
print(function(9)) #Output: (9,)
print(function(8, 5)) #Output: (8, 5)

def function(**a):
    return(a)
print(function(name = "Harry", surname = "Potter", age = 11)) #Output: {"name": "Harry", "surname": "Potter", "age": 11}
print(function(name = "Harry", surname = "Potter")) #Output: {"name": "Harry", "surname": "Potter"}

#Lambda Function
a = lambda a: a + 2
print(a(2)) #Output: 4

#Map
a = [1, 2, 3, 4, 5]

b = list(map(lambda n: n**2, a)) #Output: [1, 4, 9, 16, 25]

#Filter
a = ["a", "b", "cc", "dddd", "aaa", "b"]

b = list(filter(lambda x: x.startswith("a"), a)) #Output: ["a", "aaa"]

#Class
class person:
    def __init__(self, name, surname):
        self.name = name 
        self.surname = surname
Harry = person("Harry", "Potter")
print(Harry.name) #Output: "Harry"
print(Harry.surname) #Output: "Potter"

class person:
    def __init__(self, name, surname):
        self.name = name 
        self.surname = surname

    def SayHello(self):
        print(f"Hello I'm {self.name}")
Harry = person("Harry", "Potter")
Harry.SayHello() #Output: "Hello I'm Harry"

#Inheterance
class Vechicle:
    def general_usage(self):
        print("General use: transportation")

class Car(Vechicle):
    def __init__(self):
        print("I'm car")

        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("Specific use: commute to work")


class MotorCycle(Vechicle):
    def __init__(self):
        print("I'm motor cycle")

        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print("Specific use: road trip")

car = Car() #Output: "I'm car"
motorCycle = MotorCycle() #Output: "I'm motor cycle"

car.general_usage() #Output: "General use: transportation"
car.specific_usage() #Output: "Specific use: commute to work"
motorCycle.general_usage() #Output: "General use: transportation"
motorCycle.specific_usage() #Output: "Specific use: road trip"

#Multiple inheritance
class Father():
    def gardening(self):
        print("I enjoy gardening")

class Mother():
    def cooking(self):
        print("I love cooking")

class Child(Father, Mother):
    def sports(self):
        print("I enjoy sports")

child = Child()

child.gardening() #Output: "I enjoy gardening"
child.cooking() #Output: "I love cooking"
child.sports() #Output: "I enjoy sports"

#Exception Handling
try:
    print(3 / 0)
except ZeroDivisionError:
    print("You can't divide by zero")
finally:
    print("Stop")
#Output: "You can't divide by zero"
#        "Stop"

try:
    print(3 / 1)
except ZeroDivisionError:
    print("You can't divide by zero")
finally:
    print("Stop")
#Output: 3.0
#       "Stop"

#Iterator
a = 10
r = range(a)
i = iter(r)

while True:
    try:
        print(next(i), end=" ")
    except StopIteration:
        print("STOP")
        break
#Output: 0 1 2 3 4 5 6 7 8 9 "STOP"

#Generator
def function(a):
    while a <= 15:
        yield a

        a += 1

nums = function(10)

while True:
    try:
        print(next(nums), end=" ")
    except StopIteration:
        print("STOP")
        break
#Output: 10 11 12 13 14 15 "STOP"

#Decorators
#Functions decorators
def start_end_decorator(func):
    def wrapper():
        print("Start", end=" ")
        func()
        print("End")
    
    return wrapper

def function():
    print("Hello World", end=" ")

a = start_end_decorator(function)

function() #Output: "Hello World"
a() #Output: "Start Hello World End"

def start_end_decorator(func):
    def wrapper():
        print("Start", end=" ")
        func()
        print("End")
    
    return wrapper

@start_end_decorator
def function():
    print("Hello World", end=" ")

function() #Output: "Start Hello World End"

def start_end_decorator(func):
    def wrapper():
        print("Start", end=" ")
        func()
        print("End")
    
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

add5(5) #Output: Error

def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start", end=" ")
        result = func(*args, **kwargs)
        print("End", end=" ")

        return result
    
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

print(add5(5)) #Output: "Start End 10"

#Class decorators
class caps_lock:

    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs).upper()

@caps_lock
def message(msg):
    return msg

print(message("Hello World")) #Output: "HELLO WORLD"