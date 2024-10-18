result = ['a', 'b']

elements = ['c', 'd']
result.append([*elements[:1], "first", *elements[1:]])

print(result)