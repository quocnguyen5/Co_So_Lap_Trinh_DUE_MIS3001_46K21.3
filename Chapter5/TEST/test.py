# B = [1, 2, 3, 4.5]
# # print(len(L))

# # # for i in range(len(L)):
# # # print(L[i])
# # print(L.index(2))

# # L = []
# # n = int(input('n='))
# # for i in range(n):
# #     L.append(input())
# # x = int(input('x='))

# # del(L[1:(len(L)-1)])

# # max = L[1]
# # for x in range(len(L)):
# #     if L[x] > max:
# #         max = L[x]
# # print(L)
# # print(max)
# print(B[1])
# # for i in range(len(B)):
# #     while B[i] > B[i+1]:
# #         B[i] = B[i+1]
# #         B[i+1] = B[i]
# A = B.copy()
# print(A)
# names = ['an ', '”Nam”', ' “Binh”', '“Ngoc']
# x1 = names.pop(0)
# x2 = names.pop(-1)
# print(x1)
# print(x2)
# print(names)

# import copy
# numbers1 = [1,2,3,4,5]
# numbers2 = copy.copy(numbers1)
# print(numbers2)
# numbers3 = numbers1
# numbers3[2] = 6
# print(numbers3)


L = [1, 1, 2, 2, 3, 4, 4]
L = list(set(L))
print(L)
