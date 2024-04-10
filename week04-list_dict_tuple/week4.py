cheeses = ['Cheddar', 'Edam', 'Gouda']
cheeses.remove('Edam')
cheeses.append('Brie')
print(cheeses)

for cheese in cheeses:
    print(cheese)

'this key' in person # will check the keys only

'this key' in person.keys()
'this key' in person.values()


# # mylist = ['rully', '201', 'someone else']
# # for item in mylist:
# #     print(item)


# name = 'rully'
# course = '201'
# person = {
#     'name': name, 
#     'course': course, 
#     'name': 'someone else'
# }

# for key in person:
#     # print(key)
#     print(person[key])

# # items returns a list of key-value pairs
# for key, value in person.items():
#     print(key, value)

# # keys, values, items are all list-like objects
# print(person.keys())
# print('name' in person.keys())
# print(person.values())
# print(person.items()) # return a list of key-value pairs


# # name = 'rully'
# # course = '201'
# # # person = [name, course]
# # person = {'name': name, 'course': course, 'name': 'someone else'}
# # # dictionary is a collection of key-value pairs

# # person = { name,  course, name }
# # # set is a collection of unique values
# # print(person)

# # # key = 'name'
# # # print(key, person[key])



# # # a = 5
# # # b = 5
# # # c = [1, 2, 3]
# # # d = [1, 2, 3]

# # # e = d # does not create a new list, just a new reference to the same list

# # # print(a == b)
# # # print(a is b)
# # # print(c == d)
# # # print(c is d)
# # # print(e is d)

# # # # value: int, float, boolean
# # # # object: list, tuple, dictionary, set

# # # # nums = ['3', '41, 12, 9, 74, 15']
# # # # print(' '.join(nums))

# # # # s = 'pining for the fjords'
# # # # t = s.split()
# # # # print(t)

# # # # # nums = [3, 41, 12, 9, 74, 15]
# # # # # print(len(nums))
# # # # # print(max(nums))
# # # # # print(min(nums))
# # # # # print(sum(nums))
# # # # # print(sum(nums)/len(nums))

# # # # # # t = ['a', 'b', 'c']
# # # # # # x = t.pop(0)
# # # # # # print(t)
# # # # # # print(x)

# # # # # # # t = ['d', 'b', 'A', 'B', 'a']
# # # # # # # t.sort()
# # # # # # # print(t)


# # # # # # # # t = ['a', 'b', 'c', 'd', 'e', 'f']
# # # # # # # # #     0    1    2    3    4    5
# # # # # # # # print(t[0])
# # # # # # # # print(t[-2:-1])
# # # # # # # # # left part is the first element to be included, index starts at 0
# # # # # # # # # right part is the first element to be excluded

# # # # # # # # print(t[2:4])

# # # # # # # # print(t[:])
# # # # # # # # print(t)







# # # # # # # # # # mylist = ['spam', 2.0, 5, [10, 20]]
# # # # # # # # # # nestedlist = mylist[3]
# # # # # # # # # # print(nestedlist)
# # # # # # # # # # print(nestedlist[0])
# # # # # # # # # # print(mylist[3][0])

# # # # # # # # # # empty = []
# # # # # # # # # # print(empty)

# # # # # # # # # # s = 'abcd'
# # # # # # # # # # # s as string is immutable
# # # # # # # # # # s[0] = 'z'
# # # # # # # # # # print(s[0])

# # # # # # # # # s = ['a', 'b', 'c', 'd']
# # # # # # # # # # s[0] = 'z'
# # # # # # # # # print(s)
# # # # # # # # # print('z' in s)

# # # # # # # # # for i in s:
# # # # # # # # #     if i == 'z':
# # # # # # # # #         print('True')
        
# # # # # # # # # s[1] = 10
# # # # # # # # # print(s)

# # # # # # # # # s[1] = s[1] * 2
# # # # # # # # # print(s)

# # # # # # # # # s = [1, 2, 3, 4]
# # # # # # # # # s = s * 2 # might give you a semantic error
# # # # # # # # # # this is not a multiplication s = [2, 4, 6, 8]
# # # # # # # # # print(s)

# # # # # # # # # t = [4, 5, 6]
# # # # # # # # # print(s+t)




# # # # # # # # # # smallest = None # accumulator variable
# # # # # # # # # # sum = 0 # accumulator variable
# # # # # # # # # # print('Before:', smallest)
# # # # # # # # # # for itervar in [3, 41, 12, 1, 74, 15]:
# # # # # # # # # #     if (smallest is None) or (itervar < smallest):
# # # # # # # # # #         smallest = itervar # update accumulator variable
# # # # # # # # # #     print('Iteration:', itervar, smallest)
# # # # # # # # # # print('Smallest:', smallest)





# # # # # # # # # # x = ['a', 20, 30, 40]
# # # # # # # # # # # iteration variable i
# # # # # # # # # # i = 0
# # # # # # # # # # while i < len(x):
# # # # # # # # # #     print(i)
# # # # # # # # # #     print(x[i])
# # # # # # # # # #     i = i + 1

# # # # # # # # # # i is the iterator
# # # # # # # # # # for i in x:
# # # # # # # # # #     print(i)

# # # # # # # # # # n = 10
# # # # # # # # # # while True:
# # # # # # # # # #     print(n, end=' ')
# # # # # # # # # #     n = n - 1
# # # # # # # # # #     print(n, end=' ')
# # # # # # # # # #     if n == 9:
# # # # # # # # # #         continue
# # # # # # # # # #     break
# # # # # # # # # # print('Done!')