# print("hello world")
# print("hello world")

#==================== Sequence types data==========================
# List, Tuple, Range => Sequence types data

List = ["a", "b", "c"] #miutable data
List[2] = "Shajjad"

Tuple = ("a", "b", "c") #immiutable

Range = range(6);

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
a = 50
b = 60

a, b = b, a
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
mylist = ["apple", "banana","abc", "cde", "edh", "123"]
mylist.append("orange")

# print(mylist)

mylist.insert(1, "banana")

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
numberlist = [1,3,9,5,2,7,4,8]
strr = ["c", "b", "a", "d", "f", "e"]
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
numberlis1 =(1,3,9,5,2,7,4,8)
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
myset = {"Shajjad", "Sakib", "Sahed", "Mehedi", "Areafat"}
myset1 = {1, 2, 4, 5, 3, 8, 6, 7}
booleann = {True, False, True}

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
myinfo = {
    "category": {
        "parentCategory": "Boards",
        "subCategory": "Melamine Board",
        "description": "Elevate your interior",
        "title": "Melamine Board",
    },
    "info": {
        "location": "Dhaka",
        "price": "BDT 3000",
        "contactInfo": "01787764356",
        "seller": "652626a0fc85f53bc8bb88c7"
    },
    "name": "Md shajjad"

}
print(myinfo["category"]["title"])
print(myinfo["name"])