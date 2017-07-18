num = 5
print("Using for loops:")
print("Way #1:") #Print certain string based on the value of i
for i in range (0,5):
    if i == 0:
        print("5")
    elif i == 1:
        print("4")
    elif i == 2:
        print("3")
    elif i == 3:
        print("2")
    elif i == 4:
        print("1")
print("Blast off!")
print("\n")
print("Way #2:") #Value of i decreases by 1 each time
for i in range (5,0,-1):
    print(i)
print("Blast off!")
print("\n")
print("Way #3:") #Goes through loop and prints the negative of i
for i in range (-5,0):
    print(-i)
print("Blast off!")
print("\n")
print("Way #4:") #prints value of num each time, and then decreases value of num by 1
for i in range (0,5):
    print(num)
    num -= 1
print("Blast off!")
print("\n")
print("Way #5:") #Print same value in list
num2 = ["5","4","3","2", "1", "Blast off!"]
for i in range(0, 6):
    print(num2[i])
print("\n")
print("Way #6:")
for i in range(1,6):
    print(6 - i)
print("Blast off!")
print("\n")
print("Using while loops:")
print("\n")
print("Way #1:") #Combination of way #2 and #4 of for loops
num = 5
while num > 0:
    print(num)
    num -= 1
print("Blast off!")
print("\n")
print("Way #2:") #Same as #4 in for loops but using addition instead of subtraction
num = 0
while num < 5:
    num += 1
    print(num)
print("Blast off!")
print("\n")
print("Using functions:") #Counts down using functions. Just 'cause
num = 5
def count(number):
    "This counts down and prints 'Blast off!'"
    while number > 0:
        print(number)
        number -= 1
    print("Blast off!")
count(num)
print("\n")
print("So many things are blasting off...")
"""print("\"")
print("\n")
print("\tHello")
print("\\")
print("\'")
class myClass:
    name = "Jenna"
x = myClass
print(x.name) """
