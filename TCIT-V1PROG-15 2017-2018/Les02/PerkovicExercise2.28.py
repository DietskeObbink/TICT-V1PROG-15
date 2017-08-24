lst = [2, 7, 9, 5, 1, 8, 6]

middle = len(lst)/2 + 0.5
middle = middle - 1
print(middle)

middle = int(middle)
print(lst[middle])

lst.sort()
print(lst)

firstnumber = lst[0]
lst.remove(lst[0])
lst.append(firstnumber)
print(lst)

