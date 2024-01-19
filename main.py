# print("hello world")
# print("hello world")

#==================== Sequence types data==========================
# List, Tuple, Range => Sequence types data

# List = ["a", "b", "c"] #miutable data
# List[2] = "Shajjad"
#
# Tuple = ("a", "b", "c") #immiutable
#
# Range = range(6);

# for i in Range: print(i)

# print(List)



# ===================== Python Operators ======================

# Arithmetic operator
#  +, -, *, /, %, **, //


# Assignment Operators
# =, +=, -=, *=, /=, %=, //=,  &=, |=


# Comparison Operators
# ==, !=, >, <, >=, <=


# Logical Operators
# and, or, not



#================== Swapping ======================
# a = 50
# b = 60
#
# a, b = b, a
# print(a, b)


# =================== Python User Input ==================
# username = input("enter your username: ")

# print(username)


# =========== Type casting ================
# to convert one type to another type and the function which we are used for this that function call as casting function
# name = "509832"

# print(int(name))
# print(type(int(name)))


#=================pythone list================
# mylist = ["apple", "banana","abc", "cde", "edh", "123"]
# mylist.append("orange")

# print(mylist)

# mylist.insert(1, "banana")

# print(mylist)

# Remove list items


# mylist.remove("apple")
# print(mylist)

# mylist.pop(1)
# print(mylist)

# del mylist[1]
# print(mylist)

# mylist.clear()

# print(mylist)


# Loop list ==============================

# for x in mylist: print(x)
# for i in range(len(mylist)): print(i)

# y= 2
# while y< len(mylist):
#     print(mylist[y])
#     y = y + 1

# List comprehension ===========================
# numberlist = [1,3,9,5,2,7,4,8]
# strr = ["c", "b", "a", "d", "f", "e"]
# for i in numberlist : print( i * 2 )

# Double = [ i * 2 for i in numberlist ]
# print(Double)
# Double1= [ i +2 for i in numberlist ]
# print(Double1)

# Sort Lists ======================================
# numberlist.sort()
# print(numberlist)
# strr.sort()
# print(strr)
#
# numberlist.sort(reverse= True)
# print(numberlist)

# Copy Lists ========================================
# newlist = strr.copy()
# print(newlist)

# Join two lists ==================================
# num2 = [45, 34, 567, 333]
#
# num3 = numberlist + num2 + strr
# print(num3)
#
# numberlist.extend(num3)
# print(numberlist)


# List methods ======================================


#Matrix.============================================
 # matt =[
 #     ["a", "b", "c"],
 #     [1, 2, 3], 10
 # ]


# python tuples =========================================
# numberlis1 =(1,3,9,5,2,7,4,8)
# a =list(numberlis1)
# a.append("shajjad")
# y = tuple(a)
# print(y)

# unpack tuples========================================
# a,b,c,d,e,f,g,h = numberlis1
#
# print(a)
#
# (*a,)= numberlis1
# print(a)
#
# (a,b,c,*d) = numberlis1
# print(d)
#
# (a,*b,c,d) = numberlis1
# print(b)


# loop tuples ==============================================
# for i in numberlis1:
#     print(i)
#
# for i in range(len(numberlis1)):
#     print(i)#     aaa = 2
# aa = 2
# while aa<len(numberlis1):
#     print(numberlis1[aa])
#     aa = aa + 1


# Join tuples ============================================
# print(numberlis1 * 3)
# print(numberlis1.count(2))
# print(numberlis1.index(5))


# python sets ==================================================
# myset = {"Shajjad", "Sakib", "Sahed", "Mehedi", "Areafat"}
# myset1 = {1, 2, 4, 5, 3, 8, 6, 7}
# booleann = {True, False, True}

# print(myset)
# print(myset1)
# print(booleann)

# for i in myset:
#     print(i)
#
# print("Sahed" in myset)


# Add set item ====================
# myset.add("Tanzim")
# myset.update(myset1)
# print(myset)

# Remove set item =======================
# myset.remove("Sakib")
# print(myset)
# myset.pop()
# print(myset)

#Python loop set===================
# for i in myset:
#     print(myset)

#join set ==================


# Python Access Dictionary Items====================
# myinfo = {
#     "category": {
#         "parentCategory": "Boards",
#         "subCategory": "Melamine Board",
#         "description": "Elevate your interior",
#         "title": "Melamine Board",
#     },
#     "info": {
#         "location": "Dhaka",
#         "price": "BDT 3000",
#         "contactInfo": "01787764356",
#         "seller": "652626a0fc85f53bc8bb88c7"
#     },
#     "name": "Md shajjad"
#
# }
# print(myinfo["category"]["title"])
# print(myinfo["name"])

# print(myinfo.get("info").get("price"))
# print(myinfo.keys())
# print(myinfo.values())


# Change Dictionaries items ==========================
# changes= myinfo["name"] = "Sahed vai"
# print(changes)
# print(myinfo)
#
# updatechanges = myinfo.update({"name" : "tutul"})
#
# print(updatechanges)
# print(myinfo)

# myinfo.pop("name")
# myinfo.pop("category")
# myinfo.popitem()
# del myinfo["category"]
# myinfo["category"].clear()
# myinfo.clear()
# print(myinfo)

# for i in myinfo["category"] :
#     print(i)

# for i in myinfo["info"] :
#     print(i)

# for i in myinfo.values():
#     print(i)

# for i in myinfo.keys():
#     print(i)

# for i, j in myinfo.items():
#     print(i, j)


# Python copy Dictionaries =====================================

# myNewInfo = myinfo.copy()

# print(myNewInfo)

# myNew = dict(myinfo)
# print(myNew)


# Python conditions and if statements ===================================================
#
# a = 100
# b = 1200
# c = 60
# d = 100
#
# if a > b:
#     print("a is big")
# elif a == d:
#     print("a and b equal")
# else :
#     print("b is big")


# Python loops ===============================================================================
# for loop
# while loop
# aaa = 1
# while aaa < 10 :
#      print("yes")
#      aaa = aaa + 1


# python functions ==================================================================

# namee = "shajjad hossan"
# Roll = 2344
# isFalse = True
#
# def My_function(name):
#     print(name)
#
# My_function(namee)
# My_function(Roll)
# My_function(isFalse)


arrayList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for x in range(len(arrayList)):
#     if x == 5:
#         break
#     print(x)
#
# print("continueeeeee")
#
# for x in range(len(arrayList)):
#     if x == 5:
#         continue
#     print(x)


# Python zip function ============================================
# list1 = [11, 22, 33, 44]
# list2 = [55, 66, 77, 88]
#
# print(list(zip(list1, list2)))


# Python Lamda function ==========================================

# myFun = lambda a, b : a*b
#
# print(myFun(2, 5))


# Python debugging ===================================================

# Python Array =========================================

# python Classes and Objects ==========================================

class Parents:
     car = "BMW"
     house = "4 Cr"
     money = "12223456734"
     child = "5"


class Parents2:
    ac = "sonny"
    pc = "big"
    laptop = "hp corei 7"
    iphone = "12"

class Parents3:
    tv = "sonny led"
    bike = "big bike"
    gf = "hp onk"
    tree = "142"

class kaka(Parents, Parents2, Parents3):
    etc = "BMW3e"
    btc = "3 Cree"

A = kaka()
# print(A.child)

# Multiple Inheritance =======================



# python iterators ====================================================
Myarray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in Myarray:
#     print(i)

x = iter(Myarray)
# print(x.__next__())
# print(next(x))

# Python Scope =========================================================

# Pythone DateTime =====================================================

import datetime
a = datetime.datetime.now()

# print(a.strftime("%A"))
# print(a.strftime("%D"))
# print(a.strftime("%T"))
# print(a.strftime("%Y"))
# print(a.strftime("%m"))


# Math module ===========================
# print(min(Myarray))
# print(max(Myarray))
#
# a = -34
# print(abs(a))
# print(pow(3, 6))


# Python Regex ==========================
import re
myText = "My name is Md Shajjad Hossan, and i'm a software developer."
# findall
# search
# split
# sub

# pattern = "[a-z]"
# pattern1 = "^1"
# pattern2 ="/d"
# # print(re.findall("[A-Z]", myText))
# # print(re.findall(pattern, myText))
# a = re.findall(pattern1, myText)
# b = re.findall(pattern2, myText)
#
# print(b)
#
# if a:
#     print("true")
# else:
#     print("false")


# Try and Except ==========================
# try:
#     print("successfulll")
# except:
#     print(fhhhhh)
#
# print("hellooooooooooo")


# Python file open ===========================

# readText = open("text.text", "r")
# print(readText.read())

create = open("shajjad.html", "w")
create.write("<h1>MD shajjad</h1>")
