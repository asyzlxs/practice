# coding=utf-8
from collections import Counter
import json
from itertools import combinations
from more_itertools import chunked

a = 3
b = 6
print "a:", a, "b:", b
a, b = b, a
print "a:", a, "b:", b

some_list = [1, 2, 3, 4, 5]
another_list = [x + 1 for x in some_list]
print another_list

c = Counter('hello world')
print c, c.most_common(2)

data = {"status": "OK", "count": 2, "results": [{"age": 27, "name": "Oz", "lactose_intolerant": 'true'},
                                                {"age": 29, "name": "Joe", "lactose_intolerant": 'false'}]}
print(json.dumps(data, indent=2))

print "hello" if True else "world"

x = 2
if 1 < x > 0:
    print x

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = zip(a, b, c)
for i, j, k in zip(a, b, c):
    print i + j + k
for index, num in enumerate(a):
    print index, num

numbers = [1, 2, 3, 4, 5, 6]
even = []
even = [number for number in numbers if number % 2 == 0]
print even

city = ["beijing", "shanghai", "guangzhou", "shenzhen"]
city_dict = {value: key for key, value in enumerate(city)}
print city_dict
print ",".join(city)

is_beijing = city_dict.get("beijing", False)
is_nanjing = city_dict.get("nanjing", False)
print is_beijing, is_nanjing

for city_team in combinations(city, 3):
    print city_team

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in chunked(numbers, 3):
    print num

f = open('../tmp/a', 'a')
f.write('hello world\n')
f.close()

with open('../tmp/a', 'a') as f:
    f.write('with hello world\n')

import heapq


def heap_sort(iterable):
    h = []
    for i in iterable:
        heapq.heappush(h, i)
    return [heapq.heappop(h) for i in range(len(h))]


s = [1, 4, 5, 6, 8, 9, 2, 3, 10]
print heap_sort(s)

portfolio = [{'name': 'IBM', 'shares': 100, 'price': 91.1},
             {'name': 'AAPL', 'shares': 50, 'price': 543.22},
             {'name': 'FB', 'shares': 200, 'price': 21.09},
             {'name': 'HPQ', 'shares': 35, 'price': 31.75},
             {'name': 'YHOO', 'shares': 45, 'price': 16.35},
             {'name': 'ACME', 'shares': 75, 'price': 115.65}]

print heapq.nlargest(3, portfolio, key=lambda keys: keys['price'])
top_n_small = heapq.nsmallest(3, portfolio, key=lambda keys: keys['price'])
print top_n_small

for i in top_n_small:
    print i['name']





