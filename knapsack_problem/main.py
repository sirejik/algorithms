"""
Problem statement: The knapsack problem is a problem in combinatorial optimization: Given a set of items, each with a
weight and a value, determine the number of each item included in a collection so that the total weight is less than or
equal to a given limit and the total value is as large as possible.

Average complexity: О(N * KNAPSACK_SIZE).
"""
from collections import namedtuple
from prettytable import PrettyTable

Item = namedtuple('Item', ('name', 'weight', 'value'))

items = [
    Item(name='Item 1', weight=30, value=75),
    Item(name='Item 2', weight=50, value=80),
    Item(name='Item 3', weight=40, value=100),
    Item(name='Item 4', weight=20, value=50),
    Item(name='Item 5', weight=20, value=40),
    Item(name='Item 6', weight=23, value=80),
    Item(name='Item 7', weight=20, value=30),
    Item(name='Item 8', weight=10, value=30),
    Item(name='Item 9', weight=20, value=60),
    Item(name='Item 10', weight=15, value=20),
    Item(name='Item 11', weight=15, value=30),
    Item(name='Item 12', weight=25, value=45),
    Item(name='Item 13', weight=25, value=70),
    Item(name='Item 14', weight=15, value=30)
]
KNAPSACK_SIZE = 100
N = len(items)

dynamic_table = [[0 for j in range(0, KNAPSACK_SIZE + 1)] for i in range(0, N + 1)]
for i in range(0, N + 1):
    for j in range(0, KNAPSACK_SIZE + 1):
        if i == 0 or j == 0:
            dynamic_table[i][j] = 0
        elif items[i - 1].weight > j:
            dynamic_table[i][j] = dynamic_table[i - 1][j]
        else:
            dynamic_table[i][j] = max(
                dynamic_table[i - 1][j],
                items[i - 1].value + dynamic_table[i - 1][j - items[i - 1].weight]
            )

solution = []
total_weight = KNAPSACK_SIZE
total_value = dynamic_table[N][KNAPSACK_SIZE]
for i in range(N, 0, -1):
    if total_value <= 0:
        break
    if total_value == dynamic_table[i - 1][total_weight]:
        continue
    else:
        item = items[i - 1]
        solution.append(item)
        total_weight -= item.weight
        total_value -= item.value


solution.sort(key=lambda x: x.name)
table = PrettyTable()
table.field_names = ['Name', 'Weight', 'Value']
for field in table.field_names:
    table.align[field] = 'l'

for i in range(len(solution)):
    table.add_row([solution[i].name, solution[i].weight, solution[i].value])

print(table)
