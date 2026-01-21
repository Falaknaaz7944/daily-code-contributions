#performing operations on list
li = list(map(int, input().split()))

li.insert(0, 5)
li.insert(1, 10)
li.insert(0, 6)
print(li)

li.remove(6)
li.append(9)
li.append(1)
li.sort()
print(li)

li.pop()
li.reverse()
print(li)
