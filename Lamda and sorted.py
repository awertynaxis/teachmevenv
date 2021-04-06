initial = [(1, 2, 1), (1, 2, 5), (1, 2, 10), (1, 1, 1), (1, 1, 10), (0, 10, 10), (0, 9, 5)]
result = []
from operator import itemgetter
#Первый вариант
sorted(initial,key=itemgetter(1,0),reverse=True)
result=sorted(initial,key=itemgetter(2))
#Второй вариант
sorted(initial,key=lambda tuplets:tuplets[0],reverse=True)
sorted(initial,key=lambda tuplets:tuplets[1],reverse=True)
sorted(initial,key=lambda tuplets:tuplets[2])

assert result == [(0, 9, 5), (0, 10, 10), (1, 1, 10), (1, 1, 1), (1, 2, 10), (1, 2, 5), (1, 2, 1)]