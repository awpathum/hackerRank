#n as an integer input
n = int(input())

#Space seperated line input 
sc = list(map(int,input().split()))


# print(sc.count(1))


#Selecting distinct values from socks
output = []
for x in sc:
    if x not in output:
        output.append(x)

#Getting socks count by colors
pairs = {}
for x in range(len(output)):
    c = sc.count(output[x])
    pairs.update({output[x] : c})

#Remove if one sock form a color
#pairs = {key:val for key, val in pairs.items() if val != 1}



pairValues = list(pairs.values())
#print(pairValues)
c = 0
for x in range(len(pairs)):

    c =  c + pairValues[x] // 2
    #print(c)
print(c)
        

# for x in range(len(newPairs)):
#     newPairs[]





# print(newPairs)






# count = output.count(1)


# for x in range(len(output)):
#     count = 0
#     for y in range(1,len(output)):
#         print(output[y])
#         if output[x] == output[y]:
#             count = count + 1
#             print(count)
#     scCount.update({output[x]:count})



# print(n)
# print(socks)