'''
def add(a,b):
    print("add",a+b)
add(5,6)
def sub(a,b):
    print("sub",a-b)
sub(5,6)
def mul(a,b):
    print("mul",a*b)
mul(5,6)
def div(a,b):
    print("div",a/b)
div(5,6)

def area_circle(radius):
    area = 3.14 * radius**2
    print("Area of circle:", area)

area_circle(5) 

def area_triangle(base, height):
    area = 0.5 * base * height
    print("Area of triangle:", area)

area_triangle(3,4)

def odd_even(num):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
num=int(input("Enter a number to check if it is odd or even: "))
odd_even(num)

def count(string):
    vowels = 0
    consonants = 0
    for char in string:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowels += 1
            else:
                consonants += 1
        else:
            continue
    print("Vowels:", vowels)
    print("Consonants:", consonants)

str=input("Enter a string to count vowels and consonants: ")
count(str)
'''
def avg_list(lst):
    if len(lst) == 0:
        print("List is empty, cannot compute average.")
        return
    average = sum(lst) / len(lst)
    print("Average of the list:", average)

#lst=[int(x) for x in input("Enter numbers separated by spaces to compute average: ").split()]
lst = [10, 20, 30, 40, 50]
avg_list(lst)