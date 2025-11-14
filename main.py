
import numpy
from numpy import random
import pandas as pd


# my_list =["apple " , "gtfg" , "fyhghg" , "6" ,"7" , "0"]

# my_list[2 : 5] = ["abc"]
# print(my_list)

# my_list=[1,2,4,5,6]
# my_list.insert(2,"ggyugy")
# print(my_list)

# my_list=[1,2,4,5,6]
# my_list.append("ggyugy")
# print(my_list)

# list1 = [1,2,3]
# list2 = [4,5,6]
# list1.extend(list2)

# print(list1)


# list1 = [1,2,3,"apple" , 4,5,6]
# list1.remove("apple")
# print(list1)











# list1 = [1,2,3,4,5,6]
# list1.append("apple")
# print(list1)


# list1.insert(2,"apple")
# print(list1)

# list1.remove(6)
# print(list1)


# lista = [1,2,3,4]
# listb =[5,6,7,8]
# lista.extend(listb)
# print(lista)


# lista.pop()
# print(lista)

# lista.clear
# print(list)



# lista[0] ="hello"
# print(lista)



# #loopslists
# list1=[1,2,3,4,5,6]
# for x in list1:
#     print(x)

 
# list1=[1,2,3,4,4,4,5,6]
# for x in list1:
#     print(x)


# text = "hello"
# print(text.upper())


# text = "HELLO"
# print(text.lower())

# text = "      HELLO"
# print(text.strip())


# text = "HELLO"
# print(text.replace("HELLO" ,"world"))

# text = "HELLO"
# print(text.split())



# #X = 5
# #Y = "HGUU"
# #print(X + Y)



# # format strings 

# name = "prince"
# age = 18
# print(f"my name is {name} and i am {age} years old")


# a = 6
# a+=5
# print(a)



# a = 6
# a-=5
# print(a)


# a = 6
# a*=5
# print(a)

# a = 6
# a/=5
# print(a)



# x = 65
# y = 76
# print(x==y)
# print(x!=y)
# print(x<y)
# print(x>y)
# print(x>=y)
# print(x<=y)


# print (x==y and x!=y)
# print (x==y  or x!=y)


# print(x is y)
# print(x is not y)

# names = {"b" , "h" , "g" , "j" , "y"}
# print(names)
# names.add("m")
# print(names.add("m"))

# print(names.remove("b"))

# names = {"b" , "h" , "g" , "j" , "y"}
# for x in names :
#     print(x)


# students = {
#         "name" : "prince" ,
#         "age" : "18" ,
#         "grades" : "86"
#     }
# print(students)


# age = 17
# if age >= 18:
#     print("you are adult")

# elif age ==18:

#     print("you are teen")


# else:
#     print(" you are not adult")


# x = 15

# if x > 10:
#     print("x is greater than 10")

#     if x>20:
#         print("x is greater than 20")
#     else :
#         print ("x is not greater than 20")


# x = 22

# if x%2 == 0:
#     print("x is even")
# else:
#     print("x is odd")


# x = 17
# if x>=18:
#     print("you are eligible for driving")
# else:
#     print("you are not eligible for driving")

# word = "python"
# for letter in word :
#     print(letter)

# for i in range (1, 10000,9 ):
#     print(i)



# for i in range (1,4):
#     for j in range (1,3):
#         print(f"i={i} , j ={j}")

# for i in range (1,6):
#     if i ==4:
#         break
#     print(i)

# for i in range (1,21,1 ):
#     print(i)


# for i in range (0,31,2):
#     print(i)


# for i in range (1,10):
#     if i ==7:
#         break
#     print(i)
# print("stop the loop")

# def greet():
#     print("Hello.Python")
# greet() #calling the function


# def greet (name):
#     print(f"hello , (name)")
# greet ("alice")
# greet("bob")


# def add(a,b):
#     return a+b
# result =add(5,39)
# print(result)

# def difference(a,b):
#     return a-b
# result =difference(5,39)
# print(result)

# def greet(name="student"):
#     print(f"hello,(name)")
# greet()
# greet("alice")



# x = 10
# def my_func():
#     y = 5 
#     print(x,y)

# my_func()
# print()


# def greet():
#     print(f"Hello!")
# greet()


# def add(a,b):
#     return a + b
# result=add(546,768)
# print(result)



# class car:
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color= color
#     def drive (self):
#         print(f"{self. color}{self. brand} is driving🚗")

# #class

# car1 = car("BMW" , "Black")
# car2 = car("Tesla" ,"white")

# car1.drive()
# car2.drive()








x = random.random(100)
print(x)

x = pd.read_csv('Ipl_matches.csv')
print(x)
