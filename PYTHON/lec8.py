# set    it is immutable
a1={2,3,4,5,6,6,6}
a2=(67,44,5,5,4)
print(a1)    #{2, 3, 4, 5, 6}  not double value
print(a1.pop())   # it pop any number in the sset not last number
print(a1.add(876))

print(a1.union(a2))
print(a1.intersection(a2))
print(a1.symmetric_difference(a2))
