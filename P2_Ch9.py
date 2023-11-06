family = ['Smith', 'Mary', 'Alicia', 'Elijah']
print(family)
print(family[0])
print(len(family))

numbers = [312, 1434, 68764, 4627, 84, 470, 470, 9047, 98463, 389, 2]
high = numbers[0]
for number in numbers:
    if number > high:
        high = number
        print(f"The highest number is {high}")

matrix = [
    [19, 11, 91],
    [41, 25, 54],
    [86, 28, 21]
]
print(matrix[0][0])
print(matrix[1][1])
print(matrix[-1][-1])
print(matrix[2][0])

#List Methods

numbers = [11, 22, 33, 44, 55, 66, 77]
#numbers.append(10)
#numbers.insert(2, 20)
numbers.remove(77)
#numbers.clear
numbers.index(44)
print(numbers)
#print(numbers.index(120))
print(43 in numbers)
print(numbers.count(77))

#Tuples

numbers = (19, 21, 28, 10, 11)
print(numbers)
#numbers[0] = 10

ages = (25, 30, 35, 40)
Drake = ages[0]
Emma = ages[1]
Sully = ages[2]

#Drake, Emma, Sully, Sam = ages

# Python Dictionaries
AlumniAge = {'Andrea': 23, 'John': 28}

user_one = { #Dictionaries are represented by {}
    'name': 'Sam',
    'age': 40,
    'phone': 123456789,
    'married': False,
    'married': True    
}
print(user_one['married'])
user_one['profession'] = 'programmer'
print(user_one.get('kids', 'invalid'))