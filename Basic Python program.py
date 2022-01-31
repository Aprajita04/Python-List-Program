#WAP TO PRINT "HELLO PYTHON
'''
print('Hello Python')
___________________________________
#WAP to a Arithmetical operations addition and division

a = 55
b = 5
total = a+b
print(total)
value = a/b
print(value)
______________________________________

#WAP to find area of triangle(based on 3 sides )
a = 8
b = 7
c = 6
a = float(input('Enter 1st side of the triangle:'))
b = float(input('Enter 2nd  side of the triangle:'))
c = float(input('Enter 3rd side of the triangle:'))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of  the triangle  is %0.2f' % area)
_________________________________________________________

# WAP to Swap two variables
a = 50
b = 40
print("\nBefore Swap a  = %d and b= %d"%(a,b))
a,b = b,a
print("\nAfter Swaping a = %d and b =%d" %(a,b))
print()
____________________________________________________

#WAP To generate a random number(random number which generate a float no b/w 0 and 1 and we have to use randint() function.
import random
    n = random.random()
    print(n)
_____________________________________________________________________________
#ASSIGNMENT2
#WAP to convert Kilometres to miles.

# Python kilometer converter(formula 1km = 1000m)
km = 15
km = float(input("Value in unit kilometers: "))
#converting to meters
meter = km * 1000.0
print('%0.2f km is equal to %0.2f meters' %(km,meter))
_________________________________________________________________________
#WAP to convert celsius to Fahrenheit(formula fahrenheit = celsius * 1.8 + 32)
celsius = 57.5
# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))
______________________________________________

#WAP to display calender.
import calendar
yy = 2022
mm = 3
# To take month and year input from the user
 #yy = int(input("Enter year: "))
 #mm = int(input("Enter month: "))
print(calendar.month(yy, mm))
______________________________________________

#WAP to solve quadratic equation(ax2 + bx + c = 0, wherea, b and c are real numbers and a ≠ 0)

# Solve the quadratic equation ax**2 + bx + c = 0
import cmath
a = 10
b = 8
c = 4
d = (b**2) - (4*a*c)
# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))
________________________________________________

#WAP to Swap two variables without temp variable
x = 50
y = 10
x, y = y, x
print("x =", x)
print("y =", y)
______________________________________________
#ASSINMENT5
#Wap to convert dec to hexdec.

d = int(input("Enter a no :"))
print("Hexadecimal:" ,hex (d))
_____________________________________







