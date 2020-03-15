print('Enter number of clouds :')
n = int(input())
print('Enter cloud array :')


cloud_list = list(map(int, input().split()))
# for x in range(c):
#     z = input()
#     cloud_list.append(z)

print(cloud_list)

curCloud = 0

for c in range(n):
    if c <= n-2:
        if cloud_list[c + 2] == 0:
            curCloud = c + 2
        elif c <= n-1:
            if cloud_list[c + 1] == 0:
                curCloud = c + 1
print(curCloud)

# for c in range(n):
#     print(c)
#     if c <= n-2:
#         print("*")
#            if cloud_list[c + 2] == 0:
#                 print("**")
#                 curCloud = c + 2
#             elif c <= n-1:
#                 print("***")
#             if cloud_list[c + 1] == 0 and cloud_list[c + 2] <= n:
#                 print("****")
#                 curCloud = c + 1


# print(curCloud)
