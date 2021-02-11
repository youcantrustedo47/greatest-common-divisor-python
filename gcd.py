'''

Greatest common divisors of two numbers

by trustnoedo

'''

# Function
def divisors(x):
    l = []
    lstrng = list(range(1, x+1))
    for i in lstrng:
        if x % i == 0:
            l.append(i)
    return l


# Introduction
print()
print("--------------------------------------------------------------------")
print()
print("Hi, welcome to the program!")
print("This app is a greatest common divisor calculator for two numbers")
print()
print("--------------------------------------------------------------------")
print()

# Storing and gcd
n1 = int(input("Insert n1: "))
l1 = divisors(n1)
n2 = int(input("Insert n2: "))
l2 = divisors(n2)

l1_as_intersection = set(l1)
intersection = l1_as_intersection.intersection(l2)

result = max(intersection)
if result == 1:
    print("There are no common divisors except for 1!")
else:
    print(result)
