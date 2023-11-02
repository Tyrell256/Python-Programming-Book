def Odd_or_Even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
Odd_or_Even(100)
Odd_or_Even(78)

def Pass_or_Fail(num):
    if num >= 50:
        print("Pass")
    else: 
        print("Fail")
Pass_or_Fail(4)
Pass_or_Fail(27)

# Chapter 8: Loops in Python

numbers = [12, 3, 18, 10, 7, 2, 3, 6, 1] #Variable name storing the list
sum = 0
for i in numbers:
    sum = sum + i
print("The sum is" , sum)


def add(list):
    sum = 0
    for i in list:
        sum = sum + i
    print("The sum is" , sum)

marks=[3,8,19,6,18,29,15]
ages=[12,17,14,18,11,10,16]
mileage=[15,67,89,123,76,83]
cups=[7,10,3,5,8,16,13]


add(marks)

