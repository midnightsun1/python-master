def make_quiz(q, opts, ans):
    return {"question": q, "options": opts, "answer": ans}

curriculum = {
    "🌱 Beginner": [
        {
            "title": "1. Python Kya Hai?",
            "theory": """Python aik programming language hai jo parhne aur likhne mein bohat asaan hai. Google, YouTube, Instagram jaisi bari companies Python use karti hain. Aap Python se websites, games, apps, AI, aur data science ka kaam kar sakte ho.""",
            "example": """# Pehla program
print("Assalam-o-Alaikum Python!")
print("Main seekh raha hun Python!")""",
            "task": "Apna naam, umar, aur shahar 3 alag print statements mein likho.",
            "tip": "💡 Tip: `print()` screen par kuch bhi dikhane ke liye hota hai.",
            "quiz": make_quiz("`print()` kya karta hai?", ["Delete karta hai", "Screen par likhta hai", "File banata hai"], "Screen par likhta hai")
        },
        {
            "title": "2. Variables (Data Store Karna)",
            "theory": """Variable aik naam ka dabba hai jismein aap data rakh sakte ho. Baad mein us naam se data use kar sakte ho. Variables ko samajhna programming ka sab se zaroori hissa hai.""",
            "example": """# Variables
naam = "Ahmed"
umar = 20
qad = 5.9

print(naam)
print(umar)
print(qad)""",
            "task": "5 variables banao: naam, umar, shehar, phone, email — sab print karo.",
            "tip": "💡 Tip: Variable ka naam number se shuru nahi ho sakta.",
            "quiz": make_quiz("Variable mein kya hota hai?", ["Code", "Data", "Error"], "Data")
        },
        {
            "title": "3. Data Types (Data Ki Qisamain)",
            "theory": """Har data ki apni qisam hoti hai: `str` text ke liye, `int` pooray number ke liye, `float` decimal number ke liye, `bool` True/False ke liye, `list` bohat si cheezon ke liye.""",
            "example": """# Data types
naam = "Sara"
umar = 22
qad = 5.4
student = True

print(type(naam))   # <class 'str'>
print(type(umar))   # <class 'int'>
print(type(qad))    # <class 'float'>
print(type(student))""",
            "task": "Khud ke 4 variables banao aur `type()` se unki types check karo.",
            "tip": "💡 Tip: `type()` function batata hai ke variable kis qisam ka hai.",
            "quiz": make_quiz("Text data kis type ka hota hai?", ["int", "str", "float"], "str")
        },
        {
            "title": "4. Strings Aur String Methods",
            "theory": """String matlab text. Python mein strings ke bohat se built-in methods hain jaise upper(), lower(), replace(), len(), split().""",
            "example": """# String methods
name = "  python Seekho  "
print(name.upper())
print(name.lower())
print(name.strip())
print(len(name))
print(name.replace("python", "Coding"))""",
            "task": "Aik sentence lo aur usay upper case, lower case, aur word count karke print karo.",
            "tip": "💡 Tip: `len()` kisi bhi cheez ki length batata hai — string, list, dictionary sab ki.",
            "quiz": make_quiz("String ko baray haroof mein karne ke liye kya use hota hai?", ["lower()", "upper()", "title()"], "upper()")
        },
        {
            "title": "5. Numbers & Math Operators",
            "theory": """Python mein +, -, *, /, //, %, ** operators use hote hain. `//` floor division hai, `%` remainder deta hai, `**` power.""",
            "example": """# Math
a = 17
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  # 3
print(a % b)   # 2
print(a ** b)  # 17 ki power 5""",
            "task": "User se 2 numbers lo aur unka sum, difference, product, aur division print karo.",
            "tip": "💡 Tip: `/` hamesha float answer deta hai, `//` integer answer deta hai.",
            "quiz": make_quiz("`%` operator kya deta hai?", ["Power", "Remainder", "Division"], "Remainder")
        },
        {
            "title": "6. User Se Input Lena",
            "theory": """`input()` se aap user se keyboard ke zariye data le sakte ho. Input hamesha string hota hai. Agar number chahiye to `int()` ya `float()` se convert karo.""",
            "example": """# Input
naam = input("Apna naam likho: ")
print("Assalam-o-Alaikum,", naam)""",
            "example_inputs": "Ali",
            "task": "User se naam aur umar lo. Phir print karo: 'Aap ka naam ___ hai aur umar ___ hai.'",
            "tip": "💡 Tip: `int(input())` se string number mein convert hoti hai.",
            "quiz": make_quiz("By default `input()` kis type ka data deta hai?", ["int", "float", "str"], "str")
        },
        {
            "title": "7. Type Conversion (Casting)",
            "theory": """Kabhi kabhi aik type ko dosri type mein badalna parta hai. Jaise input se mila number string hota hai, usay int/float mein convert karna parta hai.""",
            "example": """# Type casting
s = "25"
n = int(s)
f = float(s)
print(n + 5)
print(type(f))""",
            "task": "String '100.5' ko float mein convert karo aur us mein 10 jama karo.",
            "tip": "💡 Tip: Agar conversion mumkin na ho to error aata hai.",
            "quiz": make_quiz("String ko number mein convert karne ke liye kya use hota hai?", ["str()", "int()", "text()"], "int()")
        },
        {
            "title": "8. Comparison Operators",
            "theory": """Comparison operators se do cheezon ko compare karte hain: `==` equal, `!=` not equal, `>` greater than, `<` less than, `>=`, `<=`. Jawab True ya False hota hai.""",
            "example": """# Compare
x = 10
y = 20

print(x == y)
print(x != y)
print(x > y)
print(x < y)""",
            "task": "2 numbers compare karo aur batain ke kaunsa bara hai ya barabar hai.",
            "tip": "💡 Tip: `=` value assign karta hai, `==` compare karta hai. Dono alag hain!",
            "quiz": make_quiz("`!=` ka matlab kya hai?", ["Barabar hai", "Barabar nahi hai", "Bara hai"], "Barabar nahi hai")
        },
        {
            "title": "9. Logical Operators (and, or, not)",
            "theory": """Logical operators se aik se zyada conditions jod sakte ho. `and` dono true honay par true, `or` koi aik true honay par true, `not` ulta jawab deta hai.""",
            "example": """# Logical operators
umar = 20
pass_hai = True

if umar >= 18 and pass_hai:
    print("License mil sakta hai")
else:
    print("License nahi milega")""",
            "task": "Check karo ke user ka number 10 se bada hai YA 5 ke barabar hai.",
            "tip": "💡 Tip: `and` dono conditions ko poora karta hai, `or` koi aik bhi.",
            "quiz": make_quiz("`and` kab true hota hai?", ["Dono true hon", "Aik true ho", "Dono false hon"], "Dono true hon")
        },
        {
            "title": "10. if-elif-else (Faisle Karna)",
            "theory": """Program faisla kar sakta hai using conditions. `if` pehli shart, `elif` aur shart, `else` jab koi shart na chale.""",
            "example": """# Grade check
marks = int(input("Marks dalo: "))

if marks >= 90:
    print("A+ Grade")
elif marks >= 80:
    print("A Grade")
elif marks >= 70:
    print("B Grade")
else:
    print("Aur mehnat karo")""",
            "example_inputs": "85",
            "task": "User se temperature lo aur batain: <0 thanda, 0-30 normal, >30 garam.",
            "tip": "💡 Tip: Python mein indentation (spaces) zaroori hai. Condition ke andar wala code 4 spaces andar likho.",
            "quiz": make_quiz("Jab `if` false ho aur koi aur condition check karni ho tab kya use karte hain?", ["else", "elif", "while"], "elif")
        },
        {
            "title": "11. Comments & Indentation",
            "theory": """Comments aise lines hain jo run nahi hoti, sirf samajhne ke liye hoti hain. `#` se shuru hotay hain. Indentation Python ki syntax ka hissa hai.""",
            "example": """# Yeh comment hai
x = 5  # yeh bhi comment hai

if x > 0:
    # yeh condition ke andar hai
    print("Positive number")""",
            "task": "Aik program likho jismein har line par comment ho ke yeh kya kar raha hai.",
            "tip": "💡 Tip: Ache comments aapke code ko dusron ke liye asaan banate hain.",
            "quiz": make_quiz("Comment kaisay likha jata hai?", ["// comment", "# comment", "/* comment */"], "# comment")
        },
        {
            "title": "12. Beginner Mini Project: Calculator",
            "theory": """Ab hum sab kuch mila kar aik chhota calculator banate hain. Is mein input, variables, operators, aur conditions sab use hongay.""",
            "example": """# Simple calculator
n1 = float(input("Pehla number: "))
op = input("Operator (+, -, *, /): ")
n2 = float(input("Dosra number: "))

if op == "+":
    print("Jawab:", n1 + n2)
elif op == "-":
    print("Jawab:", n1 - n2)
elif op == "*":
    print("Jawab:", n1 * n2)
elif op == "/":
    if n2 == 0:
        print("Zero se divide nahi kar sakte")
    else:
        print("Jawab:", n1 / n2)
else:
    print("Ghalat operator")""",
            "example_inputs": "10\n*\n5",
            "task": "Is calculator mein power operator `**` bhi add karo.",
            "tip": "💡 Tip: Chota project banane se confidence barhta hai. Har topic ke baad chhota project zaroor banaya karo.",
            "quiz": make_quiz("Project practice kyun zaroori hai?", ["Concepts mazboot hote hain", "Sirf time pass", "Kuch nahi seekhne milta"], "Concepts mazboot hote hain")
        }
    ],

    "🚀 Intermediate": [
        {
            "title": "13. For Loops",
            "theory": """For loop jab chalata hai jab aapko pata ho ke kaam kitni dafa karna hai. `range()` numbers ki series banata hai.""",
            "example": """# For loop
for i in range(5):
    print("Dafa number:", i)

# 1 se 10 tak
for i in range(1, 11):
    print(i)""",
            "task": "1 se lekar 20 tak sirf even numbers print karo using for loop.",
            "tip": "💡 Tip: `range(start, stop, step)` — step 2 rakhne se har dosra number milta hai.",
            "quiz": make_quiz("`range(5)` kya produce karta hai?", ["1-5", "0-4", "0-5"], "0-4")
        },
        {
            "title": "14. While Loops",
            "theory": """While loop jab tak chalta hai jab tak condition true ho. Jab pata na ho ke kitni dafa chalna, tab while loop best hai.""",
            "example": """# While loop
count = 1
while count <= 5:
    print(count)
    count += 1  # 1 barhana""",
            "task": "User se password mango jab tak 'python123' na de. Phir welcome kaho.",
            "example_inputs": "wrong\npython123",
            "tip": "💡 Tip: `count += 1` ka matlab `count = count + 1` hai.",
            "quiz": make_quiz("While loop kab use hota hai?", ["Pata ho kitni dafa chalna", "Pata na ho kitni dafa chalna", "Sirf aik dafa"], "Pata na ho kitni dafa chalna")
        },
        {
            "title": "15. break, continue, pass",
            "theory": """`break` loop rok deta ha, `continue` agli iteration par chala jata hai, `pass` kuch nahi karta — sirf jagah bharta hai.""",
            "example": """# break example
for i in range(10):
    if i == 5:
        break
    print(i)

print("---")

# continue example
for i in range(5):
    if i == 2:
        continue
    print(i)""",
            "task": "1 se 100 tak loop chalao, jab 50 aaye to loop rok do.",
            "tip": "💡 Tip: `break` loop se bahar nikal jata hai, `continue` sirf usi dafa ko skip karta hai.",
            "quiz": make_quiz("`break` kya karta hai?", ["Loop rok de", "Loop continue kare", "Error de"], "Loop rok de")
        },
        {
            "title": "16. Lists (Part 1)",
            "theory": """List aik jagah par bohat si cheezain rakhne ka tareeqa hai. Order rehti hai, duplicate allowed hai, aur change ho sakti hai (mutable).""",
            "example": """# List
fruits = ["saib", "kela", "angoor"]
print(fruits[0])       # pehli cheez
print(fruits[-1])      # aakhri cheez
fruits[1] = "santra"   # change karna
fruits.append("anar")  # add karna
print(fruits)""",
            "task": "5 subjects ki list banao, pehla aur aakhra subject print karo, phir aik subject badlo.",
            "tip": "💡 Tip: List ka index 0 se shuru hota hai. Pehli cheez [0], aakhri [-1].",
            "quiz": make_quiz("List ka pehla index kya hota hai?", ["1", "0", "-1"], "0")
        },
        {
            "title": "17. Lists (Part 2) - Methods",
            "theory": """Python lists ke bohat se built-in methods hain: append, insert, remove, pop, sort, reverse, index, count, copy, clear.""",
            "example": """# List methods
numbers = [3, 1, 4, 1, 5]
numbers.append(9)
numbers.sort()
numbers.reverse()
numbers.remove(1)
print(numbers)

print(numbers.count(4))""",
            "task": "Aik number list lo, usay sort karo, reverse karo, aur maximum/minimum value print karo.",
            "tip": "💡 Tip: `max(list)` aur `min(list)` se sab se bara/chhota number milta hai.",
            "quiz": make_quiz("List ke end mein item add karne ke liye kya use hota hai?", ["insert()", "append()", "add()"], "append()")
        },
        {
            "title": "18. Slicing Lists",
            "theory": """Slicing se list ka hissa nikal sakte ho. `list[start:stop:step]` is tarah kaam karta hai.""",
            "example": """# Slicing
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:6])    # index 2 se 5 tak
print(nums[:5])     # shuru se 4 tak
print(nums[5:])     # 5 se end tak
print(nums[::2])    # har dosra number
print(nums[::-1])   # ulta order""",
            "task": "Aik list banao aur us ka reverse print karo bina `reverse()` method ke.",
            "tip": "💡 Tip: `[::-1]` se kisi bhi list/string ka ulta version milta hai.",
            "quiz": make_quiz("List reverse karne ka shortcut kya hai?", ["[::-1]", "[::1]", "[1::-1]"], "[::-1]")
        },
        {
            "title": "19. Tuples & Sets",
            "theory": """Tuple list jaisi hai lekin change nahi hoti (immutable). Set mein duplicate items nahi hote aur order fixed nahi rehta.""",
            "example": """# Tuple
t = (1, 2, 3)
print(t[0])

# Set
s = {1, 2, 2, 3, 3, 3}
print(s)

s.add(4)
print(s)""",
            "task": "Aik tuple banao apni info ka (naam, umar, shehar) aur set banao unique numbers ka.",
            "tip": "💡 Tip: Jab data change nahi karna ho to tuple use karo. Unique items ke liye set use karo.",
            "quiz": make_quiz("Kis mein duplicate values allowed nahi hain?", ["List", "Tuple", "Set"], "Set")
        },
        {
            "title": "20. Dictionaries (Key-Value)",
            "theory": """Dictionary mein data key-value pair mein store hota hai. Jaise dictionary mein lafz aur uska matlab hota hai. Access `.get()` se bhi kar sakte hain.""",
            "example": """# Dictionary
student = {
    "naam": "Hassan",
    "umar": 21,
    "sheher": "Karachi"
}

print(student["naam"])
print(student.get("umar"))
student["grade"] = "A+"
print(student)""",
            "task": "Aik dictionary banao apne favourite phone ki details ke saath: brand, model, price, color.",
            "tip": "💡 Tip: `.get()` use karo agar key missing ho to error nahi aata, `None` milta hai.",
            "quiz": make_quiz("Dictionary mein data kis form mein hota hai?", ["Key-value pair", "Sirf values", "Sirf keys"], "Key-value pair")
        },
        {
            "title": "21. Looping on Lists & Dictionaries",
            "theory": """Aap lists aur dictionaries par loop chala sakte ho. List ke items par directly, dictionary ke keys/values dono par.""",
            "example": """# Loop on list
fruits = ["saib", "kela", "anar"]
for fruit in fruits:
    print(fruit)

# Loop on dictionary
student = {"naam": "Ali", "umar": 20}
for key, value in student.items():
    print(key, ":", value)""",
            "task": "Aik shopping list banao aur har item print karo. Phir har item ki length bhi print karo.",
            "tip": "💡 Tip: `.items()` dictionary ke key-value pairs deta hai.",
            "quiz": make_quiz("Dictionary ke items loop karne ke liye kaunsa method use hota hai?", ["values()", "items()", "keys()"], "items()")
        },
        {
            "title": "22. Functions",
            "theory": """Function aik block of code hai jo aik kaam karta hai. `def` se define hota hai. Baar baar use kar sakte ho. Clean code ke liye bohat zaroori hain.""",
            "example": """# Function
def salam_karo(naam):
    return "Assalam-o-Alaikum, " + naam

print(salam_karo("Ayesha"))
print(salam_karo("Bilal"))""",
            "task": "Aik function banao jo 2 numbers jama kare aur result return kare.",
            "tip": "💡 Tip: Function ko define karna alag hai, call karna alag. Dono zaroori hain.",
            "quiz": make_quiz("Function define karne ke liye keyword kya hai?", ["def", "fun", "function"], "def")
        },
        {
            "title": "23. Function Arguments",
            "theory": """Functions mein arguments pass kar sakte ho: default values, *args (kitne bhi values), **kwargs (kitne bhi named values).""",
            "example": """# Arguments
def greet(name, msg="Kaise hain?"):
    print(name, msg)

greet("Ali")
greet("Sara", "Aap ka din acha ho!")

# *args
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))""",
            "task": "Aik function banao jo kitne bhi numbers dey, unka average return kare.",
            "tip": "💡 Tip: `sum(list)` list ke sab numbers jama karta hai.",
            "quiz": make_quiz("Zyada arguments ke liye kya use hota hai?", ["*args", "**kwargs", "*values"], "*args")
        },
        {
            "title": "24. Lambda Functions",
            "theory": """Lambda aik chhota anonymous function hai. Aik line mein kaam karta hai. Zyada tar sort/filter/map ke saath use hota hai.""",
            "example": """# Lambda
square = lambda x: x * x
print(square(5))

nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)""",
            "task": "Lambda use karke aik list ke sab numbers ko double karo.",
            "tip": "💡 Tip: Lambda chhota kaam ke liye best hai. Bare functions ke liye `def` use karo.",
            "quiz": make_quiz("Lambda function kya hai?", ["Bara function", "Chhota anonymous function", "Class"], "Chhota anonymous function")
        },
        {
            "title": "25. File Handling",
            "theory": """Python files read/write kar sakti hai. `with` use karne se file apne aap band ho jati hai. Modes: 'r' read, 'w' write, 'a' append.""",
            "example": """# File write
with open("meri_file.txt", "w") as f:
    f.write("Yeh meri pehli file hai!")

# File read
with open("meri_file.txt", "r") as f:
    print(f.read())""",
            "task": "User se aik line lo aur usay 'notes.txt' file mein save karo, phir dobara parh kar print karo.",
            "example_inputs": "Yeh meri note hai",
            "tip": "💡 Tip: `with` hamesha use karo taake file close na karni pade.",
            "quiz": make_quiz("File append karne ke liye kaunsa mode hota hai?", ["w", "a", "r"], "a")
        },
        {
            "title": "26. Working with CSV Files",
            "theory": """CSV (Comma Separated Values) Excel jaisi files hain. Python `csv` module se inko parh aur likh sakti hai. Data science mein bohat use hoti hain.""",
            "example": """import csv

# CSV write
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Naam", "Umar", "Grade"])
    writer.writerow(["Ali", 20, "A"])
    writer.writerow(["Sara", 22, "A+"])

# CSV read
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)""",
            "task": "Aik CSV file banao apne dostoon ke naam aur phone numbers ke saath.",
            "tip": "💡 Tip: CSV files Excel mein easily khulti hain aur bohat common format hai.",
            "quiz": make_quiz("CSV ka matlab kya hai?", ["Comma Separated Values", "Common System Values", "Code Script Values"], "Comma Separated Values")
        }
    ],

    "🔥 Advanced": [
        {
            "title": "27. List & Dictionary Comprehension",
            "theory": """Comprehension se aap chhote code mein lists/dictionaries bana sakte ho. Yeh loops ka mukhtasar tareeqa hai.""",
            "example": """# List comprehension
nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums]
evens = [x for x in nums if x % 2 == 0]

print(squares)
print(evens)

# Dict comprehension
squares_dict = {x: x**2 for x in nums}
print(squares_dict)""",
            "task": "1 se 20 tak numbers ki list banao aur unke cubes ki list comprehension se banao.",
            "tip": "💡 Tip: Comprehension readable honi chahiye. Bohat complicated banane se avoid karo.",
            "quiz": make_quiz("List comprehension kis liye hoti hai?", ["Code chhota karne ke liye", "Error dene ke liye", "File delete karne ke liye"], "Code chhota karne ke liye")
        },
        {
            "title": "28. Error Handling (try-except)",
            "theory": """Program mein galtiyan hoti hain. `try-except` se error handle kar sakte hain taake program crash na ho. `finally` hamesha chalta hai.""",
            "example": """# Error handling
try:
    num = int(input("Number dalo: "))
    print("Aap ne number diya:", num)
except ValueError:
    print("Bhai, number dena tha!")
finally:
    print("Program khatam.")""",
            "example_inputs": "abc",
            "task": "User se 2 numbers lo aur divide karo. Agar zero se divide ho toh special message do.",
            "tip": "💡 Tip: `ZeroDivisionError` tab aata hai jab 0 se divide karo.",
            "quiz": make_quiz("Risky code kis block mein rakhte hain?", ["except", "try", "finally"], "try")
        },
        {
            "title": "29. Iterators & Generators",
            "theory": """Iterator ek object hai jisse aap values ek ek kar ke nikal sakte ho. Generator functions `yield` use karti hain aur memory bachati hain.""",
            "example": """# Generator
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)""",
            "task": "Aik generator banao jo 1 se n tak even numbers yield kare.",
            "tip": "💡 Tip: `yield` return jaisa hai lekin function ka state save rehta hai.",
            "quiz": make_quiz("Generator mein kaunsa keyword use hota hai?", ["return", "yield", "break"], "yield")
        },
        {
            "title": "30. Decorators",
            "theory": """Decorator aik function hai jo dosre function ko modify kar sakta hai. Logging, authentication, aur caching mein use hota hai.""",
            "example": """# Decorator
def my_decorator(func):
    def wrapper():
        print("Function shuru hone se pehle")
        func()
        print("Function khatam hone ke baad")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()""",
            "task": "Aik decorator banao jo kisi bhi function ke run hone ka time print kare.",
            "tip": "💡 Tip: `@decorator` syntax function ke upar likhte hain.",
            "quiz": make_quiz("Decorator kya hota hai?", ["Function jo function modify kare", "Variable type", "Loop"], "Function jo function modify kare")
        },
        {
            "title": "31. Object Oriented Programming (OOP)",
            "theory": """OOP mein hum real world cheezon ko code mein model karte hain. `class` blueprint hai, `object` uski actual cheez. Attributes (data) aur methods (functions) hote hain.""",
            "example": """# OOP
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def start(self):
        print(self.name + " engine started!")

my_car = Car("Toyota", "Black")
print(my_car.color)
my_car.start()""",
            "task": "Aik `Student` class banao jismein naam, umar, course ho. Phir 2 objects banao.",
            "tip": "💡 Tip: `self` object ki apni properties ki taraf ishara karta hai.",
            "quiz": make_quiz("Class se banayi hui cheez kya kehlati hai?", ["Function", "Object", "Variable"], "Object")
        },
        {
            "title": "32. Inheritance & Polymorphism",
            "theory": """Inheritance se aik class dosri class ki properties le sakti hai. Polymorphism se aik hi method alag classes mein alag kaam kar sakta hai.""",
            "example": """# Inheritance
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

for animal in [Dog(), Cat()]:
    print(animal.speak())""",
            "task": "Aik base `Vehicle` class banao aur `Car` aur `Bike` classes us se inheritance lein.",
            "tip": "💡 Tip: Inheritance se code dobara use hota hai (DRY principle).",
            "quiz": make_quiz("Inheritance kya hoti hai?", ["Class doosri class ki properties leti hai", "Error handle karna", "File banani"], "Class doosri class ki properties leti hai")
        },
        {
            "title": "33. Modules & Packages",
            "theory": """Module aik Python file hai jismein functions/classes hote hain. Package modules ka folder hota hai. `import` se humein code reuse karna asaan hota hai.""",
            "example": """# Built-in module
import math
import random

print(math.sqrt(16))
print(random.randint(1, 10))""",
            "task": "Aik apni Python file `utils.py` banao jismein `add()` function ho aur use import karo.",
            "tip": "💡 Tip: Apna module banane se project organize rehta hai.",
            "quiz": make_quiz("Module import karne ke liye keyword kya hai?", ["import", "include", "using"], "import")
        },
        {
            "title": "34. Virtual Environment & pip",
            "theory": """Virtual environment aik alag Python setup hai har project ke liye. `pip` se aap external libraries install karte ho. AI/ML libraries bhi pip se install hoti hain.""",
            "example": """# Commands (terminal mein chalao)
# python -m venv myenv
# myenv\\Scripts\\activate    # Windows
# source myenv/bin/activate  # Mac/Linux
# pip install numpy pandas""",
            "task": "Apne system mein virtual environment banao aur usmein numpy install karo.",
            "tip": "💡 Tip: Har project ke liye alag virtual environment best practice hai.",
            "quiz": make_quiz("Python libraries install karne ke liye kya use hota hai?", ["pip", "zip", "html"], "pip")
        },
        {
            "title": "35. Working with APIs",
            "theory": """API (Application Programming Interface) do systems ko apas mein baat karwata hai. Python `requests` library se websites se data le sakti hai.""",
            "example": """import requests

# Free API example
response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json()["current_user_url"])""",
            "task": "Kisi free API se weather data lenay ki koshish karo.",
            "tip": "💡 Tip: Internet connection chahiye. Status code 200 matlab successful.",
            "quiz": make_quiz("API kya hai?", ["User interface", "Do systems ki baat-cheet", "Programming language"], "Do systems ki baat-cheet")
        },
        {
            "title": "36. Regular Expressions (Regex)",
            "theory": """Regex se text patterns search karte hain. Emails validate karna, phone numbers find karna, text replace karna — sab regex se ho sakta hai.""",
            "example": """import re

text = "Mera email ali@gmail.com hai"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"

match = re.search(pattern, text)
if match:
    print("Email mila:", match.group())""",
            "task": "Aik text mein se sab phone numbers nikalo using regex.",
            "tip": "💡 Tip: Regex shuru mein mushkil lagta hai lekin bohat powerful hai.",
            "quiz": make_quiz("Regex kis liye use hota hai?", ["Text patterns search", "Math calculations", "File create"], "Text patterns search")
        },
        {
            "title": "37. Database with SQLite",
            "theory": """SQLite Python mein built-in database hai. Aap tables bana sakte ho, data save, update, delete kar sakte ho. Apps ke liye bohat useful hai.""",
            "example": """import sqlite3

conn = sqlite3.connect("school.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY, naam TEXT, umar INTEGER)''')

c.execute("INSERT INTO students VALUES (1, 'Ali', 20)")
conn.commit()

for row in c.execute("SELECT * FROM students"):
    print(row)

conn.close()""",
            "task": "Aik `products` table banao jismein name, price, quantity ho. 3 products add karo.",
            "tip": "💡 Tip: SQL commands ko capital letters mein likhna common convention hai.",
            "quiz": make_quiz("SQLite mein data fetch karne ke liye kaunsa command use hota hai?", ["INSERT", "SELECT", "DELETE"], "SELECT")
        },
        {
            "title": "38. JSON Data Handling",
            "theory": """JSON aik popular data format hai jo APIs aur config files mein use hota hai. Python mein `json` module se handle karte hain.""",
            "example": """import json

data = {
    "naam": "Sara",
    "umar": 22,
    "skills": ["Python", "AI"]
}

json_string = json.dumps(data, indent=4)
print(json_string)

parsed = json.loads(json_string)
print(parsed["naam"])""",
            "task": "Aik dictionary banao aur usay JSON file mein save karo, phir dobara parho.",
            "tip": "💡 Tip: `dumps` Python object ko JSON string banata hai, `loads` string ko object banata hai.",
            "quiz": make_quiz("JSON string ko Python object mein convert karne ke liye kya use hota hai?", ["json.dumps", "json.loads", "json.write"], "json.loads")
        }
    ],

    "🤖 AI/ML Basics": [
        {
            "title": "39. AI/ML Kya Hai?",
            "theory": """AI (Artificial Intelligence) computers ko smart banana hai. ML (Machine Learning) AI ka aik hissa hai jismein computer data se seekhta hai bina explicitly programmed kiye. Deep Learning neural networks se kaam karta hai.""",
            "example": """# AI/ML simple example
# Data: ghar ka size vs price
# Model: pattern seekhta hai
print("AI = Smart Computer Systems")
print("ML = Data se seekhna")
print("Deep Learning = Neural Networks")""",
            "task": "Apni zubaan mein likho ke AI, ML, aur Deep Learning mein kya farq hai.",
            "tip": "💡 Tip: ML mein data sab se zaroori hai — jitna acha data, utna acha model.",
            "quiz": make_quiz("Machine Learning mein computer kahan se seekhta hai?", ["Books", "Data", "Internet directly"], "Data")
        },
        {
            "title": "40. NumPy Basics",
            "theory": """NumPy numerical computing ki library hai. Arrays (NumPy arrays) normal Python lists se fast hote hain aur mathematical operations asaan kar dete hain.""",
            "example": """import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr * 2)      # har element double
print(arr.mean())   # average
print(arr.sum())    # total

matrix = np.array([[1, 2], [3, 4]])
print(matrix)""",
            "task": "Aik NumPy array banao 1 se 10 tak aur uska sum, mean, max nikalo.",
            "tip": "💡 Tip: NumPy arrays par operations automatically har element par lagte hain.",
            "quiz": make_quiz("NumPy kis liye famous hai?", ["Web design", "Fast numerical computing", "Database"], "Fast numerical computing")
        },
        {
            "title": "41. Pandas Basics",
            "theory": """Pandas data manipulation ki library hai. `DataFrame` Excel sheet jaisa structure hai jismein rows aur columns hote hain. Data analysis mein sab se zyada use hoti hai.""",
            "example": """import pandas as pd

data = {
    "Naam": ["Ali", "Sara", "Ahmed"],
    "Umar": [20, 22, 21],
    "Grade": ["A", "A+", "B"]
}

df = pd.DataFrame(data)
print(df)
print("\nAverage umar:", df["Umar"].mean())""",
            "task": "Aik DataFrame banao apne 5 classmates ke naam, umar, aur city ke saath. Phir average umar print karo.",
            "tip": "💡 Tip: Column select karne ke liye `df['ColumnName']` likho.",
            "quiz": make_quiz("Pandas mein data ka structure kya kehlata hai?", ["Array", "DataFrame", "List"], "DataFrame")
        },
        {
            "title": "42. Data Cleaning",
            "theory": """Real world data ganda hota hai — missing values, duplicates, wrong types. Pandas se aap data clean kar sakte ho. Yeh ML ka sab se boring lekin zaroori hissa hai.""",
            "example": """import pandas as pd
import numpy as np

data = {
    "Naam": ["Ali", "Sara", "Ali", np.nan],
    "Umar": [20, np.nan, 20, 22],
    "City": ["KHI", "LHR", "KHI", "ISB"]
}
df = pd.DataFrame(data)
print("Original:")
print(df)

df = df.drop_duplicates()
df["Umar"] = df["Umar"].fillna(df["Umar"].mean())
print("\nCleaned:")
print(df)""",
            "task": "Aik DataFrame banao jismein missing values hain. Unhein fill ya remove karo.",
            "tip": "💡 Tip: `.isnull().sum()` batata hai ke har column mein kitni missing values hain.",
            "quiz": make_quiz("Missing values ko bharne ke liye kaunsa method use hota hai?", ["fillna", "dropna", "remove"], "fillna")
        },
        {
            "title": "43. Matplotlib - Data Visualization",
            "theory": """Data samajhne ka sab se acha tareeqa hai usay dekhna. Matplotlib se aap charts, line graphs, bar charts, scatter plots bana sakte ho.""",
            "example": """import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o')
plt.title("Simple Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()""",
            "task": "Aik bar chart banao apne 5 favourite sports ki popularity ka.",
            "tip": "💡 Tip: Graphs presentation aur analysis dono mein kaam aate hain.",
            "quiz": make_quiz("Charts banane ke liye kaunsi library famous hai?", ["numpy", "matplotlib", "pandas"], "matplotlib")
        },
        {
            "title": "44. Machine Learning Workflow",
            "theory": """ML project ka standard flow: 1) Data collect, 2) Clean, 3) Explore, 4) Split train/test, 5) Choose model, 6) Train, 7) Test, 8) Improve. Har step zaroori hai.""",
            "example": """# ML Workflow steps
steps = [
    "1. Data Collection",
    "2. Data Cleaning",
    "3. Data Exploration",
    "4. Train/Test Split",
    "5. Model Selection",
    "6. Training",
    "7. Evaluation",
    "8. Deployment"
]
for step in steps:
    print(step)""",
            "task": "Apne project ke liye ML workflow ke har step ko apni zubaan mein likho.",
            "tip": "💡 Tip: 80% time data cleaning aur preparation mein lagta hai, 20% modeling mein.",
            "quiz": make_quiz("ML mein sab se zyada time kis cheez par lagta hai?", ["Model training", "Data cleaning/preparation", "Presentation"], "Data cleaning/preparation")
        },
        {
            "title": "45. Scikit-learn Introduction",
            "theory": """Scikit-learn Python ki sab se popular ML library hai. Ismein classification, regression, clustering algorithms hain. Syntax bohat consistent hai.""",
            "example": """from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)

print("Coefficient:", model.coef_)
print("Prediction for 6:", model.predict([[6]]))""",
            "task": "Apne simple data par Linear Regression model train karo aur predictions karo.",
            "tip": "💡 Tip: Scikit-learn mein `fit()` train karne ke liye, `predict()` predict karne ke liye.",
            "quiz": make_quiz("Scikit-learn mein model train karne ke liye kaunsa method use hota hai?", ["train()", "fit()", "learn()"], "fit()")
        },
        {
            "title": "46. Train/Test Split",
            "theory": """Data ko training aur testing hisson mein baantna zaroori hai. Is se pata chalta hai ke model naye data par kaisa chalega. Overfitting tab hoti hai jab model sirf training data yaad kar le.""",
            "example": """from sklearn.model_selection import train_test_split
import numpy as np

X = np.array([[i] for i in range(1, 101)])
y = np.array([i*2 for i in range(1, 101)])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Train size:", len(X_train))
print("Test size:", len(X_test))""",
            "task": "Aik dataset lo aur usay 70% train, 30% test mein baanto.",
            "tip": "💡 Tip: `random_state` same rakho taake har baar same split mile.",
            "quiz": make_quiz("Test set kis liye hota hai?", ["Model evaluate karne ke liye", "Model train karne ke liye", "Data delete karne ke liye"], "Model evaluate karne ke liye")
        },
        {
            "title": "47. Model Evaluation Metrics",
            "theory": """Model kitna acha hai, iske liye metrics hain. Regression ke liye MAE, MSE, R2 score. Classification ke liye accuracy, precision, recall, F1-score.""",
            "example": """from sklearn.metrics import mean_absolute_error, r2_score

y_true = [10, 20, 30, 40]
y_pred = [12, 19, 31, 38]

print("MAE:", mean_absolute_error(y_true, y_pred))
print("R2 Score:", r2_score(y_true, y_pred))""",
            "task": "Apne predictions ka R2 score aur MAE calculate karo.",
            "tip": "💡 Tip: R2 score 1 ke qareeb acha hota hai. MAE jitna chhota utna acha.",
            "quiz": make_quiz("R2 Score kis ke liye use hota hai?", ["Regression", "Classification", "Clustering"], "Regression")
        },
        {
            "title": "48. Classification Basics",
            "theory": """Classification mein hum categories predict karte hain. Jaise email spam hai ya nahi, patient diabetic hai ya nahi. Logistic Regression aur Decision Tree common hain.""",
            "example": """from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))""",
            "task": "Iris dataset par Decision Tree classifier train karo aur accuracy check karo.",
            "tip": "💡 Tip: Iris dataset ML learners ke liye classic example hai.",
            "quiz": make_quiz("Classification mein output kya hota hai?", ["Number", "Category/Class", "Image"], "Category/Class")
        },
        {
            "title": "49. Neural Networks Basics",
            "theory": """Neural networks brain ke neurons se inspired hain. Deep Learning mein bohat se layers hote hain. Activation functions, weights, biases, backpropagation important concepts hain. Simple explanation ke liye perceptron dekho.""",
            "example": """# Simple perceptron idea
inputs = [1, 2, 3]
weights = [0.2, 0.4, 0.1]
bias = 0.5

output = sum(i * w for i, w in zip(inputs, weights)) + bias
print("Perceptron output:", output)""",
            "task": "3 inputs aur weights le kar aik simple perceptron output calculate karo.",
            "tip": "💡 Tip: Real neural networks mein bahut se perceptrons layers mein hote hain.",
            "quiz": make_quiz("Neural network ka bunyadi unit kya hai?", ["Perceptron", "Loop", "Variable"], "Perceptron")
        },
        {
            "title": "50. AI Project: House Price Prediction",
            "theory": """Ab hum sab kuch mila kar aik simple AI project banate hain: ghar ka price predict karna size ke hisaab se. Yeh complete pipeline hai: data → model → prediction → evaluation.""",
            "example": """import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Size in square feet, Price in lakhs
sizes = np.array([500, 800, 1000, 1200, 1500, 1800, 2000, 2500]).reshape(-1, 1)
prices = np.array([15, 22, 28, 35, 42, 50, 58, 70])

X_train, X_test, y_train, y_test = train_test_split(
    sizes, prices, test_size=0.25, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Predictions:", predictions)
print("MAE:", mean_absolute_error(y_test, predictions))
print("1500 sqft ghar ka expected price:", model.predict([[1500]]))""",
            "task": "Apna dataset banao (jaise mobile price vs RAM) aur Linear Regression se predict karo.",
            "tip": "💡 Tip: Yeh project aapki CV mein dikhane ke liye best hai. GitHub par upload karo!",
            "quiz": make_quiz("House price prediction kis type ka ML problem hai?", ["Regression", "Classification", "Clustering"], "Regression")
        }
    ]
}
