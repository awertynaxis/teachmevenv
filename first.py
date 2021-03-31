#Task 10
numbers = '1,100,15,17,3,221,9,5,7,2,8,11'
result = {}
numbers=numbers.split(',')
for x in numbers:
    result[int(x)]=int(x)**3
print(result)
# Ваше решение

# Тесты
assert all(number in result and result[number] == number * number * number for number in (1, 100, 15, 17, 3, 221, 9, 5, 7, 2, 8, 11))