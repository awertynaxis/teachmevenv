#Task 10
numbers = '1,100,15,17,3,221,9,5,7,2,8,11'
result = {}
d=''
for x in numbers:
    if x !=',':
        d+=x
    if x==',':
        result[int(d)]=int(d)**3
        d=''
result[int(d)]=int(d)**3
print(result)
# Ваше решение

# Тесты
assert all(number in result and result[number] == number * number * number for number in (1, 100, 15, 17, 3, 221, 9, 5, 7, 2, 8, 11))