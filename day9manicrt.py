
#1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
##Sample Dictionary ( n = 5) :
##Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

##n = 5
##flag =5
##for val in range(3):
##    c=c+1
##    if c==1:
##       for val in set1:
##        for val in set2 or val in set3:
##           flag=5
##           break
##            
##    if c==2:       
##       for val in set2:
##        if val in set1 or val in set3:
##             flag=1
##             break
##            
##    if c==3:
##       for val in set3:
##        if val in set2 or val in set1:
##            flag=1
##            break
##if flag==0:
##    print("jiont")


# 2.)Find the uncommon words from 2 strings

##s1 = "Hello how are you"
##s2 = "Hello how is"
##
##for val in s2:
##    if val not in s1:
##        print(val)


# 3.)Wrire a code print the 8th fibanochi number
# 0, 1, 1, 2, 3, 5, 8

##num = 8
##n1 = 0
##n2 = 1
##
##for val in range(num):
##   ans = n1+n2
##   n1 = n2
##   n2 = ans
##print(ans)

# ? Eg:1
# ! constructors
# ? Eg:1;
# * unParametarised constructor

##class profile:
##    def _init_(self):
##        print("hello world")

##obj = profile()
##obj._init_()     

# ? Eg:2
# * Parametarised constructor

##class profile:
##    def __init__(self, id, name, age):
##        print(id, name, age)
##
##obj = profile(1, "mani", 22)

# ? Eg:3
##class c1:
##    name = "mani"
##    place= "ndl"
##    email = "mani@gmail.com"
##def m1(self):
##    name = "mani"
##    place= "ndl"
##    print(name, place)
##    print(self.email)
##
##object = c1()
##object.m1().

# ? Eg:4

##class c1:
##    def m1(self):
##        name = "mani"
##        age = 22
##        return name, age
##    def display(self):
##        print(self.name, self.age)
##        print(self.m1())
##
##object = c1()
##object.display()

# ? Eg:5;
##class class1:
##    def __inti__(self):
##        self.name = "mani"
##        self.email = "mani@gmail.com"
##
##    def display(self):
##        print(self.name, self.email)
##
##c1 = class1()
##c1.diaplay()

# ! -----------> Inheritance
# The p[rocesss of urilising the methods and attributes of parent class
# through the object of child class it is called as inheritance

# ? 5 types of inheritance
# single inherantance
# Multilevel inheritance
#Multiple inheritance
# Hybrid inheritance
#Heirarichal inheritance

## * single Inheritance
# ? It has only one parent class and only one child class
# Eg:1;
##class parent:
##    def m1(self):
##        print("I am parentclass")
##
##class child:
##    def m2(self):
##        print("I am child class")
##obj = parent()
##obj.m2()
##
##
##obj = child()
##obj.m1()

# ! Eg:2;
##class c1:
##    def __init__(self):
##        print("Iam constructor from parent class")
##
##class child1(cl):
##    pass
##
##obj.child1()

# ! Eg:3;
##class parent:
##    name = "mani"
##
##class child(parent):
##    name = "name1"
##
##    def display(self):
##        print(self.name)
##
##d= child()
##d.display()

# ! Multilevel inheritance
# ! Eg:1;
class voice:
    def sound(self):
        print("All the animals have their own voices")

class cat(dog):
    def dog_voice(self):
        print("bark")

class parrot(cat):
    def cat_vioce(self):
        print("speak")

        
all - parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()
