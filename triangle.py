# Determines Area of triangle using Heron's formula
# Joshua Lochner
# 25 February 2018

from math import sqrt

a = eval(input("Enter the length of the first side: "))
b = eval(input("Enter the length of the second side: "))
c = eval(input("Enter the length of the third side: "))

s = (a+b+c)/2
area = sqrt(s*(s-a)*(s-b)*(s-c))

print("The area of the triangle with sides of length",a,"and",b,"and",c,"is",area,end=".")